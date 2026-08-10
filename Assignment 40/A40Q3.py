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

  print("Orignal Accuracy: ",accuracy*100)


  x_two = df[["StudyHours", "Attendance"]]
  
  x_train_two,x_test_two,y_train_two,y_test_two = train_test_split(x_two,y, test_size=0.2, random_state=42)
 
  model_two = DecisionTreeClassifier()
  model_two.fit(x_train_two,y_train_two)

  y_pred_two = model_two.predict(x_test_two)

  accuracy_two = accuracy_score(y_test_two, y_pred_two)

  print("Accuracy with StudyHours and Attendance: ",accuracy_two*100)

  #The model trained using only StudyHours and Attendance achieved 100% accuracy compared to 100% 
  # using all features. Therefore, using only these two features maintained the model's performance.

def main():
  train_dataset()

if __name__ == "__main__":
  main()