import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix

from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier 
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import VotingClassifier

def load_dataset():
    df = pd.read_csv("Fraudulent_Transaction_Detection.csv")

    return df

def clean_dataset(df):
    df.dropna(inplace= True)

    return df

def split_dataset(df):
    df = pd.DataFrame(df)
    x = df.drop(" Fraud", axis=1)
    y = df[" Fraud"]

    x_train, x_test, y_train, y_test = train_test_split(
                                                        x, 
                                                        y, 
                                                        test_size= 0.2, 
                                                        random_state= 42
                                                        )

    return x_train, x_test, y_train, y_test

def train_models(x_train, y_train):

    dt_model = DecisionTreeClassifier(random_state= 42)
    log_model = LogisticRegression(random_state= 42)
    bag_model = BaggingClassifier(
                                    estimator=dt_model, 
                                    n_estimators= 10,
                                    random_state= 42
                                    )
    rf_model = RandomForestClassifier(
                                        n_estimators=10, 
                                        random_state=42
                                        )
    boost_model = AdaBoostClassifier(
                                     n_estimators= 50, 
                                     learning_rate= 1.0, 
                                     random_state= 42
                                     )

    voting_model = VotingClassifier(
                                    estimators= [
                                        ("decision_tree", dt_model),
                                        ("logistic", log_model)
                                    ],
                                    voting= "hard"
                                    )

    dt_model.fit(x_train, y_train)
    bag_model.fit(x_train, y_train)
    rf_model.fit(x_train, y_train)
    boost_model.fit(x_train, y_train)
    voting_model.fit(x_train, y_train)

    return dt_model, bag_model, rf_model, boost_model, voting_model


def evaluate_models(x_test, y_test, dt_model, bag_model, rf_model, boost_model, voting_model):

    y_dt_pred = dt_model.predict(x_test)
    y_bag_pred = bag_model.predict(x_test)
    y_rf_pred = rf_model.predict(x_test)
    y_boost_pred = boost_model.predict(x_test)
    y_voting_pred = voting_model.predict(x_test)

    dt_accuracy = accuracy_score(y_test, y_dt_pred)
    bag_accuracy = accuracy_score(y_test, y_bag_pred)
    rf_accuracy = accuracy_score(y_test, y_rf_pred)
    boost_accuracy = accuracy_score(y_test, y_boost_pred)
    voting_accuracy = accuracy_score(y_test, y_voting_pred)

    dt_precision = precision_score(y_test, y_dt_pred)
    bag_precision = precision_score(y_test, y_bag_pred)
    rf_precision = precision_score(y_test, y_rf_pred)
    boost_precision = precision_score(y_test, y_boost_pred)
    voting_precision = precision_score(y_test, y_voting_pred)

    dt_recall = recall_score(y_test, y_dt_pred)
    bag_recall = recall_score(y_test, y_bag_pred)
    rf_recall = recall_score(y_test, y_rf_pred)
    boost_recall = recall_score(y_test, y_boost_pred)
    voting_recall = recall_score(y_test, y_voting_pred)

    dt_f1 = f1_score(y_test, y_dt_pred)
    bag_f1 = f1_score(y_test, y_bag_pred)
    rf_f1 = f1_score(y_test, y_rf_pred)
    boost_f1 = f1_score(y_test, y_boost_pred)
    voting_f1 = f1_score(y_test, y_voting_pred)

    dt_cm = confusion_matrix(y_test, y_dt_pred)
    bag_cm = confusion_matrix(y_test, y_bag_pred)
    rf_cm = confusion_matrix(y_test, y_rf_pred)
    boost_cm = confusion_matrix(y_test, y_boost_pred)
    voting_cm = confusion_matrix(y_test, y_voting_pred)

    final_result = {
                    "Algorithm": ["Decision Tree", "Bagging", "Random Forest", "AdaBoost", "Voting"],
                    "Accuracy": [dt_accuracy, bag_accuracy, rf_accuracy, boost_accuracy, voting_accuracy],
                    "Precision": [dt_precision, bag_precision, rf_precision, boost_precision, voting_precision],
                    "Recall": [dt_recall, bag_recall, rf_recall, boost_recall, voting_recall],
                    "F1": [dt_f1, bag_f1, rf_f1, boost_f1, voting_f1]
    }

    final_result = pd.DataFrame(final_result)
    print(final_result)

    print("Decision Tree Confusion Matrix: ")
    print(dt_cm)

    print("Bagging Confusion Matrix: ")
    print(bag_cm)

    print("Random Forest Confusion Matrix: ")
    print(rf_cm)

    print("AdaBoost Confusion Matrix: ")
    print(boost_cm)

    print("Voting Confusion Matrix: ")
    print(voting_cm)


def main():
    df = load_dataset()
    df = clean_dataset(df)
    x_train, x_test, y_train, y_test = split_dataset(df)
    dt_model, bag_model, rf_model, boost_model, voting_model = train_models(x_train, y_train)
    evaluate_models(x_test, y_test, dt_model, bag_model, rf_model, boost_model, voting_model)


if __name__ == "__main__":
    main()