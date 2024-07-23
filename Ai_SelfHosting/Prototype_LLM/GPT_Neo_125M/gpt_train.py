import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import pdfplumber
import os
import logging  # Logging
import multiprocessing as mp  # Parallel Data Loading
from datetime import datetime  # Import datetime for timestamping
from torch.optim.lr_scheduler import ReduceLROnPlateau

from transformers import GPT2Tokenizer, GPTNeoForCausalLM
from previous_chapters import create_dataloader_v1
from GPTLogging import GPTLogging
from GPTSystemLogging import GPTSystemLogger
from EarlyStopping import EarlyStopping

def text_to_token_ids(text, tokenizer):
    encoded = tokenizer.encode(text, return_tensors='pt')
    return encoded

def token_ids_to_text(token_ids, tokenizer):
    return tokenizer.decode(token_ids[0], skip_special_tokens=True)

def calc_loss_loader(data_loader, model, device, num_batches=None):
    total_loss = 0.
    if len(data_loader) == 0:
        return float("nan")
    elif num_batches is None:
        num_batches = len(data_loader)
    else:
        num_batches = min(num_batches, len(data_loader))
    for i, batch in enumerate(data_loader):
        if i < num_batches:
            input_batch = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)
            target_batch = input_batch.clone()
            loss = calc_loss_batch(input_batch, target_batch, model, attention_mask, device)
            total_loss += loss.item()
        else:
            break
    return total_loss / num_batches

def calc_loss_batch(input_batch, target_batch, model, attention_mask, device):
    input_batch = input_batch.to(device)
    target_batch = target_batch.to(device)
    attention_mask = attention_mask.to(device)

    # Forward pass
    output = model(input_batch, labels=target_batch, attention_mask=attention_mask)
    loss = output.loss

    return loss

def evaluate_model(model, train_loader, val_loader, device, eval_iter):
    model.eval()
    with torch.no_grad():
        train_loss = calc_loss_loader(train_loader, model, device, num_batches=eval_iter)
        val_loss = calc_loss_loader(val_loader, model, device, num_batches=eval_iter)
    model.train()
    return train_loss, val_loss

def generate_and_print_sample(model, tokenizer, device, start_context):
    model.eval()
    encoded = tokenizer.encode(start_context, return_tensors='pt').to(device)
    with torch.no_grad():
        output = model.generate(encoded, max_length=50, pad_token_id=tokenizer.pad_token_id)
        decoded_text = tokenizer.decode(output[0], skip_special_tokens=True)
        print(decoded_text.replace("\n", " "))  # Compact print format
    model.train()
    return decoded_text.replace("\n", " ")  # Return the generated sentence

def train_model_simple(model, train_loader, val_loader, optimizer, device, num_epochs,
                       eval_freq, eval_iter, start_context, tokenizer, logger, resource,
                       accumulation_steps=4, system_logger=None, early_stopping=None,
                       min_epochs=5):  # Add min_epochs parameter. Original min_epochs: `5`.
    train_losses, val_losses, track_tokens_seen = [], [], []
    tokens_seen = 0
    global_step = -1

    scheduler = ReduceLROnPlateau(optimizer, mode='min', factor=0.2, patience=5) # Original factor: 0.1, Original patience: 3

    for epoch in range(num_epochs):
        logger.start_epoch()  # Start timer for the epoch
        if system_logger:
            system_logger.log_during_training(epoch)  # Log system stats during training

        model.train()  # Set model to training mode
        total_steps = 0
        epoch_train_loss = []
        optimizer.zero_grad()  # Reset gradients

        for i, batch in enumerate(train_loader):
            input_batch = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)
            target_batch = input_batch.clone()
            loss = calc_loss_batch(input_batch, target_batch, model, attention_mask, device)
            loss.backward()  # Accumulate gradients

            if (i + 1) % accumulation_steps == 0:
                optimizer.step()  # Update model weights
                optimizer.zero_grad()  # Reset gradients

            tokens_seen += input_batch.numel()
            global_step += 1
            total_steps += 1
            epoch_train_loss.append(loss.item())

            if global_step % eval_freq == 0:
                train_loss, val_loss = evaluate_model(
                    model, train_loader, val_loader, device, eval_iter)
                train_losses.append(train_loss)
                val_losses.append(val_loss)
                track_tokens_seen.append(tokens_seen)
                print(f"Ep {epoch+1} (Step {global_step:06d}): "
                      f"Train loss {train_loss:.3f}, Val loss {val_loss:.3f}")

                if early_stopping and epoch >= min_epochs: # Check for early stopping before early stopping
                    early_stopping(val_loss, model)
                    if early_stopping.early_stop:
                        print("Early stopping")
                        break

        avg_train_loss = sum(epoch_train_loss) / len(epoch_train_loss)
        val_loss = sum(val_losses) / len(val_losses) if val_losses else float('nan')
        generated_sentence = generate_and_print_sample(
            model, tokenizer, device, start_context)
        logger.end_epoch(epoch+1, total_steps, avg_train_loss, val_loss, generated_sentence, resource)

        scheduler.step(val_loss)

        if early_stopping and early_stopping.early_stop:
            print(f"Early Stopping at epoch {epoch+1}")
            break

    return train_losses, val_losses, track_tokens_seen, model

