I created a Wiki for:
```
ProtoType 08, Prototype_text, GPT_final
```
https://github.com/nathanMcL/Student.Originated.Software/wiki/Ai-Selfhosting<br>

## 06/16/2024 The Swap...
- `gpt_train.py`, `previous_chapters.py` & `GPT_gabba.py` currently uses gpt2 which is a smaller pretrained model, that I believe will not return a user query with a response to the question asked(see `chat_log.csv`). The gpt2 model to me is more of a training model, so that an engineer can see how things work. For instance, to self-host `GPT 4o` That would require so much more computational power than my 64gb 4060GPU. That said, I think I want to try and swap out the code components that use the `gpt2` model for a larger Generative Pretrained Transformer, the `gpt2-xl`.<br>
- I tested the gpt2-xl on huggingface, with my test phase from `gpt_train.py`. I did not receive a direct response to my question.
- Collecting the data and seeing the difference in small versus a larger model.<br>

 ### GPT-2 XL
 - The XL has a 1.5B parameters version of GPT-2, a transformer-based language model created and released by OpenAI. This model is pre-trained on the English language using a causal language modeling (CLM) objective.<br>

### Desirable outcomes...
- The program runs without being killed by the OS, due to resource consumption.
- Three trained models with CSV & pdf data.
- `GPT_gabba.py` returns a reasonable response to a query... This could be anything, a sentence that makes sense...<br>
- Bonus if it pertains to the user query.<br>

## 06/20/2024 fun, while it lasted...
So, I shot for the stars again.<br>

- This GPT2-xl, computationally is very large, and then once the program runs, the amount of hardware resources that are being utilized is alot, ahhhh...lot.<br>

- After altering locally, `gpt_train.py`, so it uses the `GPT2-xl` version from Huggingface<br> (see `GPT2_xl` within the Project_LLM directory).

- The following are ruff, minimum harware considertions for a `GPT2-xl` transformer:
  ```
  GPT-2 XL (1.5B parameters)
  GPU: NVIDIA GPU with at least 24 GB of VRAM (e.g., RTX 3090, Titan RTX).
  RAM: 128 GB of system RAMStorage.
  SSD with at least 300 GB of free spaceCPU.
  High-end multi-core CPU (e.g., Intel i9 or AMD Ryzen 9 Threadripper).
  CUDA and cuDNN: Installed and compatible with the GPU and PyTorch version
  ```
- I need to scale back the size of the model I want to try and swap out.
- I should attempt to test the `GPT2-medium`, the minimum system requirements are more feasible for conducting training of that vesion. <br>

```
GPT-2 Medium (345M parameters)
GPU: NVIDIA GPU with at least 12-16 GB of VRAM (e.g., RTX 2080 Ti, RTX 3080).
RAM: 32 GB of system RAMStorage.
SSD with at least 100 GB of free spaceCPU. Modern multi-core CPU (e.g., Intel i7 or AMD Ryzen 7)
CUDA and cuDNN: Installed and compatible with the GPU and PyTorch version
```
## 06/22/2024 Happy Compromises...
 - So, as I mentioned previously, the GPT2-XL requires a machine that can run the much larger GPT2-XL version. I did still gut `gpt_train.py` and implement the needed code for the GPT2_XL to run, named 'GPT2_xl'. <br>

- I created a new directory, named: `GPT_small` \ `GPT_final_small` that I copied over the necessary files from `GPT_final_two` directory.<br>

- `GPT_small` is my current working AI trainer. The purpose is to have a working copy that I can continue to modify, tweak, finetune, and test.<br>

- Testing out different configurations, and collecting the data from the data logging scripts on a small Transformer would allow me to also implement the same techniques on a larger Transformer model.<br>

### GPT_small

