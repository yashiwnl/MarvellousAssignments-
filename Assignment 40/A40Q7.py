import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def train_dataset():

  df = pd.read_csv("student_performance_ml.csv")

  x = df.drop(columns="FinalResult")
  y = df["FinalResult"]

  x_train,x_test,y_train,y_test = train_test_split(x,y, test_size=0.2, random_state=0)
  model = DecisionTreeClassifier()
  model.fit(x_train,y_train)
  y_pred = model.predict(x_test)
  accuracy = accuracy_score(y_test,y_pred)
  print("Accuracy with random state = 0: ",accuracy * 100)

  x_train,x_test,y_train,y_test = train_test_split(x,y, test_size=0.2, random_state=10)
  model = DecisionTreeClassifier()
  model.fit(x_train,y_train)
  y_pred = model.predict(x_test)
  accuracy = accuracy_score(y_test,y_pred)
  print("Accuracy with random state = 10: ",accuracy * 100)  

  x_train,x_test,y_train,y_test = train_test_split(x,y, test_size=0.2, random_state=42)
  model = DecisionTreeClassifier()
  model.fit(x_train,y_train)
  y_pred = model.predict(x_test)
  accuracy = accuracy_score(y_test,y_pred)
  print("Accuracy with random state = 42: ",accuracy * 100)

def main():
  train_dataset()

if __name__ == "__main__":
  main()