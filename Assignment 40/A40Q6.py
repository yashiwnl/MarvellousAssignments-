import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def train_dataset():

  df = pd.read_csv("student_performance_ml.csv")

  x = df.drop(columns="FinalResult")
  y = df["FinalResult"]
  x_train,x_test,y_train,y_test = train_test_split(x,y, test_size=0.2, random_state=42)
 
  model = DecisionTreeClassifier()
  model.fit(x_train,y_train)

  y_pred = model.predict(x_test)

  misclassified = y_test != y_pred

  misclassified_students = x_test[misclassified]

  print(misclassified_students)

  print("Number of misclassifed students: ", misclassified.sum())

  print("Actual Results:")
  print(y_test[misclassified])

  print("Predicted Results:")
  print(y_pred[misclassified])

  # Number of misclassified students: 0. 
  # The Decision Tree correctly classified all students in the test dataset. 
  # There were no differences between the actual and predicted results.

def main():
  train_dataset()

if __name__ == "__main__":
  main()