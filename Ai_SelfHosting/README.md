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
pip3 install Pillow  && pip3 install numpy && pip3 install pbjson
```
## 04/18/2024
FYI: I have to install the dependencies each time I log back into gitpod to work on the code.

## 04/19/2024
I was able to create the trainer on my local machine. It will run for a while to see what happens. <br>

## 04/22/2024
I have been able to save the epochs up to 50
```
Epoch 40: 1030 / 10000
Epoch 41: 1015 / 10000
Epoch 42: 1032 / 10000
Epoch 43: 1129 / 10000
Epoch 44: 1063 / 10000
Epoch 45: 1088 / 10000
Epoch 46: 1039 / 10000
Epoch 47: 1044 / 10000
Epoch 48: 1055 / 10000
Epoch 49: 1050 / 10000
```
It is good that I can reach Epoch 50. However, the percentage or accuracy of the images recognized  1050 / of the 10k training images used per Epoch should increase as it trains.

## 04/25/2024
created a ```dropout``` function.<br>
...But what is a ```dropout``` function?<br>
```
def dropout(self, x, level):
        if level < 0. or level >= 1:  # Level is the dropout probability
            raise ValueError('Dropout level must be in interval [0, 1).')
        retain_prob = 1. - level
        # We scale the activations at training time to keep the same expected sum of activations.
        sample = np.random.binomial(n=1, p=retain_prob, size=x.shape)
        x *= sample
        x /= retain_prob
        return x
```
In the context of this MNIST trainer, the ```dropout``` function manages the network's learning process by randomly deactivating a subset of neurons durning the traing phase.<br>
This is meant to prevent ```overfitting```. This ```overfitting``` can occur when a neural network model learns the training data too well and can perform poorly on new unseen data. <br>

But, how does the ```dropout``` function work?<br>
## 1. Probability Setting:<br> 
The dropout function accepts an input x (the activations from the previous layer) and a level, which represents the dropout rate. The dropout rate is the probability that each neuron’s output is set to zero. This rate must be between 0 and 1, where 0 means no dropout and 1 means complete dropout.<br>
## 2. Activation Retention: <br>
The function calculates the retain_prob as 1 - level, which is the probability of retaining a neuron's activation. For example, if the dropout level is 0.5, there’s a 50% chance that any given neuron will be retained (meaning, not dropped).<br>
## 3. Sampling:<br>
It uses a binomial distribution to randomly decide which neurons to keep (sample = np.random.binomial(n=1, p=retain_prob, size=x.shape)). In this sampling process, each neuron has an independent probability retain_prob of being retained.<br>
## 4. Application of Dropout:<br>
The function then applies this mask to the activations (x *= sample). This step sets the activation of dropped neurons to 0.<br>
## 5. Scaling:<br> 
Since on average a proportion retain_prob of the inputs are retained, this could lead to a lower total input to the next layer. To compensate for this reduction in input, the activations are scaled up by dividing by retain_prob (x /= retain_prob). This scaling is needed because it maintains the expected sum of the activations consistent whether dropout is applied or not, in theory, it should... stabilize the learning process.<br>

### Why implement this ```dropout``` function?
Implementing the dropout function helps by the training of mulitple neural networks with different architectures. The function does this by  randomly dropping different sets of neurons. This is repersents sampling from an ensemble of neural networks, which improves the gerneralization of the model.<br>
So... while the program is "training", ```dropout``` is not applied, the neurons are not dropped, and the full capabilities of the trained network are utilized. This helps the network make the most accurate predictions possible with the learned weight and biases.<br> 

## Evaluate Training Accuracy:<br>
I wanted to create an instance once the program is finished "training", that the ```Training Accuracy``` is printed. The Idea is to later, create a CSV log report of the training accuracy amoung other collectable data...<br> 
But for now... ```print```<br>
### Date & Time <br>
04/25/24 0935 <br>
```
   Training Accuracy: 70.29833333333333%
   Training Accuracy: 85.53%
```


```
def evaluate_accuracy(self, data):
        """Evaluate the network's accuracy on the provided data."""
        results = [(np.argmax(self.feedforward(x)), np.argmax(y)) for (x, y) in data]
        accuracy = sum(int(x == y) for (x, y) in results) / len(data) * 100  # I want to calculate the  accuracy as a percentage
        return accuracy
```
What the ```evaluate_accuracy``` function does is calculate how many total training labels are recognized out of the total training imaged used as a percentage.<br>


## 04/26/2024
### Log the Training Results

This function's purpose is to create a CSV file that logs training data once the program is complete.<br>
The ```log_training_results``` create a CSV file with the following headers: <br>
```
Date and Time, Total Epochs, Images per Epoch, and Training Accuracy
```
(sample csv)<br>
```
Date and Time,Total Epochs,Images per Epoch,Training Accuracy
2024-04-26 05:02:08,50,60000,53.059999999999995
```



## todo:

```
Figure out how to improve the algorithm to:
 increase its recognition,
 increase wall-clock speed,

```




## How to run our demo
Example of how you can run the program once you have navigated to the directory.
```python3 prototype-00```
```python3 train.py```



## How we built it






## Challenges we ran into






## Accomplishments we are proud of







## What we learned







## What is next for the project




