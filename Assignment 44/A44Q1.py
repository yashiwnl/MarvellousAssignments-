import pandas as pd

def main():
  data = {
    "Name" : ["Amit", "Sagar", "Pooja"],
    "Math" : [85,90,78],
    "Science" : [92,88, 80],
    "English" : [75,85,82]
  }

  df = pd.DataFrame(data)

  print("Shape of data :")
  print(df.shape)
  print("Columns: ")
  print(df.columns)
  print("Datatypes: ")
  print(df.dtypes)

if __name__ == "__main__":
  main()