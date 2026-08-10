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

  plot_tree(
    model,
    feature_names=x.columns,
    class_names=["Fail", "Pass"],
    filled=True
  )

  plt.show()

  # Root Node: StudyHours
  # StudyHours was selected as the root node because, for this particular training split, 
  # it provided the most effective first separation between 
  # Pass and Fail students according to the Decision Tree's splitting criterion.

def main():
  train_dataset()

if __name__ == "__main__":
  main()