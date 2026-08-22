# Income    Spending Score
# High       Low
# High       High
# Low        High
# Low        Low

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def main():
    ############################################################
    # STEP 1 : Load the Dataset
    ############################################################
    
    df = pd.read_csv("Mall_Customers.csv")
    print("DataSet Loaded with values")
    print(df.head())
    print("Missing Values:")
    print(df.isnull().sum())

if __name__ == "__main__":
    main()
