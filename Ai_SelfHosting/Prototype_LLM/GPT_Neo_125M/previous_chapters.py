import torch
from torch.utils.data import Dataset, DataLoader
from joblib import Memory
from transformers import GPT2Tokenizer

# Set up caching
memory = Memory("cache_dir", verbose=0)

#####################################
# Chapter 2
#####################################

class GPTDatasetV1(Dataset):
    def __init__(self, txt, tokenizer, max_length, stride):
        self.input_ids, self.target_ids = self.process_chunks(txt, tokenizer, max_length, stride)
        
    @staticmethod
    @memory.cache  # Cache the results of this method
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


def create_dataloader_v1(txt, batch_size=8, max_length=256,  # Original `batch_size`: `4`
                         stride=128, shuffle=True, drop_last=True, num_workers=4):
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
    dataset = GPTDatasetV1(txt, tokenizer, max_length, stride)
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=shuffle, drop_last=drop_last, num_workers=num_workers)
    return dataloader