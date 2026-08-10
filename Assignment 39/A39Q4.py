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

  model = DecisionTreeClassifier()

  model.fit(x_train,y_train)

  y_pred = model.predict(x_test)

  cm = confusion_matrix(y_test,y_pred)

  cm_display = ConfusionMatrixDisplay(confusion_matrix=cm)
  cm_display.plot(cmap=plt.cm.Blues)

  plt.show()

  #The confusion matrix shows that the model correctly classified all 6 test samples. 
  # It correctly predicted 5 students as Fail (TN) and 1 student as Pass (TP). 
  # There were no False Positive or False Negative predictions. 

def main():
  train_model()

if __name__ == "__main__":
  main()