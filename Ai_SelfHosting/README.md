```
ProtoType 08
```


## What is Ai Self-Hosting?

AI self-hosting refers to the capability to run AI models on your own infrastructure rather than relying on cloud-based services.<br>
This can involve setting up the necessary hardware and software to train and run AI models locally.<br>
The process is autonomous to an extent but is heavily guided by the initial programming and ongoing training provided by human operators.

When I think about AI, particularly in the context of generating responses to user queries, we're often discussing models trained on large datasets that learn to predict the most likely response based on the input they receive. These AI models, like GPT (Generative Pretrained Transformer), use statistical probabilities to generate responses that are coherent and contextually relevant to the queries they receive.<br>

## 4/16/2024
added prototype-00. ' -00 ' is a current build from Ai-selfhosting course. 
I ran both prototypes within gitpod. Once I executed the first prototype the training files then unzip within the directory. which I thought was fine, I had created a .gitignore file.<br>
I was unable to commit and push my changes after I ran the prototypes.<br>
I had to exit out, get back into gitpod and redo my changes, then commit and push. <br>

Next time commit and push changes before running.<br>

You'll need to download the training images, labels, test images and labels, from Yann LeCun's website.

https://yann.lecun.com/exdb/mnist/ by using the following command:

```
curl http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz -o train-images-idx3-ubyte.gz &&
curl http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz -o train-labels-idx1-ubyte.gz &&
curl http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz -o t10k-images-idx3-ubyte.gz &&
curl http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz -o t10k-labels-idx1-ubyte.gz
```
After the .gitignore file is created, run the .gz unzip command:
```
gunzip *.gz
```

## Installed libraries
```
pip3 install Pillow  && pip3 install numpy
```
## 04/18/2024
FYI: I have to install the dependencies each time I log back into gitpod to work on the code.




## todo:

 Traceback (most recent call last):<br>
  File "/workspace/Student.Originated.Software/Ai_SelfHosting/prototype-08/load_mnist.py", line<br> 154, in <module> <br>
    nn.SGD( <br>
  File "/workspace/Student.Originated.Software/Ai_SelfHosting/prototype-08/network.py", line 41,<br> in SGD <br>
    self.update_mini_batch(mini_batch, eta) <br>
  File "/workspace/Student.Originated.Software/Ai_SelfHosting/prototype-08/network.py", line 53,<br> in update_mini_batch <br>
    delta_nabla_b, delta_nabla_w = self.backprop(x, y) <br>
                                   ^^^^^^^^^^^^^^^^^^^ <br>
  File "/workspace/Student.Originated.Software/Ai_SelfHosting/prototype-08/network.py", line 71,<br> in backprop<br>
    activation = sigmoid(z) <br>
                 ^^^^^^^ <br>
NameError: name 'sigmoid' is not defined. Did you mean: 'self.sigmoid'? <br>






## How to run our demo
Example of how you can run the program once you have navigated to the directory.
```
python3 prototype-00
```




## How we built it






## Challenges we ran into






## Accomplishments we are proud of







## What we learned







## What is next for the project




