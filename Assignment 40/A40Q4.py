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

  new_students = pd.DataFrame({
    "StudyHours": [2, 4, 6, 8, 10],
    "Attendance": [60, 72, 85, 90, 95],
    "PreviousScore": [45, 55, 66, 78, 88],
    "AssignmentsCompleted": [3, 5, 7, 8, 10],
    "SleepHours": [5, 6, 7, 7, 8]
})

  y_pred = model.predict(new_students)

  print("Predictions: ")
  print(y_pred)


def main():
  train_dataset()

if __name__ == "__main__":
  main()