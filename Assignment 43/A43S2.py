import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_dataset():

  #Step 1: Get Data

  df = pd.read_csv("PlayPredictor.csv")

  #Step 2: Clean, Prepare and Manipulate data

  whether_encoder = LabelEncoder()
  temperature_encoder = LabelEncoder()
  play_encoder = LabelEncoder()

  df['Whether'] = whether_encoder.fit_transform(df['Whether'])
  df['Temperature'] = temperature_encoder.fit_transform(df['Temperature'])
  df['Play'] = play_encoder.fit_transform(df['Play'])

  print(df)

def main():
  load_dataset()

if __name__ == "__main__":
  main()