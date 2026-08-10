import pandas as pd
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split

def train_dataset():

  df = pd.read_csv("student_performance_ml.csv")


  x = df.drop(columns="FinalResult")
  y = df["FinalResult"]

  x_train,x_test,y_train,y_test = train_test_split(x,y, test_size=0.2, random_state=42)
  model = DecisionTreeClassifier()
  model.fit(x_train,y_train)
  y_pred = model.predict(x_test)
  accuracy = accuracy_score(y_test,y_pred)
  print("Accuracy without PerformanceIndex: ", accuracy * 100)

  df["PerformanceIndex"] =  (df["StudyHours"] * 2) +  df["Attendance"]

  x = df.drop(columns="FinalResult")
  y = df["FinalResult"]

  x_train,x_test,y_train,y_test = train_test_split(x,y, test_size=0.2, random_state=42)
  model = DecisionTreeClassifier()
  model.fit(x_train,y_train)
  y_pred = model.predict(x_test)
  accuracy = accuracy_score(y_test,y_pred)
  print("Accuracy with PerformanceIndex: ", accuracy * 100)

  # The original model achieved 100% accuracy, 
  # while the model with PerformanceIndex achieved 100% accuracy too. 
  # Therefore, adding PerformanceIndex did not improve the model's testing performance

def main():
  train_dataset()

if __name__ == "__main__":
  main()