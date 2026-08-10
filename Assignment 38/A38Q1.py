import pandas as pd

def load_dataset():
  df = pd.read_csv("student_performance_ml.csv")

  print("First 5 records:")
  print(df.head())

  print("\nLast five records:")
  print(df.tail())

  print("\nTotal rows and columns: ")
  print(df.shape)

  print("Column names: ")
  print(df.columns)

  print("Data types: ")
  print(df.dtypes)


def main():
  load_dataset()

if __name__ == "__main__":
  main()