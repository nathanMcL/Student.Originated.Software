I created a Wiki for:
```
ProtoType 08, Prototype_text, GPT_final
```
https://github.com/nathanMcL/Student.Originated.Software/wiki/Ai-Selfhosting<br>

## 06/16/2024 The Swap...
- `gpt_train.py` currently uses gpt2 which is a smaller pretrained model, that I believe will not return a user query. The gpt2 model to me is more of a training model, so that an engineer can see how it works. That said, I think I want to try and swap out the code components that use the `gpt2` model for a larger Generative Pretrained Transformer, the `gpt2-xl`.<br>

 ### GPT-2 XL
 - The XL has a 1.5B parameters version of GPT-2, a transformer-based language model created and released by OpenAI. This model is pre-trained on the English language using a causal language modeling (CLM) objective.<br>

### Desirable outcomes...
- The program runs without being killed by the OS, due to resource consumption.
- Three trained models with CSV & pdf data.
- `GPT_gabba.py` returns a reasonable response to a query... This could be anything sentence that makes sense...<br>
- Bonus if it pertains to the user query.<br>




## TODO:
- Always Seek Improvements


### Resources

- https://huggingface.co/openai-community/gpt2
- https://huggingface.co/openai-community/gpt2-xl



