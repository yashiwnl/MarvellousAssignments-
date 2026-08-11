import pandas as pd

def load_dataset():

  #Step 1: Get Data
  df = pd.read_csv("WinePredictor.csv")

  print("Number of rows: ",df.shape[0])
  print("Number of columns: ",df.shape[1])

  print("\nColumn names: ")
  print(df.columns)

  print("\nFirst five records: ")
  print(df.head(5))

  print("\nData Types: ")
  print(df.dtypes)

  print("\n Missing Values:")
  print(df.isna().sum())


def main():
  load_dataset()

if __name__ == "__main__":
  main()