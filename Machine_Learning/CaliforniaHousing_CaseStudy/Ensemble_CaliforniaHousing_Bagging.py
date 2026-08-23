import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import BaggingRegressor
from sklearn.metrics import mean_squared_error, r2_score

#---------------------------------------------------------------------------------
# Step 1 : Load the Dataset
#---------------------------------------------------------------------------------
df = pd.read_csv("california_housing.csv")
print("Shape of Records :",df.shape)
print("\nFew Records      :")
print(df.head())


#---------------------------------------------------------------------------------
# Step 2 : Seperate the Dataset Features and Label
#---------------------------------------------------------------------------------
X = df.drop("target", axis = 1 )
Y = df["target"]

print("\nShape of X    :",X.shape)
print("\nShape of Y    :",Y.shape)


#---------------------------------------------------------------------------------
# Step 3 : Split the Dataset for Training and Testing
#---------------------------------------------------------------------------------
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.20,random_state =42)


#---------------------------------------------------------------------------------
# Step 4.1 : Create the Base Model
#---------------------------------------------------------------------------------
base_model = DecisionTreeRegressor(random_state = 42)


#---------------------------------------------------------------------------------
# Step 4.2 : Create the Bagging Model
#---------------------------------------------------------------------------------
model = BaggingRegressor(
    estimator = base_model,
    n_estimators = 10,
    random_state = 42
)


#---------------------------------------------------------------------------------
# Step 5 : Train the Model
#---------------------------------------------------------------------------------
model = model.fit(X_train,Y_train)



#---------------------------------------------------------------------------------
# Step 6 : Evaluate the Model
#---------------------------------------------------------------------------------
Y_pred = model.predict(X_test)


#----------------------------------------------------------------------------------
# Step 7 : Split the Dataset for Training and Testing
#---------------------------------------------------------------------------------

print("\nMSE :", mean_squared_error(Y_test,Y_pred))
print("\nR2  :", r2_score(Y_test,Y_pred))
