feature_map = [
    [3, 3, 3],
    [0, 0, 0],
    [-3, -3, -3]
]

relu_output = []

for row in feature_map:
    new_row = []

    for value in row:
        if value < 0:
            new_row.append(0)
        else:
            new_row.append(value)

    relu_output.append(new_row)

print("ReLU Output:")

for row in relu_output:
    print(row)


pool_size = 2
pool_output = []

for i in range(0, len(relu_output[0]) - 1, pool_size):

    row = []

    for j in range(0, len(relu_output[0]) - 1, pool_size):

        values = [
            relu_output[i][j],
            relu_output[i][j + 1],
            relu_output[i + 1][j],
            relu_output[i + 1][j + 1]
        ]

        row.append(max(values))

    pool_output.append(row)

print("\nMax Pooling Output:")

for row in pool_output:
    print(row)