import pandas as pd
import matplotlib.pyplot as plt

def main():
  data = {
    "Name" : ["Amit", "Sagar", "Pooja"],
    "Math" : [85,90,78],
    "Science" : [92,88, 80],
    "English" : [75,85,82]
  }

  df = pd.DataFrame(data)

  df["Total"] = df["Math"] + df["Science"] + df["English"]            

  df["Name"] = df["Name"].replace("Pooja", "Puja")

  amit = df[df["Name"] == "Amit"]

  print(amit)

  subjects = ["Math", "Science", "English"]

  marks = [
    amit["Math"].iloc[0],
    amit["Science"].iloc[0],
    amit["English"].iloc[0]
  ]

  plt.plot(subjects, marks)

  plt.xlabel("Subjects")
  plt.ylabel("Amit's Marks")

  plt.show()

if __name__ == "__main__":
  main()