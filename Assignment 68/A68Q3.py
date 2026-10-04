matrix = [
    [6, 4],
    [8, 6]
]

flatten_output = []

for row in matrix:
    for value in row:
        flatten_output.append(value)

print("Flattened Output:")
print(flatten_output)

weights = [0.1, 0.2, 0.3, 0.4]
bias = 1

weighted_sum = 0

for i in range(len(flatten_output)):
    weighted_sum += flatten_output[i] * weights[i]

weighted_sum += bias

print("\nFully Connected Layer Output:")
print(weighted_sum)

#Role of flattening in CNN: 
# Flattening converts the 2D feature maps produced by convolution and pooling 
# into a 1D vector that can be given to dense (fully connected) layers 
# for final prediction.