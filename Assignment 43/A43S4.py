import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier


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

  #Step 3: Train Data

  x = df[['Whether', 'Temperature']]
  y = df['Play']

  model = KNeighborsClassifier(n_neighbors=3)
  model = model.fit(x,y)

  #Step 4: Test Data

  weather = input("Enter Weather: ")
  temperature = input("Enter Temperature: ")

  weather_encoded = whether_encoder.transform([weather])
  temperature_encoded = temperature_encoder.transform([temperature])

  new_data = pd.DataFrame({
    "Whether" : weather_encoded,
    "Temperature" : temperature_encoded
  })

  prediction = model.predict(new_data)

  result = play_encoder.inverse_transform(prediction)

  print("Predicted Result: ",result[0])

def main():
  load_dataset()

if __name__ == "__main__":
  main()