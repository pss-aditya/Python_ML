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

    ############################################################
    # STEP 2 : Feature Selection
    ############################################################
    X =df[["AnnualIncome","SpendingScore"]]
    print("Selected Features :")
    print(X.head())

    ############################################################
    # STEP 3 : Scale the Data
    ############################################################
    scalar = StandardScaler()
    X_scaled = scalar.fit_transform(X)
    print("Scaled Data :")
    print(X_scaled[:5])
    

    ############################################################
    # STEP 4 : Elbow method
    ############################################################  
    WCSS = []
    
    for k in range(1,11):
        model = KMeans(n_clusters = k,random_state = 42,n_init = 10)
        model.fit(X_scaled)
        WCSS.append(model.inertia_)
        
    print("Values of WCSS : ")
    for i in  range(len(WCSS)):
        print(f"{i+1} : {WCSS[i]}")

    ############################################################
    # STEP 5 : Elbow Visualization
    ############################################################    
    plt.plot(range(1,11),WCSS,marker = "o")
    
    plt.xlabel("Number of cluster : k")
    plt.ylabel("WCSS")
    plt.title("Elbow Method Analysis")
    
    plt.grid(True)
    
    plt.show()
    
    ############################################################
    # STEP 6 : Final K-Means Model
    ############################################################   
    model = KMeans(n_clusters = 4,random_state = 42,n_init = 10)
    clusters = model.fit_predict(X_scaled)
    df["Cluster"] = clusters
    
    
    ############################################################
    # STEP 7 : Display Dataset with Clusters
    ############################################################
    print("\nDataset with Cluster :")
    print(df.head(100))
    
    ############################################################
    # STEP 8 : Cluster Visualization
    ############################################################
    
    plt.scatter(
        X_scaled[:,0],
        X_scaled[:,1],
        c=clusters
    )
    
    plt.xlabel("Annual Income")
    plt.ylabel("Spending Score")
    plt.title("Customer Segmentation using K-Means")
    plt.grid(True)
    plt.show()
    

if __name__ == "__main__":
    main()
