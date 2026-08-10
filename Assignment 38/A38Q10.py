import pandas as pd
import matplotlib.pyplot as plt

def load_dataset():
  df = pd.read_csv("student_performance_ml.csv")

  sleep_result = df.groupby("FinalResult")["SleepHours"].mean()

  plt.bar(
    ["Pass", "Fail"],
    sleep_result
  )

  plt.xlabel("Final Result")
  plt.ylabel("Average Sleep Hours")
  plt.title("Sleep Hours vs Final Result")

  plt.show()

  #Students who passed slept an average of 7.44 hours, compared to 5.58 hours for students who failed. 
  #This suggests that adequate sleep is associated with better academic performance . 
  #However, sleeping more does not guarantee success 
  #because other factors such as study hours, attendance, previous score, 
  #and assignment completion also influence the final result.

def main():
  load_dataset()

if __name__ == "__main__":
  main()