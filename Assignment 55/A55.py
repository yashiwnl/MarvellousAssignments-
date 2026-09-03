import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import VotingClassifier

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def load_dataset():
    df = pd.read_csv("Customer_Loan_Approval.csv")

    return df
def clean_dataset(df):
    df.dropna(inplace= True)

    return df

def scale_dataset(x_train, x_test):

    scaler = StandardScaler()

    x_train = scaler.fit_transform(x_train)
    x_test = scaler.transform(x_test)

    return x_train, x_test


def split_dataset(df):

    x = df.drop(columns=" LoanApproved")
    y = df[" LoanApproved"]

    x_train, x_test, y_train,y_test = train_test_split(
                                                        x,
                                                        y, 
                                                        test_size= 0.2, 
                                                        random_state= 42
                                                        )

    return x_train, x_test, y_train, y_test


def train_models(x_train, y_train):

    model_log = LogisticRegression()
    model_dt = DecisionTreeClassifier()
    model_knn = KNeighborsClassifier()

    model_log.fit(x_train, y_train)
    model_dt.fit(x_train, y_train)
    model_knn.fit(x_train, y_train)   

    return model_log, model_dt, model_knn

def calculate_indivisual_accuracy(x_test, y_test, model_log, model_dt, model_knn):

    y_log_pred = model_log.predict(x_test)
    y_dt_pred = model_dt.predict(x_test)
    y_knn_pred = model_knn.predict(x_test)

    log_accuracy = accuracy_score(y_test, y_log_pred)
    dt_accuracy = accuracy_score(y_test, y_dt_pred)
    knn_accuracy = accuracy_score(y_test, y_knn_pred)

    print("Logistic Regression Accuracy score: ", log_accuracy*100)
    print("Decision Tree Accuracy score: ", dt_accuracy*100)
    print("KNN Classifier Accuracy score: ", knn_accuracy*100)


def voting_model(model_log, model_dt, model_knn, x_train, y_train, x_test, y_test):

    hard_model = VotingClassifier(estimators= [
                                            ("logistic_regression",model_log),
                                            ("decision_tree", model_dt),
                                            ("knn",model_knn)  
                                            ],
                            voting= "hard")

    soft_model = VotingClassifier(estimators= [
                                            ("logistic_regression",model_log),
                                            ("decision_tree", model_dt),
                                            ("knn",model_knn)  
                                            ],
                            voting= "soft")

    hard_model.fit(x_train, y_train)
    y_hard_pred = hard_model.predict(x_test)
    hard_accuracy = accuracy_score(y_test, y_hard_pred)
    print("Hard voting model Accuracy: ", hard_accuracy *100)

    soft_model.fit(x_train, y_train)
    y_soft_pred = soft_model.predict(x_test)
    soft_accuracy = accuracy_score(y_test, y_soft_pred)
    print("Soft voting model Accuracy: ", soft_accuracy *100)

def main():
    df = load_dataset()
    df = clean_dataset(df)
    x_train, x_test, y_train, y_test = split_dataset(df) 
    x_train, x_test = scale_dataset(x_train, x_test)

    model_log, model_dt, model_knn = train_models(x_train, y_train)

    calculate_indivisual_accuracy(x_test, y_test, model_log, model_dt, model_knn)

    voting_model(model_log,model_dt,model_knn, x_train, y_train, x_test, y_test)


    
if __name__ == "__main__":
    main()