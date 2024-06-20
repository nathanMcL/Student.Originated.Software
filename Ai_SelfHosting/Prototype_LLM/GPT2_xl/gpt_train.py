import matplotlib.pyplot as plt  # type: ignore
import torch  # type: ignore
import torch.nn as nn   # type: ignore
import pdfplumber  # type: ignore
import os
import logging
import multiprocessing as mp
from datetime import datetime
from transformers import GPT2Tokenizer, GPT2LMHeadModel, AdamW, get_linear_schedule_with_warmup  # type: ignore
from previous_chapters import create_dataloader_v1, generate_text_simple
from GPTLogging import GPTLogging

def text_to_token_ids(text, tokenizer):
    encoded = tokenizer.encode(text, return_tensors="pt")
    return encoded

def token_ids_to_text(token_ids, tokenizer):
    return tokenizer.decode(token_ids.squeeze().tolist())

def calc_loss_loader(data_loader, model, device, num_batches=None):
    total_loss = 0.
    if len(data_loader) == 0:
        return float("nan")
    elif num_batches is None:
        num_batches = len(data_loader)
    else:
        num_batches = min(num_batches, len(data_loader))
    for i, (input_batch, target_batch) in enumerate(data_loader):
        if i < num_batches:
            loss = calc_loss_batch(input_batch, target_batch, model, device)
            total_loss += loss.item()
        else:
            break
    return total_loss / num_batches

def calc_loss_batch(input_batch, target_batch, model, device):
    input_batch = input_batch.to(device)
    target_batch = target_batch.to(device)

    # Forward pass
    output = model(input_batch)
    logits = output.logits

    # Calculate loss
    criterion = nn.CrossEntropyLoss()
    loss = criterion(logits.view(-1, logits.size(-1)), target_batch.view(-1))

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
    context_size = model.config.n_positions
    encoded = text_to_token_ids(start_context, tokenizer).to(device)
    with torch.no_grad():
        token_ids = generate_text_simple(
            model=model, idx=encoded,
            max_new_tokens=50, context_size=context_size
        )
        decoded_text = token_ids_to_text(token_ids, tokenizer)
        print(decoded_text.replace("\n", " "))  # Compact print format
    model.train()
    return decoded_text.replace("\n", " ")  # Return the generated sentence

