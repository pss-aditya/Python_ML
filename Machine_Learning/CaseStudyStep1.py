import pandas as pd


Border = "-"*40
##########################################
# Step 1 : Load the Dataset 
###########################################

print(Border)
print("Step 1 : Load the Dataset ")
print(Border)

DataPath = "iris.csv"

df = pd.read_csv(DataPath)
print("Dataset loaded successfully")
print("Initial Entry from Dataset are :")
print(df.head()) 