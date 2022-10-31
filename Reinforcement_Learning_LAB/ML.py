import random
import numpy as np
import time
class Model:
    def __init__(self, input_size, output_size, lr):
        self.weights = np.array([
            [round(random.random()*2-1,2) for _ in range(output_size)]
            for _ in range(input_size)
        ])
        self.input_size = input_size
	self.lr = lr
	print("Weight Created of shape :",self.weights.shape)
    def apply(self, input_matrix):
	print("\n-------------Begin apply method -----------\n")
	print("Input matrix shape : ",input_matrix.shape)
        a = input_matrix
        b = self.weights
        activation = a*b
	print("Activation Function : ",activation.shape)
        o = np.array([[1 if a > 0 else 0 for a in l] for l in activation])
        return o
    def add_layer(self,number_of_neurons):
        self.weights.append(np.array([[random.random()*2-1 for _ in range(number_of_neurons)] for _ in range(self.hidden_layer_sizes[-1])]))
    def adjust(self, o, t, x):
        self.weights = self.weights + x*np.transpose(t - o)*self.lr

def example():
    m = Model(input_size = 4, output_size= 3, lr=0.3)
    x_input=np.array([
        [1,0,0],
        [1,0,1],
        [1,0,1],
        [0,1,0]
    ])
    t=np.array([
        [1,0,0],
        [1,0,1],
        [1,0,1],
    ])
    iter = 0
    while (True):
        o = m.apply(x_input)
        m.adjust(o, t, x_input)
	break
        iter+=1
        print(m.weights)
        time.sleep(2)
        print("T:O\n",t,o)
        if (np.array_equal(t,o)):
            print("iter", iter)
            print(m.weights)
            break
example()
