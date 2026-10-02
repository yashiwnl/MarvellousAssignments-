x = 2
weight = 0.5
bias = 0.5
target = 1
learning_rate = 0.1

prediction = (x * weight) + bias

error = target - prediction

gradient = error * x

old_weight = weight

weight = weight + (learning_rate * gradient)

print("Input:", x)
print("Old Weight:", old_weight)
print("Prediction:", prediction)
print("Target:", target)
print("Error:", error)
print("Updated Weight:", weight)