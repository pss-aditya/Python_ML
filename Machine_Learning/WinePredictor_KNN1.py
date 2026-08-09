import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler


def MarvellousClassifier(DataPath):
    Border = "*"*60
    print(Border)
    print("Step 1 : Load the Dataset from CSV File")
    print(Border)
    
    df = pd.read_csv(DataPath)
    
    print(Border)
    print("Some Entries from Dataset :")
    print(df.head())
    print(Border)
    

def main():
    MarvellousClassifier("WinePredictor.csv")


if __name__ == "__main__":
    main()