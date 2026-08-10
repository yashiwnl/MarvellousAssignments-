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

  accuracy = accuracy_score(y_test, y_pred)

  print("Accuracy with SleepHours: ",accuracy*100)


  x_ws = df.drop(columns=["FinalResult", "SleepHours"])

  x_train_ws,x_test_ws,y_train_ws,y_test_ws = train_test_split(x_ws,y, test_size=0.2, random_state=42)
 
  model_ws = DecisionTreeClassifier()
  model_ws.fit(x_train_ws,y_train_ws)

  y_pred_ws = model_ws.predict(x_test_ws)

  accuracy_ws = accuracy_score(y_test_ws, y_pred_ws)

  print("Accuracy without SleepHours: ",accuracy_ws*100)

  #No it doesnt afftect the accuracy and performance as both accuracies stay 100%

def main():
  train_dataset()

if __name__ == "__main__":
  main()