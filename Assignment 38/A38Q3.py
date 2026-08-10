import pandas as pd

def load_dataset():
  df = pd.read_csv("student_performance_ml.csv")

  print("Average StudyHours: ", df["StudyHours"].mean())
  print("\nAverage Attendance: ", df["Attendance"].mean())
  print("\nMaximum PreviousScore: ", df["PreviousScore"].max())
  print("\nMinimum SleepHours: ", df["SleepHours"].min())


def main():
  load_dataset()

if __name__ == "__main__":
  main()