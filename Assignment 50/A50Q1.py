import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

#---------------------------------
#Step 1.1: Load the dataset
#---------------------------------

cancer = load_breast_cancer(as_frame=True)

df = pd.DataFrame(cancer.frame) 

print("Shape of dataset: ", df.shape)

print("First few records")
print(df.head())

#---------------------------------
#Step 1.2: Clean the dataset
#---------------------------------

print("Missing values: ")
print(df.isnull().sum())

df.dropna(inplace= True)

#-----------------------------------------
#Step 1.3: EDA (Exploratory Data Analysis)
#-----------------------------------------

print("Statistics: ")
print(df.describe())

corr_matrix = df.corr()

sns.heatmap(corr_matrix)

plt.show()


#-------------------------------------
#Step 2: Separate Features and labels
#-------------------------------------

x = df.drop("target", axis=1)
y = df["target"]

print("X shape: ", x.shape)
print("y shape: ", y.shape)

#-------------------------------------------------
#Step 3: Split dataset for training and testing
#-------------------------------------------------

x_train, x_test, y_train, y_test =  train_test_split(
                                                      x, 
                                                      y, 
                                                      test_size=0.2, 
                                                      random_state=42
                                                      )


#-------------------------------------------------
#Step 4: Scale the features
#-------------------------------------------------

scaler = StandardScaler()

x_train = scaler.fit_transform(x_train)
x_test  = scaler.transform(x_test)
#-------------------------------------------------
#Step 5: Create the model
#-------------------------------------------------

model = LogisticRegression(max_iter=1000)

#-------------------------------------------------
#Step 6 :Train the model
#-------------------------------------------------

model.fit(x_train,y_train)

#-------------------------------------------------
#Step 7: Test the model
#-------------------------------------------------

y_pred = model.predict(x_test)

#-------------------------------------------------
#Step 8: Evaluate the model
#-------------------------------------------------
accuracy = accuracy_score(y_test,y_pred)
print("Accuracy: ", accuracy * 100)

print("Confusion Matrix: ")
print(confusion_matrix(y_test,y_pred))

print("Classification Report: ")
print(classification_report(y_test, y_pred))