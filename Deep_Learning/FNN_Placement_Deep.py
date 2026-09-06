#---------------------------------------------------------------------------------
# Deep Learning Pipeline
#---------------------------------------------------------------------------------
# 1.  Read the Data from csv
# 2.  Data Analysis (EDA)
# 3.  Preprocessing 
# 4.  Train Test Split
# 5.  Feature Scaling
# 6.  FNN Model trainig
# 7.  Model Evalution
# 8.  Graphical Representation
# 9.  Model Preserve
# 10. Model Loding and Preserve
# 11. Test Unseen Data
#-----------------------------------------------------------------------------------

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix
import joblib
import matplotlib.pyplot as plt

#---------------------------------------------------------------------------------
# 1.  Read the Data from csv
#----------------------------------------------------------------------------------

print("1.  Read the Data from csv")
data = pd.read_csv("placement_data.csv")
print("Complete Dataset :")
print(data)

#---------------------------------------------------------------------------------
# 2.  Data Analysis (EDA)
#----------------------------------------------------------------------------------
print("\n2. Data Analysis (EDA)")
print("\n-----> First 5 Rows        : ")
print(data.head())

print("\n-----> Columns names       : ")
print(data.columns)

print("\n-----> Shape of Dataset    : ")
print(data.shape)

print("\n-----> Statistical Summary : ")
print(data.describe())

#---------------------------------------------------------------------------------
# 3.  Preprocessing
#---------------------------------------------------------------------------------
print("\n3.  Preprocessing")
X = data[['Aptitude', 'Coding', 'Communication', 'Academics', 'Internship']]
Y = data['Placed']
print("-----> Input Features :")
print(X.head())

print("\n-----> Target :")
print(Y.head())

#---------------------------------------------------------------------------------
# 4.  Train Test Split
#---------------------------------------------------------------------------------
print("\n4.  Train Test Split")

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.30,random_state=42)

print("Training Input Shape  :", X_train.shape)
print("Testing Input Shape   :", X_test.shape)
print("Training Output Shape :", Y_train.shape)
print("Testing Output Shape  :", Y_train.shape)

#---------------------------------------------------------------------------------
# 5.  Feature Scaling
#---------------------------------------------------------------------------------
print("\n5.  Feature Scaling")

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)

print("\nScaled Training Data :")
print(X_train_scaled[:5])

#---------------------------------------------------------------------------------
# 6.  FNN Model trainig
#---------------------------------------------------------------------------------
print("\n6.  FNN Model trainig")
model = MLPClassifier(
    hidden_layer_sizes = (8,4),
    activation ='relu',
    solver='adam',
    max_iter=1000,
    random_state=42
)
print(model)

print("Train the Model:")
model  = model.fit(X_train_scaled,Y_train)
print("\n-----> Model Trainig Completed  <-----")


#---------------------------------------------------------------------------------
# 7.  Model Evalution
#---------------------------------------------------------------------------------
print("\n7.  Model Evalution")
Y_Pred = model.predict(X_test_scaled)

accuracy = accuracy_score(Y_test,Y_Pred)
print("\nAccuracy of Deep Learning Model is : ",accuracy)

cm = confusion_matrix(Y_test,Y_Pred)
print("\nConfusion Matrix:")
print(cm)

print("\nPredict the Probability :")
Y_prob   = model.predict_proba(X_test_scaled)
print(Y_prob[:5])

#---------------------------------------------------------------------------------
# 9.  Model Preserve
#----------------------------------------------------------------------------------
print("\n9.  Model Preserve")
joblib.dump(model,"placement_fnn_model.pkl")
joblib.dump(scaler,"placement_scalar.pkl")

print("\n---> Model and Scalar gets dumped Successfully <---")

#---------------------------------------------------------------------------------
# 10. Model Loding and Preserve
#----------------------------------------------------------------------------------
print("\n10. Model Loding and Preserve")

loaded_model =joblib.load("placement_fnn_model.pkl")
loaded_scalar =joblib.load("placement_scalar.pkl")

print("\n---> Model get's loaded Successfully <---")

#---------------------------------------------------------------------------------
# 11. Test Unseen Data
# Apptitude        :   70
# Coding           :   75
# Communication    :   80
# Academics        :   85
# Internship       :   1
#----------------------------------------------------------------------------------
print("\n11. Test Unseen Data")

new_student = pd.DataFrame([[70,75,80,85,1]], columns=['Aptitude', 'Coding', 'Communication', 'Academics', 'Internship'])

new_student_scaled = loaded_scalar.transform(new_student)

new_prediction = loaded_model.predict(new_student_scaled)

new_probability = loaded_model.predict_proba(new_student_scaled)

print("\nNew Student Data :")
print(new_student)

print("\nPrediction Probability :", new_probability)
if new_prediction[0] == 1:
    print("Prediction : Placed")
else:
    print("Prediction : Unplaced")