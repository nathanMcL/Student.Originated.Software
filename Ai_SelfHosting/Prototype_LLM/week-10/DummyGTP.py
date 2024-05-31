import torch
import torch.nn as nn
from GPT_CONFIG_124M import GPT_CONFIG_124M

# Implementing a GPT model from scratch to generate text.
# Pg 110: Dummy GPT Model: 

class DummyGPTModel(nn.Module):
    def __init__(self, cfg):
        super().__init__()
        self.tok_emb = nn.Embedding(cfg["vocab_size"], cfg["emb_dim"])
        self.pos_emb = nn.Embedding(cfg["context_length"], cfg["emb_dim"])
        self.drop_emb = nn.Dropout(cfg["drop_rate"])
        self.trf_blocks = nn.Sequential(
            *[DummyTransformerBlock(cfg) for _ in range(cfg["n_layers"])])  # A: Use a placeholder for TransformerBlock
        self.final_norm = DummyLayerNorm(cfg["emb_dim"])   # B: Use a placeholder for LayerNorm
        self.out_head = nn.Linear(
            cfg["emb_dim"], cfg["vocab_size"], bias=False)
        

    def forward(self, in_idx):
        batch_size, seq_len = in_idx.shape
        tok_embeds = self.tok_emb(in_idx)
        pos_embeds = self.pos_emb(torch.arange(seq_len, device=in_idx.device))
        x = tok_embeds + pos_embeds
        x = self.drop_emb(x)
        x = self.trf_blocks(x)
        x = self.final_norm(x)
        logits = self.out_head(x)
        return logits

# C: A placeholder class that will be replaced by a real TransformerBlock later
class DummyTransformerBlock(nn.Module):
    def __init__(self, cfg):
        super().__init__()

    # D: This block does nothing and just returns its input.
    def forward(self, x):
        return x


# E: A simple placeholder class that will be replaced by a real TransformerBlock later
class DummyLayerNorm(nn.Module):
    def __init__(self, normalized_shape, eps=1e-5):  # F: The parameters here are just to mimic the LayerNorm interface.
        super().__init__()

    def forward(self, x):
        return x



