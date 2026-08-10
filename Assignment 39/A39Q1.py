from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

def train_model():

  df = pd.read_csv("student_performance_ml.csv")

  x = df.drop(columns="FinalResult")
  y = df["FinalResult"]

  x_train,x_test,y_train,y_test = train_test_split(x,y)

  model = DecisionTreeClassifier()

  model.fit(x_train,y_train)



def main():
  train_model()

if __name__ == "__main__":
  main()