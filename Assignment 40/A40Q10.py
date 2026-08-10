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
  model = DecisionTreeClassifier(max_depth=None)
  model.fit(x_train,y_train)

  y_test_pred = model.predict(x_test)
  testing_accuracy = accuracy_score(y_test,y_test_pred)

  y_train_pred = model.predict(x_train)
  training_accuracy = accuracy_score(y_train,y_train_pred)
  print("Testing Accuracy: ", testing_accuracy * 100)
  print("Training Accuracy: ", training_accuracy * 100)

  # The model achieved 100% accuracy on both training and testing data. 
  # Therefore, there is no clear indication of overfitting based on these accuracy values, 
  # as the model performs equally well on unseen testing data


def main():
  train_dataset()

if __name__ == "__main__":
  main()