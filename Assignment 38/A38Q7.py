import pandas as pd
import matplotlib.pyplot as plt

def load_dataset():
  df = pd.read_csv("student_performance_ml.csv")

  pass_students = df[df["FinalResult"] == 1]
  fail_students = df[df["FinalResult"] == 0]

  plt.scatter(
    pass_students["StudyHours"],
    pass_students["PreviousScore"],
    label = "Pass"
  )

  plt.scatter(
  fail_students["StudyHours"],
  fail_students["PreviousScore"],
  label = "Fail"
)

  plt.xlabel("Study Hours")
  plt.ylabel("Previous Score")
  plt.title("Study Hours vs Previous Score")
  plt.legend()

  plt.show()

def main():
  load_dataset()

if __name__ == "__main__":
  main()