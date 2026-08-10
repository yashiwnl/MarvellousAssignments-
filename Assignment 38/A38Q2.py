import pandas as pd

def load_dataset():
  df = pd.read_csv("student_performance_ml.csv")

  print("total number of students: ", len(df))

  passed = (df["FinalResult"] == 1).sum()
  failed = (df["FinalResult"] == 0).sum()

  print("Students passed: ", passed)
  print("Students failed: ", failed)



def main():
  load_dataset()

if __name__ == "__main__":
  main()