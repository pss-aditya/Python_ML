import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def MarvellousRegression(Datapath):
    Border = "-"*60
    ###################################################
    # Step 1 : Load the Data
    ###################################################
    
    print(Border)
    print("Load the Data")
    print(Border)
    
    df = pd.read_csv(Datapath)
    print(df.head())
    
    
    ###################################################
    # Step 2 : Drop the Unwanted Column
    ###################################################
    
    print(Border)
    print("Drop the unwanted Column")
    print(Border)
    
    if "Unnamed: 0" in df.columns:
        df = df.drop(columns = ["Unnamed: 0"])
        
    print(df.head())
    
    ###################################################
    # Step 3 : Check Missing Values
    ###################################################
    
    print(Border)
    print("Check Missing Values")

    
    print("Total Missing Values :")
    print(Border)
    print(df.isnull().sum())    
    print(Border)
    
    ###################################################
    # Step 4 : Statistical Summary
    ###################################################
    
    print(Border)
    print("Statistical Summary")
    print(Border)
    
    print(df.describe())
  
    
    ###################################################
    # Step 5 : Co-relation
    ###################################################
    
    print(Border)
    print("Co-relation")
    print(Border)
    
    print(df.corr())
    
    ###################################################
    # Step 6 : Independent and Dependent variable
    ###################################################
    
    print(Border)
    print("Independent and Dependent variable")
    print(Border)

    X = df[["TV","radio","newspaper"]]
    Y = df["sales"]
    
    print("Independent Variable are :")
    print(X.head())
    
    print("Dependent Variable are   :")
    print(Y.head())
    
    ###################################################
    # Step 7 : Split the Dataset
    ###################################################
    
    print(Border)
    print("Split the Dataset")
    print(Border) 
    
    X_train, X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.20,random_state=42)
    
    print("Trainig Data :", X_train.shape)
    print("Testing Data :", X_test.shape)

def main():
    MarvellousRegression("Advertising.csv")

if __name__ == "__main__":
    main()
