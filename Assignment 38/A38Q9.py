import pandas as pd
import matplotlib.pyplot as plt

def load_dataset():
  df = pd.read_csv("student_performance_ml.csv")

  assignment_result = df.groupby("FinalResult")["AssignmentsCompleted"].mean()

  plt.bar(
    ["Fail", "Pass"],
    assignment_result
  )
  plt.xlabel("Final Result")
  plt.ylabel("Average Assignments Completed")
  plt.title("Assignments Completed vs Final Result")

  plt.show()

  #Students who passed generally completed more assignments than students who failed. 
  # This suggests that completing assignments regularly increases knowledge. 
  # Students who failed tend to have fewer completed assignments on average. 

def main():
  load_dataset()

if __name__ == "__main__":
  main()