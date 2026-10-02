import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def relu(x):
    return np.maximum(0, x)

def tanh(x):
    return np.tanh(x)


sigmoid_output = sigmoid(x)
relu_output = relu(x)
tanh_output = tanh(x)

plt.figure(figsize=(10, 6))

plt.plot(x, sigmoid_output, label="Sigmoid")
plt.plot(x, relu_output, label="ReLU")
plt.plot(x, tanh_output, label="Tanh")

plt.xlabel("Input")
plt.ylabel("Output")
plt.title("Activation Functions")
plt.legend()
plt.grid(True)

plt.show()

# Explanation
# Sigmoid: Converts values into a range between 0 and 1. 
#          Commonly used in the output layer for binary classification.

# ReLU: Returns 0 for negative values and the input itself for positive values. 
#       It is commonly used in hidden layers of neural networks.

# Tanh: Converts values into a range between -1 and 1. 
#       It is useful when both positive and negative outputs are needed.