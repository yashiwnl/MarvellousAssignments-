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

  new_df = df.drop(columns="English")

  print(new_df)


if __name__ == "__main__":
  main()