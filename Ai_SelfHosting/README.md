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
- I am have been attempting to resolve the import dependencies one by one. Instead of chaining the import install commands togeather.
- While swapping in the GPT2_medium, I am having to resolve a lot of yellow warnings within `gpt_train.py`, & `previous_chapters.py` code before I have the chance to run the program.
- I do not think they are necessary to write about... I'm not sure if what I did resolved the issue until I run the program...
- FYI, different Operating Systems and Coding interpreters might have different messages when attempting to swap out one code for another while attempting to use the framework of the previous model...

- That all said... I need to ensure I post the notable changes that are needed to swap in the different models...


## TODO:
- Always Seek Improvements
- Practice creating unit tests
- Source more data for resource folder

### Resources

- https://huggingface.co/openai-community/gpt2
- https://huggingface.co/openai-community/gpt2-medium
- https://huggingface.co/openai-community/gpt2-xl



