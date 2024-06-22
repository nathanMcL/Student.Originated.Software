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

- This GPT-xl, computationally is very large, and then once the program runs, the amount of hardware resources that are being utilized is alot, ahhhh...lot.<br>

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
- I should attempt to test the `GPT-medium`, the minimum system requirements are more feasible for conducting training of that vesion. <br>

```
GPT-2 Medium (345M parameters)
GPU: NVIDIA GPU with at least 12-16 GB of VRAM (e.g., RTX 2080 Ti, RTX 3080).
RAM: 32 GB of system RAMStorage.
SSD with at least 100 GB of free spaceCPU. Modern multi-core CPU (e.g., Intel i7 or AMD Ryzen 7)
CUDA and cuDNN: Installed and compatible with the GPU and PyTorch version
```
## 06/22/2024 Happy Compromises...
 - So, as I mentioned previously, the GPT2-XL requires a machine that can run the much larger GPT2-XL version. I did still gut `gpt_train.py` and implement the needed code for the GPT_XL to run, named 'GPT2_xl'. <br>

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
- The `Name` is of the Device. TODO: currently the name is not the correct device name, investigate...
- The `Date & Time` is logged for each event entry.
- The `Available RAM (GB)` is a snapshot of its state during the logging process.
- The `Available Memory (%)` is a snapshot of the current memory percentage.
- The `GPU Name` is logged for identification.
- The `GPU Memory (MB)` is a snapshot of the GPU's Memory.
- The `Temperature` is logged to track the device's physical health

GPTSystemLogging.py will log the before metric, during metrics, but for the Event `After` Training, the script computes the average Available RAM (GB), the average Available Memory (%), The average GPU Memory, and average Temperature.<br>

- I hope.lol, the program has not completed running as I type this. :)


## TODO:
- Always Seek Improvements


### Resources

- https://huggingface.co/openai-community/gpt2
- https://huggingface.co/openai-community/gpt2-xl



