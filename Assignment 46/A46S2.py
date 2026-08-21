import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def load_dataset():

  #Step 1 Get Data
  df = pd.read_csv("Advertising.csv")

  return df

def clean_dataset(df):

  print(df)
  df.dropna(inplace=True)
  df = df.drop(columns= "Unnamed: 0")

  return df

def main():
  df = load_dataset()
  df = clean_dataset(df)

if __name__ == "__main__":
  main()