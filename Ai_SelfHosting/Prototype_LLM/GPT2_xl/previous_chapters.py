import torch  # type: ignore

from transformers import GPT2Tokenizer, GPT2LMHeadModel   # type: ignore
from torch.utils.data import Dataset, DataLoader # type: ignore
from joblib import Memory # type: ignore

# Set up caching
memory = Memory("cache_dir", verbose=0)

#####################################
# Chapter 2
#####################################


class GPTDatasetV1(Dataset):
    def __init__(self, txt, tokenizer, max_length, stride):
        self.input_ids, self.target_ids = self.process_chunks(txt, tokenizer, max_length, stride)
        
    @staticmethod
    @memory.cache  # Cashe the results of the this method
    def process_chunks(txt, tokenizer, max_length, stride):
        input_ids = []
        target_ids = []

        # Tokenize the entire text
        token_ids = tokenizer.encode(txt)
        
        # Use a sliding window to chunk the text into overlapping sequences of max_length
        for i in range(0, len(token_ids) - max_length, stride):
            input_chunk = token_ids[i:i + max_length]
            target_chunk = token_ids[i + 1:i + max_length + 1]
            input_ids.append(torch.tensor(input_chunk))
            target_ids.append(torch.tensor(target_chunk))
        return input_ids, target_ids

    def __len__(self):
        return len(self.input_ids)

    def __getitem__(self, idx):
        return self.input_ids[idx], self.target_ids[idx]


def create_dataloader_v1(txt, batch_size=4, max_length=1024,
                         stride=512, shuffle=True, drop_last=True, num_workers=2):  # Use multiple worker threads. Started with 2.
    """
    Create a DataLoader for the GPT dataset.

    Parameters:
    - txt: The text data to load.
    - batch_size: The number of samples per batch.
    - max_length: The maximum length of each sequence.
    - stride: The stride for the sliding window.
    - shuffle: Whether to shuffle the data.
    - drop_last: Whether to drop the last batch if it's incomplete.
    - num_workers: The number of worker threads to use for loading data.

    Returns:
    - DataLoader object for the dataset.
    """
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2-xl")
    dataset = GPTDatasetV1(txt, tokenizer, max_length, stride)
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=shuffle, drop_last=drop_last, num_workers=num_workers)
    return dataloader


#####################################
# Chapter 3
#####################################

class GPTModel:
    def __init__(self):
        self.model = GPT2LMHeadModel.from_pretrained("gpt2-xl")

    def forward(self, input_ids):
        return self.model(input_ids).logits

def generate_text_simple(model, idx, max_new_tokens, context_size):
    model.model.eval()
    with torch.no_grad():
        output = model.model.generate(input_ids=idx, max_length=context_size + max_new_tokens, pad_token_id=model.model.config.eos_token_id)
    return output

if __name__ == "__main__":

    GPT_CONFIG_XL = {
        "vocab_size": 50257,     # Vocabulary size
        "context_length": 1024,  # Context length
        "emb_dim": 1600,         # Embedding dimension for GPT-2 XL
        "n_heads": 25,           # Number of attention heads for GPT-2 XL
        "n_layers": 48,          # Number of layers for GPT-2 XL
        "drop_rate": 0.1,        # Dropout rate
        "qkv_bias": False        # Query-Key-Value bias
    }

    torch.manual_seed(123)
    model = GPTModel()
    model.model.eval()  # disable dropout

    start_context = "Hello, I am"

    tokenizer = GPT2Tokenizer.from_pretrained("gpt2-xl")
    encoded = tokenizer.encode(start_context, return_tensors="pt")
    encoded_tensor = encoded

    out = generate_text_simple(
        model=model,
        idx=encoded_tensor,
        max_new_tokens=10,
        context_size=GPT_CONFIG_XL["context_length"]
    )
    decoded_text = tokenizer.decode(out.squeeze(0).tolist())

    print(f"\n\n{50*'='}\n{22*' '}OUT\n{50*'='}")
    print("\nOutput:", out)
    print("Output length:", len(out[0]))
    print("Output text:", decoded_text)