import math

actual_regression = [3,5,7,9]
predicted_regression = [2.5, 5.5, 6.5, 8.5]

def mean_squared_error(actual, predicted):
    total_error = 0

    for a, p in zip(actual, predicted):
        total_error += (a - p) ** 2

    return total_error / len(actual)


mse = mean_squared_error(actual_regression, predicted_regression)
print("Mean Squared Error:", mse)

actual_classification = [1, 0, 1, 1]
predicted_classification = [0.9, 0.2, 0.8, 0.7]

def binary_crossentropy(actual, predicted):
    total_loss = 0

    for a, p in zip(actual, predicted):
        loss = -(a * math.log(p) + (1 - a) * math.log(1 - p))
        total_loss += loss

    return total_loss / len(actual)


bce = binary_crossentropy(
    actual_classification,
    predicted_classification
)

print("Binary Cross Entropy:", bce)