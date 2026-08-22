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
    


def main():
    MarvellousRegression("Advertising.csv")

if __name__ == "__main__":
    main()
