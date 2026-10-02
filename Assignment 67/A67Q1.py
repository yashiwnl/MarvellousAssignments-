import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.neural_network import MLPClassifier

x = np.array([
    [25, 500, 12, 1, 2],
    [30, 700, 24, 0, 1],
    [45, 1200, 6, 5, 8],
    [50, 1500, 5, 6, 10],
    [28, 600, 18, 1, 1],
    [35, 800, 30, 0, 0],
    [48, 1400, 4, 7, 9],
    [52, 1600, 3, 8, 12],
    [27, 550, 20, 0, 1],
    [42, 1300, 8, 4, 7]
])

y = np.array([
    0, 0, 1, 1, 0,
    0, 1, 1, 0, 1
])

X_train, X_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)


# Feature scaling
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = MLPClassifier(
    hidden_layer_sizes= (10, 5),
    activation="relu",
    solver="adam",
    max_iter=1000,
    random_state=42
)

model.fit(X_train, y_train)


y_pred = model.predict(X_test)


accuracy = accuracy_score(y_test, y_pred)

print("Actual Values: ", y_test)
print("Predicted Values: ", y_pred)
print("Accuracy:", accuracy)


new_customer = np.array([[46, 1450, 5, 6, 9]])

new_customer_scaled = scaler.transform(new_customer)

prediction = model.predict(new_customer_scaled)


if prediction[0] == 1:
    print("Prediction: Customer may leave")
else:
    print("Prediction: Customer may stay")