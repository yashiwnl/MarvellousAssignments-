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

  df["Gender"] = ["Male", "Male", "Female"]

  df["Status"] = df["Total"].apply(lambda total: "Pass" if total >=250 else "Fail")

  df = df.rename(
    columns= {
      "Math" : "Mathematics"
      }
  )


  plt.boxplot(df["English"])

  plt.ylabel("English Marks")

  plt.show()

if __name__ == "__main__":
  main()