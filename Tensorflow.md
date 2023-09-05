Today I studied the following topics:
1. Neural network model
2. TensorFlow implementation
3. Basic Computer Vision with ML

1. Neural network model

![Screenshot 2023-09-05 124116](https://github.com/Titanpimpale/ML-Documentation-/assets/109168200/ccb63210-a898-42d7-8030-7ed23cbbcac5)<br>
above image represent NN notation<pre> where a is activation value
                                            g is the activation function 
                                            w and b are parameters of layer l  
Note: Activation means deciding whether a neuron should be activated or not

2. Tensorflow:
   how data is stored in a tensor?
   Tensor is the way to represent matrix, in TensorFlow data is stored in a tensor (i.e. matrix)
   example: data = np.array([100,17]) #1-D array<br>
<strong>Build model using tensorflow</strong>

TensorFlow is a machine learning library, TensorFlow helps us in instead of putting data into layer<br>to another layer we tell Tensorflow to do it 

example model = sequiential[layer1, layer2]
![Screenshot 2023-09-05 093722](https://github.com/Titanpimpale/ML-Documentation-/assets/109168200/5055bb7b-3139-4a71-aced-83ba8b2a1dcb)

3. Basic Computer Vision with ML(using TensorFlow)

![Screenshot 2023-09-05 125525](https://github.com/Titanpimpale/ML-Documentation-/assets/109168200/72f95a0e-bf57-454e-a7da-172d760a6e9c)
<em>output:</em>
![Screenshot 2023-09-05 125557](https://github.com/Titanpimpale/ML-Documentation-/assets/109168200/48ba55ab-d11e-410a-82fe-642c390c9d07)

Following are the thumb rules of TensorFlow :
1. Increasing neuron: takes longer time but gives accurate prediction (not work all the time)
2. Flatten ():  We add the Flatten() layer at the beginning, and when the arrays are loaded into the model later, they'll automatically be flattened for us.
3. why the final layer is 10 layers only: The number of neurons in the last layer is the same of number of classes you classify here 0-9 so 10 layer
4. Extra layers are necessary

   Hope you like my documentation, Thank you!!!  


