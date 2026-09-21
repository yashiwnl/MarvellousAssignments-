import pandas as pd
import matplotlib.pyplot as plt

from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    precision_score,
    recall_score,
    f1_score
)


# ---------------------------------------------------------
# 1. Load and understand dataset
# 2. Exploratory analysis
# 3. Missing values
# ---------------------------------------------------------

def load_dataset():

    df = pd.read_csv("Loan_Default.csv")

    # Clean column names
    df.columns = df.columns.str.strip()

    # Clean categorical values
    df["PreviousDefault"] = df["PreviousDefault"].str.strip()
    df["HomeOwnership"] = df["HomeOwnership"].str.strip()

    print("Shape of dataset:", df.shape)

    print("\nColumn Names:")
    print(df.columns.tolist())

    print("\nFirst five records:")
    print(df.head())

    print("\nDatatypes:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nStatistical Summary:")
    print(df.describe())

    return df


# ---------------------------------------------------------
# 4. Check whether target classes are balanced
# ---------------------------------------------------------

def check_class_balance(df):

    print("\nDefault Class Distribution:")
    print(df["Default"].value_counts())

    print("\nDefault Class Percentage:")
    print(df["Default"].value_counts(normalize=True) * 100)

    print("\nClass Balance:")
    if df["Default"].value_counts(normalize=True).min() < 0.4:
        print("Classes are imbalanced.")
    else:
        print("Classes are reasonably balanced.")


# ---------------------------------------------------------
# 5. Encode categorical variables
# ---------------------------------------------------------

def convert_dataset(df):

    previous_default_encoder = LabelEncoder()

    # Encode PreviousDefault
    df["PreviousDefault"] = previous_default_encoder.fit_transform(
        df["PreviousDefault"]
    )

    # One-hot encode HomeOwnership
    df = pd.get_dummies(
        df,
        columns=["HomeOwnership"],
        dtype=int
    )

    print("\nAfter Encoding:")
    print(df.head())

    print("\nPreviousDefault Classes:")
    print(previous_default_encoder.classes_)

    print("\nColumns after One-Hot Encoding:")
    print(df.columns.tolist())

    return df, previous_default_encoder


# ---------------------------------------------------------
# 6. Separate X and y
# ---------------------------------------------------------

def split_features_target(df):

    X = df.drop("Default", axis=1)
    y = df["Default"]

    print("\nFeatures:")
    print(X.columns.tolist())

    print("\nTarget:")
    print("Default")

    return X, y


# ---------------------------------------------------------
# 7 & 8. Train/test split
# ---------------------------------------------------------

def split_dataset(X, y):

    # Stratification is used because Default classes are imbalanced
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    print("\nTraining Data Shape:", X_train.shape)
    print("Testing Data Shape:", X_test.shape)

    print("\nTraining Class Distribution:")
    print(y_train.value_counts(normalize=True))

    print("\nTesting Class Distribution:")
    print(y_test.value_counts(normalize=True))

    return X_train, X_test, y_train, y_test


# ---------------------------------------------------------
# 9. Scale features
# ---------------------------------------------------------

def scale_features(X_train, X_test):

    scaler = StandardScaler()

    X_train = scaler.fit_transform(X_train)

    # Only transform test data
    X_test = scaler.transform(X_test)

    return X_train, X_test, scaler


# ---------------------------------------------------------
# 10 & 11. Create and train MLP
# ---------------------------------------------------------

def train_model(X_train, y_train, activation="relu",
                hidden_layers=(32, 16),
                learning_rate_init=0.001):

    model = MLPClassifier(
        hidden_layer_sizes=hidden_layers,
        activation=activation,
        solver="adam",
        learning_rate_init=learning_rate_init,
        max_iter=1000,
        random_state=42
    )

    model.fit(X_train, y_train)

    print("\nIterations Required:", model.n_iter_)
    print("Final Training Loss:", model.loss_)

    return model


# ---------------------------------------------------------
# 12. Accuracy
# 13. Confusion Matrix
# 14. Classification Report
# 15. Precision, Recall, F1
# ---------------------------------------------------------

def evaluate_model(model, X_train, y_train, X_test, y_test):

    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)

    training_accuracy = accuracy_score(
        y_train,
        y_train_pred
    )

    testing_accuracy = accuracy_score(
        y_test,
        y_test_pred
    )

    print("\nTraining Accuracy:", training_accuracy)
    print("Testing Accuracy:", testing_accuracy)

    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_test_pred))

    print("\nClassification Report:")
    print(classification_report(y_test, y_test_pred))

    precision = precision_score(
        y_test,
        y_test_pred,
        zero_division=0
    )

    recall = recall_score(
        y_test,
        y_test_pred,
        zero_division=0
    )

    f1 = f1_score(
        y_test,
        y_test_pred,
        zero_division=0
    )

    print("\nPrecision:", precision)
    print("Recall:", recall)
    print("F1-Score:", f1)

    return training_accuracy, testing_accuracy


# ---------------------------------------------------------
# 16. Plot training loss
# ---------------------------------------------------------

def plot_training_loss(model):

    plt.plot(
        range(1, len(model.loss_curve_) + 1),
        model.loss_curve_
    )

    plt.xlabel("Iterations")
    plt.ylabel("Training Loss")
    plt.title("MLP Training Loss")

    plt.show()


# ---------------------------------------------------------
# 17. Test model on new loan applicants
# ---------------------------------------------------------

