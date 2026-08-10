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

  new_entry = pd.DataFrame({
    "StudyHours" : [6],
    "Attendance" : [85],
    "PreviousScore" : [66],
    "AssignmentsCompleted" : [7],
    "SleepHours" : [7]
  })

  model = DecisionTreeClassifier()

  model = model.fit(x_train,y_train)

  y_pred = model.predict(new_entry)

  if y_pred[0] == 1:
    print("Student Passed")
  else:
    print("Student Failed")



def main():
  train_model()

if __name__ == "__main__":
  main()