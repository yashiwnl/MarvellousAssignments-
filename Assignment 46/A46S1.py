import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def load_dataset():

  #Step 1 Get Data
  df = pd.read_csv("Advertising.csv")

  return df

def main():
  df = load_dataset()
if __name__ == "__main__":
  main()