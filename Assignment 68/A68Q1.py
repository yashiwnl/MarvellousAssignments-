image = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

kernel = [
    [-1, -1, -1],
    [0,  0,  0],
    [1,  1,  1]
]

image_rows = len(image)
image_cols = len(image[0])

kernel_size = len(kernel)

feature_map = []

for i in range(image_rows - kernel_size + 1):
    row = []

    for j in range(image_cols - kernel_size + 1):

        total = 0

        for ki in range(kernel_size):
            for kj in range(kernel_size):
                total += image[i + ki][j + kj] * kernel[ki][kj]

        row.append(total)

    feature_map.append(row)


print("Feature Map: ")

for row in feature_map:
    print(row)
