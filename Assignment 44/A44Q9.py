import pandas as pd
import numpy as np
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

  data2 = {
    "Name" : ["Amit", "Sagar", "Pooja"],
    "Math" : [np.nan, 76 ,88],
    "Science" : [91, np.nan, 85]
  }

  df2 = pd.DataFrame(data2)

  df2["Math"] = df2["Math"].fillna(df2["Math"].mean())
  df2["Science"] = df2["Science"].fillna(df2["Science"].mean())

  print(df2)



if __name__ == "__main__":
  main()