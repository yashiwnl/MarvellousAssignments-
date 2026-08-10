from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import pandas as pd

def train_model():

  df = pd.read_csv("student_performance_ml.csv")

  x = df.drop(columns="FinalResult")
  y = df["FinalResult"]

  x_train,x_test,y_train,y_test = train_test_split(x,y, test_size=0.2, random_state=42)


  model1 = DecisionTreeClassifier(max_depth=1)

  model1.fit(x_train,y_train)

  y_pred1 = model1.predict(x_test)

  accuracy1 = accuracy_score(y_test, y_pred1)

  print("Accuracy of model 1 with max_depth = 1 : ",accuracy1*100)


  model2 = DecisionTreeClassifier(max_depth=3)

  model2.fit(x_train,y_train)

  y_pred2 = model2.predict(x_test)

  accuracy2 = accuracy_score(y_test, y_pred2)

  print("Accuracy of model 2 with max_depth = 3 : ",accuracy2*100)


  model3 = DecisionTreeClassifier(max_depth=None)

  model3.fit(x_train,y_train)

  y_pred3 = model3.predict(x_test)

  accuracy3 = accuracy_score(y_test, y_pred3)

  print("Accuracy of model 3 with max_depth = None : ",accuracy3*100)

  #All three Decision Tree models achieved 100% testing accuracy for the given train-test split. 
  # This indicates that all three models correctly classified the six test samples. 
  # The difference in max_depth did not affect the testing accuracy on this particular dataset split. 
  # because the dataset contains only 30 students and the testing set contains only 6 students



def main():
  train_model()

if __name__ == "__main__":
  main()