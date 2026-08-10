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

  feature_importances = model.feature_importances_

  for feature, importance in zip(x.columns, feature_importances):
    print(feature,":", importance)

def main():
  train_dataset()

if __name__ == "__main__":
  main()