def predict_loan_applicants(
        applicant_data,
        model,
        scaler,
        previous_default_encoder,
        training_columns):

    applicant_data = applicant_data.copy()

    # Encode PreviousDefault using existing encoder
    applicant_data["PreviousDefault"] = (
        previous_default_encoder.transform(
            applicant_data["PreviousDefault"]
        )
    )

    # One-hot encode HomeOwnership
    applicant_data = pd.get_dummies(
        applicant_data,
        columns=["HomeOwnership"],
        dtype=int
    )

    # Make sure all training columns exist
    for column in training_columns:

        if column not in applicant_data.columns:
            applicant_data[column] = 0

    # Remove any unexpected columns
    applicant_data = applicant_data[training_columns]

    # Scale using existing scaler
    applicant_scaled = scaler.transform(applicant_data)

    prediction = model.predict(applicant_scaled)

    print("\nLoan Applicant Predictions:")

    for i, result in enumerate(prediction, start=1):

        if result == 1:
            print(f"Applicant {i}: Default")
        else:
            print(f"Applicant {i}: No Default")


# ---------------------------------------------------------
# Hyperparameter Experiment
# ---------------------------------------------------------

def hyperparameter_experiments(X_train, y_train, X_test, y_test):

    print("\n\n========== HYPERPARAMETER EXPERIMENTS ==========")

    # -----------------------------------------------------
    # Experiment 1 - Activation
    # -----------------------------------------------------

    activations = [
        "identity",
        "logistic",
        "tanh",
        "relu"
    ]

    print("\n========== Experiment 1: Activation ==========")

    for activation in activations:

        model = MLPClassifier(
            hidden_layer_sizes=(32, 16),
            activation=activation,
            solver="adam",
            max_iter=1000,
            random_state=42
        )

        model.fit(X_train, y_train)

        prediction = model.predict(X_test)

        accuracy = accuracy_score(
            y_test,
            prediction
        )

        print(
            f"{activation}: "
            f"Accuracy = {accuracy:.4f}, "
            f"Iterations = {model.n_iter_}"
        )


    # -----------------------------------------------------
    # Experiment 2 - Hidden Layers
    # -----------------------------------------------------

    hidden_layers = [
        (10,),
        (20, 10),
        (50, 25),
        (100, 50, 25)
    ]

    print("\n========== Experiment 2: Hidden Layers ==========")

    for layers in hidden_layers:

        model = MLPClassifier(
            hidden_layer_sizes=layers,
            activation="relu",
            solver="adam",
            max_iter=1000,
            random_state=42
        )

        model.fit(X_train, y_train)

        prediction = model.predict(X_test)

        accuracy = accuracy_score(
            y_test,
            prediction
        )

        print(
            f"{layers}: "
            f"Accuracy = {accuracy:.4f}, "
            f"Iterations = {model.n_iter_}"
        )


    # -----------------------------------------------------
    # Experiment 3 - Learning Rate
    # -----------------------------------------------------

    learning_rates = [
        0.0001,
        0.001,
        0.01
    ]

    print("\n========== Experiment 3: Learning Rate ==========")

    for learning_rate in learning_rates:

        model = MLPClassifier(
            hidden_layer_sizes=(32, 16),
            activation="relu",
            solver="adam",
            learning_rate_init=learning_rate,
            max_iter=1000,
            random_state=42
        )

        model.fit(X_train, y_train)

        prediction = model.predict(X_test)

        accuracy = accuracy_score(
            y_test,
            prediction
        )

        print(
            f"Learning Rate {learning_rate}: "
            f"Accuracy = {accuracy:.4f}, "
            f"Iterations = {model.n_iter_}"
        )


# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------

def main():

    # Task 1, 2, 3
    df = load_dataset()

    # Task 4
    check_class_balance(df)

    # Task 5
    df, previous_default_encoder = convert_dataset(df)

    # Task 6
    X, y = split_features_target(df)

    # Task 7 & 8
    X_train, X_test, y_train, y_test = split_dataset(X, y)

    # Task 9
    X_train, X_test, scaler = scale_features(
        X_train,
        X_test
    )

    # Task 10 & 11
    model = train_model(
        X_train,
        y_train
    )

    # Task 12-15
    evaluate_model(
        model,
        X_train,
        y_train,
        X_test,
        y_test
    )

    # Task 16
    plot_training_loss(model)

    # -----------------------------------------------------
    # Task 17 - New loan applicants
    # -----------------------------------------------------

    applicant_data = pd.DataFrame({

        "Age": [25, 42, 55, 31, 47],

        "Income": [
            350000,
            750000,
            250000,
            600000,
            450000
        ],

        "LoanAmount": [
            400000,
            300000,
            900000,
            500000,
            700000
        ],

        "CreditScore": [
            720,
            680,
            590,
            750,
            620
        ],

        "EmploymentYears": [
            3,
            15,
            5,
            8,
            12
        ],

        "ExistingLoans": [
            1,
            2,
            4,
            0,
            3
        ],

        "MonthlyDebt": [
            12000,
            25000,
            45000,
            15000,
            35000
        ],

        "LoanTerm": [
            36,
            48,
            60,
            36,
            48
        ],

        "PreviousDefault": [
            "No",
            "No",
            "Yes",
            "No",
            "Yes"
        ],

        "HomeOwnership": [
            "Own",
            "Mortgage",
            "Rent",
            "Own",
            "Rent"
        ]
    })

    predict_loan_applicants(
        applicant_data,
        model,
        scaler,
        previous_default_encoder,
        X.columns
    )

    # Hyperparameter experiments
    hyperparameter_experiments(
        X_train,
        y_train,
        X_test,
        y_test
    )


if __name__ == "__main__":
    main()