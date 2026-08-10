from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import pandas as pd

def train_model():

  #Step 1: Loading the dataset 
  df = pd.read_csv("student_performance_ml.csv")


  x = df.drop(columns="FinalResult")
  y = df["FinalResult"]

  #Step 2: Analyzing the data
  print("First 5 records: ",df.head(5))
  print("Rows: ",df.shape[0])
  print("Columns: ",df.shape[1])


  #Step 3: Visualisation
  plt.hist(df["StudyHours"], rwidth=0.9, bins=5)
  plt.title("StudyHours Distribution")
  plt.ylabel("No of Students")
  plt.xlabel("StudyHours")
  plt.show()

  #Step 4: Train Test Split
  x_train,x_test,y_train,y_test = train_test_split(x,y, test_size=0.2, random_state=42)

  #Step 5: Model Training 
  model = DecisionTreeClassifier()
  model.fit(x_train,y_train)

  #Step 6: Model Prediction
  y_pred = model.predict(x_test)

  #Step 7: Accuracy Calculation
  accuracy = accuracy_score(y_test, y_pred)
  accuracy = accuracy*100

  #Step 8: Confusion matrix generation
  cm = confusion_matrix(y_test,y_pred)
  cm_display = ConfusionMatrixDisplay(confusion_matrix=cm)
  cm_display.plot(cmap=plt.cm.Blues)
  plt.show()

  #Final Conclusion:
  print(f"Conclusion:\n The Decision Tree model achieved {accuracy:.2f}% accuracy.")
  print(f"The confusion matrix shows how correctly the model classified Pass and Fail students.")
def main():
  train_model()

if __name__ == "__main__":
  main()