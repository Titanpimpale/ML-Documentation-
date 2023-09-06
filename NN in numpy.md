Today I learned the following topic:

Forward propagation<br>
AGI (artificial general intelligence)<br>
Training neural network with TensorFlow

1.<b> Forward propogation</b>
<pre>
def my_dense(a_in, W, b, g):

    units = W.shape[1]
    a_out = np.zeros(units)
    for j in range(units):               
        w = W[:,j]                                    
        z = np.dot(w, a_in) + b[j]         
        a_out[j] = g(z)               
    return(a_out)
  </pre>
<pre>
def my_sequential(x, W1, b1, W2, b2):
    a1 = my_dense(x,  W1, b1, sigmoid)
    a2 = my_dense(a1, W2, b2, sigmoid)
    return(a2)
    </pre>

<br> The above code is forward propagation where we don't write code for all a_in, W,b,g we make a matrix where we store all a_in, W, b, g <br>
when we input some values of i.e. a_in and initialize a_out with zero matrices and allow for loop to do the calculations of  z = np.dot(w, a_in) + b[j]  <br>
we input data and then run def my_sequential(x, W1, b1, W2, b2):
Thus  we forward propagate with simple Python and Numpy

<b>2. AGI (Artificial General Intelligence):</b><br>
   Basically, there are two types of AI
   1. ANI, which stands for Artificial Narrow Intelligence with ani we can build self-driving cars, smart speakers, web search recommendations etc.
   2. AGI, AI which can do everything that humans can.
   AGI is a crazy field that performs any intellectual task that a human being can. AGI is also known as strong AI, full AI, or general intelligent action.
   ![iStock-1178121288](https://github.com/Titanpimpale/ML-Documentation-/assets/109168200/2ecfd22a-ffc7-490d-8e23-598b6b53078f)

<b>3. Training Neural Network in TensorFlow</b>

   ![Screenshot 2023-09-06 105858](https://github.com/Titanpimpale/ML-Documentation-/assets/109168200/2f164eae-aefd-48b0-8b37-a5b06898c4a9)

<be><pre> Part 1: specify the model
          Part 2. Compile the model 
          Part 3. Train the model</pre>

   
