import pandas as pd

def load_dataset():
  df = pd.read_csv("student_performance_ml.csv")

  print("Final Result Distribution: ")
  print(df["FinalResult"].value_counts())

  pass_percentage = (df["FinalResult"] == 1).mean() * 100
  fail_percentage = (df["FinalResult"] == 0).mean() * 100

  print(f"Pass Percentage: {pass_percentage:.2f} ")
  print(f"Fail Percentage: {fail_percentage:.2f} ")



def main():
  load_dataset()

if __name__ == "__main__":
  main()