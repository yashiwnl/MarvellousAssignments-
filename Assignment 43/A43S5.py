import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def checkAccuracy(x,y):

  x_train,x_test,y_train,y_test = train_test_split(x, y, test_size= 0.2, random_state= 42)

  for k in [1,3,5]:
    model = KNeighborsClassifier(n_neighbors=k)
    model = model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)

    print(f"Model Accuracy for K = {k} is: {(accuracy*100):.2f}")


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

  #Step 5: Calculate Accuracy

  checkAccuracy(x,y)


def main():
  load_dataset()

if __name__ == "__main__":
  main()