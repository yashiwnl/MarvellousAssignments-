import pandas as pd

def load_dataset():

  #Step 1: Get Data
  df = pd.read_csv("WinePredictor.csv")

  #Step 2: Clean, Prepare and Manipulate Data
  df.dropna(inplace=True)
  x = df.drop(columns="Class")
  y = df["Class"]

def main():
  load_dataset()

if __name__ == "__main__":
  main()