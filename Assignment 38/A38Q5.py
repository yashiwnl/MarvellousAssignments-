import pandas as pd

def load_dataset():
  df = pd.read_csv("student_performance_ml.csv")

  print("Average StudyHours by FinalResults")
  print(df.groupby("FinalResult")["StudyHours"].mean())

  print("\n Average Attendance by FinalResults")
  print(df.groupby("FinalResult")["Attendance"].mean())

  #Based on my observations, the students whos StudyHours
  #are more results in FinalResults as 1 i.e passed

  #And the students whos Attendace is more results in 
  #Final results as 1 i.e passed


def main():
  load_dataset()

if __name__ == "__main__":
  main()