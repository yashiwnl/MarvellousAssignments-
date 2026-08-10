import pandas as pd
import matplotlib.pyplot as plt

def load_dataset():
  df = pd.read_csv("student_performance_ml.csv")

  plt.boxplot(df["Attendance"])

  plt.ylabel("Attendance (%)")
  plt.title("Attendance Distribution")

  plt.show()
  
  Q1 = df["Attendance"].quantile(0.25)
  Q3 = df["Attendance"].quantile(0.75)

  IQR = Q3 - Q1

  lower = Q1 - 1.5 * IQR
  upper = Q3 + 1.5 * IQR

  outliers = df[
      (df["Attendance"] < lower) |
      (df["Attendance"] > upper)
  ]

  print("Number of Attendance Outliers:", len(outliers))
  print(outliers["Attendance"])

def main():
  load_dataset()

if __name__ == "__main__":
  main()