def train_model_simple(model, train_loader, val_loader, optimizer, device, num_epochs,
                       eval_freq, eval_iter, start_context, tokenizer, logger, resource, accumulation_steps=2):
    train_losses, val_losses, track_tokens_seen = [], [], []
    tokens_seen = 0
    global_step = -1

    scheduler = get_linear_schedule_with_warmup(optimizer, num_warmup_steps=100, num_training_steps=num_epochs * len(train_loader))

    for epoch in range(num_epochs):
        logger.start_epoch()
        model.train()
        total_steps = 0
        epoch_train_loss = []
        optimizer.zero_grad()

        for i, (input_batch, target_batch) in enumerate(train_loader):
            loss = calc_loss_batch(input_batch, target_batch, model, device)
            loss.backward()

            if (i + 1) % accumulation_steps == 0:
                optimizer.step()
                optimizer.zero_grad()
                torch.cuda.empty_cache()  # Clear the cache to free up memory

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

        avg_train_loss = sum(epoch_train_loss) / len(epoch_train_loss)
        val_loss = sum(val_losses) / len(val_losses) if val_losses else float('nan')
        generated_sentence = generate_and_print_sample(
            model, tokenizer, device, start_context)
        logger.end_epoch(epoch+1, total_steps, avg_train_loss, val_loss, generated_sentence, resource)

        scheduler.step()

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

    torch.manual_seed(123)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    logging.info("Using device: %s", device)

    try:
        resource_files = [
            r"/mnt/d/myPython/SpringStudentOriginatedSoftware/AI_SelfHosting/Prototype_LLM/resources/ArtOfWar.pdf",
            r"/mnt/d/myPython/SpringStudentOriginatedSoftware/AI_SelfHosting/Prototype_LLM/resources/BlueBookTP600-4.pdf",
            r"/mnt/d/myPython/SpringStudentOriginatedSoftware/AI_SelfHosting/Prototype_LLM/resources/LDRSHIP_ARN36735-FM_6-22-000-WEB-1.pdf",
            r"/mnt/d/myPython/SpringStudentOriginatedSoftware/AI_SelfHosting/Prototype_LLM/resources/DrillandCer_ARN32297-TC_3-21.5-000-WEB-1.pdf",
            r"/mnt/d/myPython/SpringStudentOriginatedSoftware/AI_SelfHosting/Prototype_LLM/resources/PhysFitARN30964-FM_7-22-001-WEB-4.pdf"
        ]

        raw_text = load_data_parallel(resource_files)
        logging.info("Data loaded successfully")

    except Exception as e:
        logging.error("Error processing files:\n %s", e)
        raise

    text_data = raw_text
    resource_name = ", ".join([os.path.basename(file) for file in resource_files])

    try:
        tokenizer = GPT2Tokenizer.from_pretrained("gpt2-xl")
        model = GPT2LMHeadModel.from_pretrained("gpt2-xl")
        model.to(device)
        optimizer = AdamW(model.parameters(), lr=settings["learning_rate"], weight_decay=settings["weight_decay"])

        train_ratio = 0.90
        split_idx = int(train_ratio * len(text_data))

        train_loader = create_dataloader_v1(
            text_data[:split_idx],
            batch_size=settings["batch_size"],
            max_length=gpt_config["context_length"],
            stride=gpt_config["context_length"] // 2,
            drop_last=True,
            shuffle=True,
            num_workers=2  # Number of workers: start with 2.
        )

        val_loader = create_dataloader_v1(
            text_data[split_idx:],
            batch_size=settings["batch_size"],
            max_length=gpt_config["context_length"],
            stride=gpt_config["context_length"] // 2,
            drop_last=False,
            shuffle=False,
            num_workers=2  # Number of workers: start with 2.
        )

        logger = GPTLogging("training_log.csv", "chat_log.csv")
        logger.log_start_time()

        train_losses, val_losses, tokens_seen, model = train_model_simple(
            model, train_loader, val_loader, optimizer, device,
            num_epochs=settings["num_epochs"], eval_freq=5, eval_iter=1,
            start_context="What is the first General Order?", tokenizer=tokenizer, logger=logger, resource=resource_name, accumulation_steps=2
        )

        timestamp = get_timestamp()
        model_filename = f"model_{timestamp}.pth"
        model.save_pretrained(model_filename)
        logging.info("Model saved as %s", model_filename)

    except Exception as e:
        logging.error("Error during model training: %s", e)
        raise e

    return train_losses, val_losses, tokens_seen, model

if __name__ == "__main__":
    GPT_CONFIG_XL = {
        "vocab_size": 50257,
        "context_length": 1024,
        "emb_dim": 1600,
        "n_heads": 25,
        "n_layers": 48,
        "drop_rate": 0.2, # Dropout rate: start at 0.2.
        "qkv_bias": False
    }

    OTHER_SETTINGS = {
        "learning_rate": 2e-4,  # Learning Rate: start at 1e-4
        "num_epochs": 20,  # Epochs: start at 20
        "batch_size": 1,   # Batch size: start with 1 to reduce memory usage.
        "weight_decay": 0.2
    }

    train_losses, val_losses, tokens_seen, model = main(GPT_CONFIG_XL, OTHER_SETTINGS)

    epochs_tensor = torch.linspace(0, OTHER_SETTINGS["num_epochs"], len(train_losses))
    plot_losses(epochs_tensor, tokens_seen, train_losses, val_losses)
    plt.savefig("gpt_train_loss.pdf")

    torch.save(model.state_dict(), "model.pth")
    model = GPT2LMHeadModel.from_pretrained("gpt2-xl")
    model.load_state_dict(torch.load("model.pth"))
