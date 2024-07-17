I created a Wiki DevDiary for:
```
Ai_SelfHosting 
```
## Start Here...<br>
https://github.com/nathanMcL/Student.Originated.Software/wiki/Ai-Selfhosting<br>

## GPT2_Medium


```
GPT-2 Medium (345M parameters)
GPU: NVIDIA GPU with at least 12-16 GB of VRAM (e.g., RTX 2080 Ti, RTX 3080).
RAM: 32 GB of system RAMStorage.
SSD with at least 100 GB of free spaceCPU. Modern multi-core CPU (e.g., Intel i7 or AMD Ryzen 7)
CUDA and cuDNN: Installed and compatible with the GPU and PyTorch version
```

- To implement the GPT2-medium I had to remove code and change import dependencies<br>
 from:
- `previous_chapters` all of chapter four, lines 125 through 247.

```
#####################################
# Chapter 4
#####################################
```
- Change the tokenizer from `gpt2` to `gpt2-medium`

```
tokenizer = tiktoken.get_encoding("gpt2-medium")
```

### Swapping out & in
- I have been attempting to resolve the import dependencies one by one. Instead of chaining the import install commands togeather.
- While swapping in the GPT2_medium, I am having to resolve a lot of yellow warnings within `gpt_train.py`, & `previous_chapters.py` code before I have the chance to run the program.
- I do not think they are necessary to write about... I'm not sure if what I did resolved the issue until I run the program...
- FYI, different Operating Systems and Coding interpreters might have different messages when attempting to swap out one code for another while attempting to use the framework of the previous model...

- That all said... I need to ensure I post the notable changes that are needed to swap in the different models...

## 07/12/2024 Setting up Cuda
*This should be all the steps* <br>
starting in my Windows VScode, WSL, Ubuntu terminal...<br>
- The following are the commands I used to install `Cuda`...

- First, Remove any previous Cuda repositories
```
sudo rm /etc/apt/sources.list.d/cuda*
```
  
- Add the cuda repo for Ubuntu 22.04 <br>
```wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-ubuntu2204.pin && sudo mv cuda-ubuntu2204.pin /etc/apt/preferences.d/cuda-repository-pin-600 && ```

```sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/3bf863cc.pub && sudo add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/ /" ``` 

- Update the package list and install Cuda
```sudo apt-get update && sudo apt-get install -y nvidia-docker2 && sudo systemctl restart docker```

- In Power Shell:
- Update WSL to latest version: <br>
```wsl --update``` <br>
- Next, shutdown WSL <br>
```wsl --shutdown wsl``` <br>
- Then restart: <br>
```wsl``` <br>

- Back in the VS code, WSL, Ubuntu terminal verify that Cuda is installed correctly: <br>
```nvidia-smi``` <br>

- `Output` <br>

```
nvidia-smi
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2021 NVIDIA Corporation
Built on Thu_Nov_18_09:45:30_PST_2021
Cuda compilation tools, release 11.5, V11.5.119
Build cuda_11.5.r11.5/compiler.30672275_0
Failed to initialize NVML: N/A
Failed to properly shut down NVML: N/A
```
- I am still investigating the Failed NVML issues...


### 07/12/2024 12:45PM Prepping `GPT2_medium`... Before ...

- *Swapped in the GPT_medium*
> - Resolved all my import dependancies...<br>
> - Reconnected the main framework with the GPT2_medium...<br>
> - Resolved additional warnings...<br>

*Next Check Configuration Settings* <br>

- `EarlyStopping.py` set the `patience=75`
- `previous_chapters.py` set `num_workers=4` & `batch_size=4`
- `gpt_train.py` set `train_loader`'s workers to `num_workers=4`, & `val_loader`'s workers to `num_workers=4`
- `gpt_train.py` set `accumulation_steps=4`

```
GPT_CONFIG_MEDIUM = {
        "vocab_size": 50257,    # Vocabulary size
        "context_length": 1024,  # Context length. Orginal value was: 1024
        "emb_dim": 1024,         # Embedding dimension for GPT-2 Medium. Original value was: 1024
        "n_heads": 16,           # Number of attention heads for GPT-2 Medium. Original value was: 16
        "n_layers": 24,          # Number of layers for GPT-2 Medium. Original value was: 24
        "drop_rate": 0.3,       # Dropout rate. Original value was: 0.1
        "qkv_bias": False       # Query-Key-Value bias
    }

    OTHER_SETTINGS = {
        "learning_rate": 3e-4,  # Original value was: 5e-4,
        "num_epochs": 10,       # Increase number of epochs from 10 to 20
        "batch_size": 8,        # Increase the batch size or Decrease. Original value was: 2
        "weight_decay": 0.05     # Original value was: 0.1
    }

```
 
- attempt to run the program... ... but there might be errors 😭... lol... 🥹 <br>

## 07/16/2024 ... There were errors... TBC...


# 07/16/2024 GPT-Neo 125M
<br>
See:
https://github.com/nathanMcL/Student.Originated.Software/blob/main/Ai_SelfHosting/Prototype_LLM/GPT_Neo_125M/readme.md 
<br>

- Model Overview
The GPT-Neo 125M is a transformer-based model developed by EleutherAI, emulating the architecture of GPT-3. The term GPT-Neo refers to the family of models, and 125M signifies that this specific pre-trained model comprises 125 million parameters.<br>

- Training Data
The GPT-Neo 125M model was trained using the Pile, an extensive and meticulously curated dataset assembled by EleutherAI, specifically for training such models.

- Training Process
The GPT-Neo 125M underwent training on the Pile dataset, processing 300 billion tokens over 572,300 steps. The training was conducted as a masked autoregressive language model, utilizing cross-entropy loss to optimize performance.






  

## TODO:
- Always Seek Improvements
- Practice creating unit tests
- Source more data for resource folder

### Resources

- https://huggingface.co/openai-community/gpt2
- https://huggingface.co/openai-community/gpt2-medium
- https://huggingface.co/openai-community/gpt2-xl



