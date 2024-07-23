import torch
from torch.utils.data import Dataset, DataLoader
from joblib import Memory
from transformers import GPT2Tokenizer, DataCollatorForLanguageModeling

# Set up caching
memory = Memory("cache_dir", verbose=0)

#####################################
# Chapter 2
#####################################

class GPTDatasetV1(Dataset):
    def __init__(self, txt, tokenizer, max_length, stride):
        self.tokenizer = tokenizer
        self.max_length = max_length
        self.stride = stride
        self.text_chunks = self.process_chunks(txt, max_length, stride)
        
    @staticmethod
    @memory.cache  # Cache the results of this method
    def process_chunks(txt, max_length, stride):
        text_chunks = []

        # Tokenize the entire text
        tokenizer = GPT2Tokenizer.from_pretrained("EleutherAI/gpt-neo-125M")  # Define the tokenizer variable
        tokenizer.pad_token = tokenizer.eos_token  # Set the pad token to eos_token
        token_ids = tokenizer.encode(txt)
        
        # Use a sliding window to chunk the text into overlapping sequences of max_length
        for i in range(0, len(token_ids) - max_length, stride):
            chunk = token_ids[i:i + max_length]
            text_chunks.append(chunk)
        
        # Handle the final chunk if the text length is not a perfect multiple of max_length
        if len(token_ids) > max_length:
            chunk = token_ids[-max_length:]
            text_chunks.append(chunk)

        return text_chunks

    def __len__(self):
        return len(self.text_chunks)

    def __getitem__(self, idx):
        return torch.tensor(self.text_chunks[idx], dtype=torch.long)


def create_dataloader_v1(txt, batch_size=6, max_length=256,  # Original `batch_size`: `4`
                         stride=128, shuffle=True, drop_last=True, num_workers=6): # Original `num_workers`: `4`
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
    tokenizer = GPT2Tokenizer.from_pretrained("EleutherAI/gpt-neo-125M")
    tokenizer.pad_token = tokenizer.eos_token  # Set the pad token to eos_token
    dataset = GPTDatasetV1(txt, tokenizer, max_length, stride)
    
    def collate_fn(batch):
        inputs = torch.nn.utils.rnn.pad_sequence(batch, batch_first=True, padding_value=tokenizer.pad_token_id)
        attention_mask = (inputs != tokenizer.pad_token_id).long()
        return {
            'input_ids': inputs,
            'attention_mask': attention_mask
        }
    
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=shuffle, drop_last=drop_last, num_workers=num_workers, collate_fn=collate_fn)
    return dataloader
