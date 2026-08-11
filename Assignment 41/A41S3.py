import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def load_dataset():

  #Step 1: Get Data
  df = pd.read_csv("WinePredictor.csv")

  #Step 2: Clean, Prepare and Manipulate Data
  df.dropna(inplace=True)
  x = df.drop(columns="Class")
  y = df["Class"]

  #Step 3: Train Data
  x_train,x_test,y_train,y_test = train_test_split(x, y, test_size=0.2, random_state= 42)
  model = DecisionTreeClassifier()
  model = model.fit(x_train, y_train)



def main():
  load_dataset()

if __name__ == "__main__":
  main()