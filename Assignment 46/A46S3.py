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

def train_data(df):

  x = df.drop(columns= "sales")
  y = df["sales"]

  x_train, x_test, y_train, y_test = train_test_split(x,y)

  model = LinearRegression()

  model = model.fit(x_train, y_train)

  return model, x_test, y_test


def main():
  df = load_dataset()
  df = clean_dataset(df)
  model, x_test, y_test = train_data(df)

if __name__ == "__main__":
  main()