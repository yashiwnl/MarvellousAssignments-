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

  y_test_pred = model.predict(x_test)

  correct = 0

  for actual, predicted in zip(y_test,y_test_pred):
    if actual == predicted:
      correct += 1

  manual_accuracy = (correct / len(y_test)) * 100

  sklearn_accuracy = accuracy_score(y_test, y_test_pred)

  print("Manual Accuracy: ",manual_accuracy, "%")
  print("Sklearn Accuracy: ",sklearn_accuracy*100, "%")



def main():
  train_dataset()

if __name__ == "__main__":
  main()