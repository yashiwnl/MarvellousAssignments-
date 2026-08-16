import pandas as pd

def load_dataset():

  df = pd.read_csv("PlayPredictor.csv")

  print("First five records: \n")
  print(df.head(5))

  print("\nRows: ", df.shape[0])
  print("Columns: ", df.shape[1])

  print("\nColumn Names: ")
  print(df.columns)


def main():
  load_dataset()

if __name__ == "__main__":
  main()