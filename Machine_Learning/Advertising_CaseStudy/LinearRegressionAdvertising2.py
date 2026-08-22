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
    print(Border)
    
    print("Total Missing Values :")
    print(Border)
    print(df.isnull().sum())    
    print(Border)


def main():
    MarvellousRegression("Advertising.csv")

if __name__ == "__main__":
    main()