- While typing code, attempting to run the program, collecting data, implementing new functions, and tweaking the original code further... I started to observe my CPU Task Manager Performance metrics, and I started thinking about how my CPU is handling this small GPT.<br>
-- Does the memory usage fluctuate while the GPT trains?<br>
-- When there is a `Validation loss`(like when it starts to rise) and `Training loss`(Those positive spikes along the downward gradient curve) is there a drop in any of the system performance metrics?<br>

I had the idea to create another Python script. This GPTSystemLogging.py script is meant to log additional metrics about the Operating System `Before`, `During` & `After` training. Previously while attempting to train the GPT2 on my Windows Surface Book2 I noticed how much of the computing resources were being used. The temperature was hot! And the same goes for my Windows Studio. I want to see how the hardware resources are being used by logging an `Event`:<br>

- `Before`, the train starts a snapshot is taken.
- `During`, while the program is running, at set intervals. A snapshot is taken.
- `After`, once the last epoch has been completed and logged. A snapshot is taken
  
### GPTSystemLogging.py
- Creates a CSV file with these headers:<br>

- The Event, Name, Date & Time, Available RAM (GB), Available Memory %, The GPU name, GPU Memory (MB), and Temperature in Celsius and Fahrenheit (C / F).
- The `Event` will tell what type of training event it was (`Before`, `During` & `After`).
- The `Name` is of the Device. 
- The `Date & Time` is logged for each event entry.
- The `Available RAM (GB)` is a snapshot of its state during the logging process.
- The `Available Memory (%)` is a snapshot of the current memory percentage.
- The `GPU Name` is logged for identification.
- The `GPU Memory (MB)` is a snapshot of the GPU's Memory.
- The `Temperature` is logged to track the device's physical health

GPTSystemLogging.py will log the before metric, during metrics, but for the Event `After` Training, the script computes the average usage before and after, Available RAM (GB), the average Available Memory (%), The average GPU Memory, and average Temperature.<br>

