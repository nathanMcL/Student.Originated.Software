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
*This should all the steps*
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

- In Power Shell enter update to latest version: <br>
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
- I am still trying to investigating the Failed NVML issues...

  

## TODO:
- Always Seek Improvements
- Practice creating unit tests
- Source more data for resource folder

### Resources

- https://huggingface.co/openai-community/gpt2
- https://huggingface.co/openai-community/gpt2-medium
- https://huggingface.co/openai-community/gpt2-xl