def plot_losses(epochs_seen, tokens_seen, train_losses, val_losses):
    fig, ax1 = plt.subplots()

    ax1.plot(epochs_seen, train_losses, label="Training loss")
    ax1.plot(epochs_seen, val_losses, linestyle="-.", label="Validation loss")
    ax1.set_xlabel("Epochs")
    ax1.set_ylabel("Loss")
    ax1.legend(loc="upper right")

    ax2 = ax1.twiny()
    ax2.plot(tokens_seen, train_losses, alpha=0)
    ax2.set_xlabel("Tokens seen")

    fig.tight_layout()

def get_timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def setup_logging(log_file):
    logging.basicConfig(filename=log_file, level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s')

def load_data_parallel(resource_files):
    pool = mp.Pool(mp.cpu_count())
    raw_text_list = pool.map(load_single_file, resource_files)
    pool.close()
    pool.join()
    return ''.join(raw_text_list)

def load_single_file(data_path):
    if not os.path.isfile(data_path):
        raise FileNotFoundError(f"File not found at: {data_path}")
    with pdfplumber.open(data_path) as pdf:
        raw_text = ""
        for page in pdf.pages:
            raw_text += page.extract_text()
    return raw_text

def main(gpt_config, settings):
    setup_logging("training.log")
    system_logger = GPTSystemLogger()
    system_logger.log_before_training()

    torch.manual_seed(123)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    logging.info("Using device: %s", device)

    try:
        resource_files = [
            r"/mnt/d/myPython/SpringStudentOriginatedSoftware/AI_SelfHosting/Prototype_LLM/resources/ArtOfWar.pdf",
            r"/mnt/d/myPython/SpringStudentOriginatedSoftware/AI_SelfHosting/Prototype_LLM/resources/BlueBookTP600-4.pdf",
            r"/mnt/d/myPython/SpringStudentOriginatedSoftware/AI_SelfHosting/Prototype_LLM/resources/LDRSHIP_ARN36735-FM_6-22-000-WEB-1.pdf",
            r"/mnt/d/myPython/SpringStudentOriginatedSoftware/AI_SelfHosting/Prototype_LLM/resources/DrillandCer_ARN32297-TC_3-21.5-000-WEB-1.pdf",
            r"/mnt/d/myPython/SpringStudentOriginatedSoftware/AI_SelfHosting/Prototype_LLM/resources/PhysFitARN30964-FM_7-22-001-WEB-4.pdf",
            r"/mnt/d/myPython/SpringStudentOriginatedSoftware/AI_SelfHosting/Prototype_LLM/resources/FoodServ_ARN7458_R30_22_FINAL.pdf",
            r"/mnt/d/myPython/SpringStudentOriginatedSoftware/AI_SelfHosting/Prototype_LLM/resources/Nutrition_AR40-25_WEB_Final.pdf",
            r"/mnt/d/myPython/SpringStudentOriginatedSoftware/AI_SelfHosting/Prototype_LLM/resources/FirstAid_FM4-25.11.pdf",
            r"/mnt/d/myPython/SpringStudentOriginatedSoftware/AI_SelfHosting/Prototype_LLM/resources/fm4_40_QUARTERMASTER OPERATIONS.pdf"
        ]

        raw_text = load_data_parallel(resource_files)
        logging.info("Data loaded successfully")

    except Exception as e:
        logging.error("Error processing files:\n %s", e)
        raise

    text_data = raw_text
    resource_name = ", ".join([os.path.basename(file) for file in resource_files])

    try:
        tokenizer = GPT2Tokenizer.from_pretrained("EleutherAI/gpt-neo-125M")
        tokenizer.pad_token = tokenizer.eos_token  # Ensure pad token is set
        model = GPTNeoForCausalLM.from_pretrained("EleutherAI/gpt-neo-125M")
        model.to(device)
        optimizer = torch.optim.AdamW(
            model.parameters(), lr=settings["learning_rate"], weight_decay=settings["weight_decay"]
        )

        scheduler = ReduceLROnPlateau(optimizer, mode='min', factor=0.1, patience=10)

        train_ratio = 0.90
        split_idx = int(train_ratio * len(text_data))

        max_length = gpt_config["context_length"]
        train_loader = create_dataloader_v1(
            text_data[:split_idx],
            batch_size=settings["batch_size"],
            max_length=max_length,
            stride=max_length//2,
            drop_last=True,
            shuffle=True,
            num_workers=6 # Original value was: 4
        )

        val_loader = create_dataloader_v1(
            text_data[split_idx:],
            batch_size=settings["batch_size"],
            max_length=max_length,
            stride=max_length//2,
            drop_last=False,
            shuffle=False,
            num_workers=6 # Original value was: 4
        )

        logger = GPTLogging("training_log.csv", "chat_log.csv")
        logger.log_start_time()

        early_stopping = EarlyStopping(patience=200, verbose=True)

        train_losses, val_losses, tokens_seen, model = train_model_simple(
            model, train_loader, val_loader, optimizer, device,
            num_epochs=settings["num_epochs"], eval_freq=3, eval_iter=1, # Original `eval_freq`: `5`
            start_context="Discuss the importance of hydration and electrolyte balance in military nutrition.", tokenizer=tokenizer,
            logger=logger, resource=resource_name, accumulation_steps=4, system_logger=system_logger,
            early_stopping=early_stopping
        )

        system_logger.log_after_training()

        timestamp = get_timestamp()
        model_filename = f"model_{timestamp}.pth"
        torch.save(model.state_dict(), model_filename)
        logging.info("Model saved as %s", model_filename)

    except Exception as e:
        logging.error("Error during model training: %s", e)
        raise e

    return train_losses, val_losses, tokens_seen, model


if __name__ == "__main__":

    GPT_CONFIG_124M = {
        "vocab_size": 50257,    # Vocabulary size
        "context_length": 256,  # Shortened context length (orig: 1024)
        "emb_dim": 768,         # Embedding dimension. Orignial value was: 768. Test the value: 1024.
        "n_heads": 12,          # Number of attention heads. Orignial value was: 12. Test the value: 16.
        "n_layers": 12,         # Number of layers. Orignial value was: 12. Test the value: 24.
        "drop_rate": 0.3,       # Dropout rate. Original value was: 0.1. lower value for larger datasets, higher value for smaller datasets.
        "qkv_bias": False       # Query-Key-Value bias
    }

    OTHER_SETTINGS = {
        "learning_rate": 3e-4,  # Original value was: 5e-4,
        "num_epochs": 20,       # Increase number of epochs from 10 to 20
        "batch_size": 8,        # Increase the batch size or Decrease. Original value was: 2
        "weight_decay": 0.05     # Original value was: 0.1
    }

    train_losses, val_losses, tokens_seen, model = main(GPT_CONFIG_124M, OTHER_SETTINGS)

    epochs_tensor = torch.linspace(0, OTHER_SETTINGS["num_epochs"], len(train_losses))
    plot_losses(epochs_tensor, tokens_seen, train_losses, val_losses)
    plt.savefig("gpt_train_loss.pdf")

    torch.save(model.state_dict(), "model.pth")
    model = GPTNeoForCausalLM.from_pretrained("EleutherAI/gpt-neo-125M")
    model.load_state_dict(torch.load("model.pth"))