- I hope.lol, the program has not completed running as I type this. :)
![Screenshot (3)](https://github.com/nathanMcL/Student.Originated.Software/assets/129904249/c81ecaa9-12af-4ba7-a50c-60863946f1ec)

### 0855 Feed the Machine!
- After searching things up, I learned that not having a large diverse enough data set could have a factor in the `Validation Loss`'s overfitting that leads to over `Generalization`.
- This has a factor in why there is a rise in the `Validation Loss`.
- So...add more data...
- I did source the U.S. Army: Food Service, Nutrition, & First-Aid manuals to add to my dataset...But I need more...

### Before additional resources were added
config:
- accumulation_steps=4
- num_workers=4+4+4 (Four works at each location)
```
GPT_CONFIG_124M = {
        "vocab_size": 50257,    # Vocabulary size
        "context_length": 256,  # Shortened context length (orig: 1024)
        "emb_dim": 768,         # Embedding dimension. Orignial value was: 768.
        "n_heads": 12,          # Number of attention heads. Orignial value was: 12 
        "n_layers": 12,         # Number of layers. Orignial value was: 12
        "drop_rate": 0.1,       # Dropout rate. Original value was: 0.1
        "qkv_bias": False       # Query-Key-Value bias
    }

    OTHER_SETTINGS = {
        "learning_rate": 4e-4,  # Original value was: 5e-4,
        "num_epochs": 20,       # Increase number of epochs from 10 to 20
        "batch_size": 4,        # Increase the batch size or Decrease. Original value was: 2
        "weight_decay": 0.1     # Original value was: 0.1
    }
```
![Screenshot (4)](https://github.com/nathanMcL/Student.Originated.Software/assets/129904249/9cc91a49-b086-46b3-8d96-05eaf7509612)

### After adding additional resources
![Screenshot (5)](https://github.com/nathanMcL/Student.Originated.Software/assets/129904249/943b4880-1fce-4b9d-9262-654753354a89)

## 06/23/2024 Python Library errors 😔

So... ... How do I explain the problem...
- When creating the `GPTSystemLogging.py` to log the operating system metrics: `Before`, `During`, & `After`.<br>
I had to install / import `GPUtil`, But...<br>
Today I received an error message when I attempted to run the program. I had not received any previous traceback messages regarding any issue with logging the GPU data.<br>

`ValueError: invalid literal for int() with base 10: Failed to initialize NVML: N/A`<br>
What I think this means, is that the library that handles or logs my GPU Nvidia data, now has some issue preventing it from being used to log my GPU data as it had previously.<br>
- So far, I created an `Exception` for the `get_system_stats` method that will log " N/A " if the `import GPUtil` is not functioning as it should.

```
def get_system_stats(self):
        mem = psutil.virtual_memory()
        try:
            gpus = GPUtil.getGPUs()
            gpu_info = gpus[0] if gpus else None
            gpu_name = gpu_info.name if gpu_info else "N/A"
            gpu_memory = gpu_info.memoryFree if gpu_info else "N/A"
            gpu_temp_c = gpu_info.temperature if gpu_info else "N/A"
            gpu_temp_f = (gpu_temp_c * 9/5) + 32 if gpu_temp_c != "N/A" else "N/A"
            if gpu_temp_c != "N/A":
                self.temperature_celsius.append(gpu_temp_c)
        except Exception as e:
            gpu_name = "N/A"
            gpu_memory = "N/A"
            gpu_temp_c = "N/A"
            gpu_temp_f = "N/A"
```
  

- The `GPTSystemLogging.py` script has previously logged the GPU data, so I am not sure what happened at the moment.
![Screenshot (6)](https://github.com/nathanMcL/Student.Originated.Software/assets/129904249/f3272439-393b-4cae-a8af-19a43c5c92f1)

### 06/24/2024 Troubleshoot powpow
- Did a `sudo apt update && sudo apt upgrade`, hoping it would resolve the issue of not logging the GPU data.
- installed the `cuda toolkit` library
- try uninstalling the dependancies and re-install(I don't like this option).
- read on-line, that `GPTil` may need to be using WSL2 kernal...
> I downloaded WSL2 files, set the WSL2 to be used though the admin-terminal.<br>
> I hve not proceeded, the instructions on how to switch from using WSL to WSL2 are challenging to sort out ATM.<br>

## 06/26/2024 Eight Batches!

- Still investigating the issue of not being able to log the GPU data.

### Learning to fine-tune

config:<br>
> - `accumulation_steps=4`<br>
> - `num_workers`=4+4+4 (Four workers at each location)<br>

```
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
        "num_epochs": 25,       # Increase number of epochs from 10 to 20
        "batch_size": 8,        # Increase the batch size or Decrease. Original value was: 2
        "weight_decay": 0.05     # Original value was: 0.1
    }
```
gpt training loss<br>
![Screenshot (7)](https://github.com/nathanMcL/Student.Originated.Software/assets/129904249/cacd77a8-0231-4371-8bb6-24840ff49676)
GPT OS system log<br> 
![Screenshot (8)](https://github.com/nathanMcL/Student.Originated.Software/assets/129904249/2bccc4fd-a5b7-4bae-8281-02a7e93b92c8)

### 8-batches...
- The choice of using 8-batches during training appears to be a critical factor influencing the generalization capabilities of the small GPT-2 model.<br>
- When training with this setting, the validation loss is noticeably reduced, indicating that the model is better at predicting unseen data. This reduction in validation loss demonstrates improved generalization, which means the model is not just memorizing the training data but is also learning patterns that apply to new data.<br>
- Training with 8-batches helps achieve lower overall loss, making the model more effective and reliable.<br>

## 06/28/2024 WorkStations
- An example of top-shelf Workstations for AI/ML training...
  ![Screenshot (11)](https://github.com/nathanMcL/Student.Originated.Software/assets/129904249/41fea69b-3239-4df0-8999-8963b2c06f2a)


## TODO:
- Always Seek Improvements
- Practice creating unit tests

### Resources

- https://huggingface.co/openai-community/gpt2
- https://huggingface.co/openai-community/gpt2-xl



