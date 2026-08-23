import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

##################################################################################
# Step 1 : Load the Dataset
##################################################################################

df = pd.read_csv("breast_cancer.csv")
print("Shape of Datastet :", df.shape)

print("First Few Records :")
print(df.head())

##################################################################################
# Step 2 : Seperate Features and Labels
##################################################################################

X = df.drop("target", axis=1)
Y = df["target"]

print("X shape : ",X.shape)
print("Y shape : ",Y.shape)

##################################################################################
# Step 3 : Split the dataset for training and testing
##################################################################################

X_train,X_test,Y_train,Y_test = train_test_split (X,Y,test_size=0.20,random_state=42)

##################################################################################
# Step 4 : Scale the features
##################################################################################

scalar = StandardScaler()

X_train = scalar.fit_transform(X_train)
X_test = scalar.fit_transform(X_test)

##################################################################################
# Step 5.1 : Create the Base Model
##################################################################################

base_model = DecisionTreeClassifier(random_state = 42)

##################################################################################
# Step 5.2 : Create the Bagging Model
##################################################################################

model = BaggingClassifier(
    estimator = base_model,
    n_estimators = 10,
    random_state = 42
)

##################################################################################
# Step 6 :Train the Model
##################################################################################

model = model.fit(X_train, Y_train)

##################################################################################
# Step 7 :Test the Model
##################################################################################

Y_pred = model.predict(X_test)

##################################################################################
# Step 8 :Evalaute the Model
##################################################################################

print("Accuracy :", accuracy_score(Y_test,Y_pred)*100)
print("Confusion Matrix : ", confusion_matrix(Y_test,Y_pred))