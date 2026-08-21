import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

def load_dataset():

  #Step 1 Get Data
  df = pd.read_csv("Advertising.csv")

  return df

def clean_dataset(df):

  df.dropna(inplace=True)
  df = df.drop(columns= "Unnamed: 0")

  return df

def train_data(df):

  x = df.drop(columns= "sales")
  y = df["sales"]

  x_train, x_test, y_train, y_test = train_test_split(x,y, test_size= 0.5, random_state= 42)

  model = LinearRegression()

  model = model.fit(x_train, y_train)

  return model, x_test, y_test

def test_data(model, x_test):

  y_pred = model.predict(x_test)

  return y_pred

def calculate_accuracy(y_test, y_pred):

  score = r2_score(y_test, y_pred)

  return score

def main():
  df = load_dataset()
  df = clean_dataset(df)
  model, x_test, y_test = train_data(df)
  y_pred = test_data(model, x_test)

  score = calculate_accuracy(y_test, y_pred)


if __name__ == "__main__":
  main()