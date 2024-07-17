# 07/16/2024 GPT-Neo 125M

- Model Overview
The GPT-Neo 125M is a transformer-based model developed by EleutherAI, emulating the architecture of GPT-3. The term GPT-Neo refers to the family of models, and 125M signifies that this specific pre-trained model comprises 125 million parameters.<br>

- Training Data
The GPT-Neo 125M model was trained using the Pile, an extensive and meticulously curated dataset assembled by EleutherAI, specifically for training such models.

- Training Process
The GPT-Neo 125M underwent training on the Pile dataset, processing 300 billion tokens over 572,300 steps. The training was conducted as a masked autoregressive language model, utilizing cross-entropy loss to optimize performance.

In `previous_chapters.py`

```
# Remove or comment out the model architecture code
#####################################
# Chapter 3 & 4 (Comment out these sections)
#####################################
# class MultiHeadAttention(nn.Module):
#     ...

# class LayerNorm(nn.Module):
#     ...

# class GELU(nn.Module):
#     ...

# class FeedForward(nn.Module):
#     ...

# class TransformerBlock(nn.Module):
#     ...

# class GPTModel(nn.Module):
#     ...

```

- Import the `GPT-Neo 125M` components:<br>

`from transformers import GPT2Tokenizer, GPTNeoForCausalLM`<br>

- Replace the initialization of `GPTModel` and the `tokenizer` in the main function:<br>

```
try:
    tokenizer = GPT2Tokenizer.from_pretrained("EleutherAI/gpt-neo-125M")
    model = GPTNeoForCausalLM.from_pretrained("EleutherAI/gpt-neo-125M")
    model.to(device)
    optimizer = torch.optim.AdamW(
        model.parameters(), lr=settings["learning_rate"], weight_decay=settings["weight_decay"]
    )
```

- Update the `generate_and_print_sample` function:<br>

```
def generate_and_print_sample(model, tokenizer, device, start_context):
    model.eval()
    encoded = tokenizer.encode(start_context, return_tensors='pt').to(device)
    with torch.no_grad():
        output = model.generate(encoded, max_length=50)
        decoded_text = tokenizer.decode(output[0], skip_special_tokens=True)
        print(decoded_text.replace("\n", " "))  # Compact print format
    model.train()
    return decoded_text.replace("\n", " ")  # Return the generated sentence

```

- Ensure `train_model_simple` function:<br>

```
def train_model_simple(model, train_loader, val_loader, optimizer, device, num_epochs,
                       eval_freq, eval_iter, start_context, tokenizer, logger, resource,
                       accumulation_steps=4, system_logger=None, early_stopping=None):
```
<br>



## Issues...

- 07/16/2024 Froze at Ep4
```
Ep 4 (Step 001055): Train loss 2.897, Val loss 5.351
EarlyStopping counter: 73 out of 100
Validation loss: 5.351215
```





## TODO:
- Always Seek Improvements


### Resources

- https://huggingface.co/EleutherAI/gpt-neo-125m 
