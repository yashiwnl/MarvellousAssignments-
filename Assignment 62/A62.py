import pandas as pd

from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

import matplotlib.pyplot as plt


def load_dataset():
    df = pd.read_csv("Employee_Attrition.csv")

    # Remove leading/trailing spaces from column names
    df.columns = df.columns.str.strip()

    print("Shape of dataset: ", df.shape)

    print("\nColumn Names: ")
    print(df.columns)

    print("\nFirst five records: ")
    print(df.head())

    print("\nMissing values")
    print(df.isnull().sum())

    print("\nDatatypes: ")
    print(df.dtypes)

    return df


def convert_dataset(df):

    # Remove leading/trailing spaces from categorical values
    df["OverTime"] = df["OverTime"].str.strip()
    df["Attrition"] = df["Attrition"].str.strip()

    overtime_encoder = LabelEncoder()
    attrition_encoder = LabelEncoder()

    df["OverTime"] = overtime_encoder.fit_transform(df["OverTime"])
    df["Attrition"] = attrition_encoder.fit_transform(df["Attrition"])

    print("\nAfter Encoding: ")
    print(df.head())

    print("\nOverTime classes: ")
    print(overtime_encoder.classes_)

    print("\nAttrition classes: ")
    print(attrition_encoder.classes_)

    return df, overtime_encoder, attrition_encoder


def split_dataset(df):

    x = df.drop("Attrition", axis=1)
    y = df["Attrition"]

    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        test_size=0.2,
        random_state=42
    )

    return x_train, x_test, y_train, y_test


def scale_features(x_train, x_test):

    scaler = StandardScaler()

    x_train = scaler.fit_transform(x_train)
    x_test = scaler.transform(x_test)

    return x_train, x_test, scaler


def train_model(xtrain, ytrain):

    model = MLPClassifier(
        hidden_layer_sizes=(100, 50),
        max_iter=490,
        random_state=42
    )

    model.fit(xtrain, ytrain)

    print("\nIterations Required: ", model.n_iter_)
    print("Model Loss: ", model.loss_)

    return model, model.n_iter_, model.loss_curve_


def check_accuracies(x_train, y_train, x_test, y_test, model):

    y_train_pred = model.predict(x_train)
    y_test_pred = model.predict(x_test)

    training_accuracy = accuracy_score(y_train, y_train_pred)
    testing_accuracy = accuracy_score(y_test, y_test_pred)

    print("\nTraining Accuracy: ", training_accuracy)
    print("Testing Accuracy: ", testing_accuracy)

    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_test_pred))


def plot_loss_curve(iterations, loss):

    plt.plot(range(1, iterations + 1), loss)

    plt.xlabel("Iterations")
    plt.ylabel("Loss")
    plt.title("MLP Training Loss Curve")

    plt.show()


def PredictAttrition(
    employee_data,
    model,
    scaler,
    overtime_encoder,
    attrition_encoder
):

    employee_data = employee_data.copy()

    employee_data["OverTime"] = overtime_encoder.transform(
        employee_data["OverTime"]
    )

    employee_data_scaled = scaler.transform(employee_data)

    prediction = model.predict(employee_data_scaled)

    prediction_labels = attrition_encoder.inverse_transform(prediction)

    print("\nPrediction on unseen data:")

    for i, result in enumerate(prediction_labels, start=1):
        print(f"Employee {i}: {result}")


def main():

    df = load_dataset()

    df, overtime_encoder, attrition_encoder = convert_dataset(df)

    x_train, x_test, y_train, y_test = split_dataset(df)

    x_train, x_test, scaler = scale_features(x_train, x_test)

    model, iterations, loss = train_model(
        x_train,
        y_train
    )

    check_accuracies(
        x_train,
        y_train,
        x_test,
        y_test,
        model
    )

    plot_loss_curve(
        iterations,
        loss
    )

    employee_data = pd.DataFrame({
        "Age": [24, 31, 42, 35, 27],
        "MonthlyIncome": [2800, 5200, 7800, 6100, 3500],
        "YearsAtCompany": [1, 6, 12, 8, 3],
        "TotalWorkingYears": [2, 9, 18, 12, 5],
        "DistanceFromHome": [18, 5, 25, 7, 20],
        "JobSatisfaction": [2, 4, 2, 3, 1],
        "WorkLifeBalance": [2, 3, 2, 4, 1],
        "OverTime": ["Yes", "No", "Yes", "No", "Yes"],
        "NumCompaniesWorked": [2, 1, 4, 2, 3],
        "TrainingTimesLastYear": [2, 3, 2, 4, 1]
    })


    PredictAttrition(
        employee_data,
        model,
        scaler,
        overtime_encoder,
        attrition_encoder
    )

    # The MLP model is suffering from overfitting. 
    # The training accuracy is 100%, while the testing accuracy is only 73.5%, 
    # The very low training loss of approximately 0.00765 also indicates that 
    # the model has learned the training data very closely. 
    # Since the model performs substantially better on training data than on test data, 
    # it is overfitting rather than underfitting.

if __name__ == "__main__":
    main()