import pandas as pd
import matplotlib.pyplot as plt

def load_dataset():
  df = pd.read_csv("student_performance_ml.csv")

  plt.hist(
    df["StudyHours"],
    bins=10,
    rwidth= 0.9
    
  )

  plt.xlabel("Study Hours")
  plt.ylabel("Number of Students")
  plt.title("Distribution of Study Hours")

  plt.show()

  #The distribution tells me that 4 students study for 1.8-2.5 hours,
  #5.5-6.2 hours and 7.8-8.5 hours
  # 3 students study for 2.5-3.2 hours, 4-5.5 hours and 7-7.8 hours
  # and 2 students study for 1-1.8 hours, 3.2-4 hours and 6.2-7 hours


def main():
  load_dataset()

if __name__ == "__main__":
  main()