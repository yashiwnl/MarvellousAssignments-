from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

def train_model():

  df = pd.read_csv("student_performance_ml.csv")

  x = df.drop(columns="FinalResult")
  y = df["FinalResult"]

  x_train,x_test,y_train,y_test = train_test_split(x,y, test_size=0.2, random_state=42)

  model = DecisionTreeClassifier()

  model.fit(x_train,y_train)

  y_pred = model.predict(x_test)

  print("Actual Values:")
  print(y_test)

  print("Predicted Values:")
  print(y_pred)

def main():
  train_model()

if __name__ == "__main__":
  main()