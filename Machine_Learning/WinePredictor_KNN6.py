import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler


def MarvellousClassifier(DataPath):
    Border = "*"*60
    ##############################################
    # Step 1 : Load the Dataset from CSV File
    ##############################################
    print(Border)
    print("Step 1 : Load the Dataset from CSV File")
    print(Border)
    
    df = pd.read_csv(DataPath)
    
    print(Border)
    print("Some Entries from Dataset :")
    print(df.head())
    print(Border)
    
    
    
    ############################################
    # Step 2 : Clean the Dataset
    ############################################
    print(Border)
    print("Step 2 : Clean the Dataset")
    print(Border)
    
    df.dropna(inplace = True)
    
    print("Shape of Dataset : ", df.shape)
    print("Total Records    : ", df.shape[0]) # row
    print("Total Columns    : ", df.shape[1]) # column
    print(Border)
    
    
    
    ########################################################
    # Step 3 : Seperate Independent and Dependent Variable
    ########################################################
    print(Border)
    print("Step 3 : Seperate Independent and Dependent Variable")
    print(Border)
    
    X = df.drop(columns = ['Class'])
    Y = df['Class']
    
    print("Shape of X :", X.shape)
    print("Shape of Y :", Y.shape)
    
    print(Border)
    print("Input Columns  :",X.columns.tolist())
    print("Output Columns : Class")
    print(Border)
    
    
    
    ##############################################
    # Step 4 : Split the Dataset for Train & Test
    ##############################################
    print(Border)
    print("Step 4 : Split the Dataset for Train & Test")
    print(Border)
    
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.5, random_state=42, stratify=Y)
    
    print(Border)
    print("Training and Testing Data ")
    print("Shape of X_train :", X_train.shape)
    print("Shape of X_test  :", X_test.shape)
    print("Shape of Y_train :", Y_train.shape)
    print("Shape of Y_test  :", Y_test.shape)
    
    print(Border)
    


    ##############################################
    # Step 5 : Feature Scaling
    ##############################################
    print(Border)
    print("Step 5 : Feature Scaling")
    print(Border) 
    
    scalar = StandardScaler()
    X_train_Scaled =  scalar.fit_transform(X_train)
    X_test_scaled = scalar.fit_transform(X_test)
    
    print("Feature Scaling Done")
    print(Border)



    ##############################################
    # Step 6 : Build the Model
    ##############################################
    print(Border)
    print("Step 6 : Build the Model")
    print(Border) 

    model = KNeighborsClassifier(n_neighbors = 9)
    print("Classification Model is Created")



    ##############################################
    # Step 7 : Train the Model
    ##############################################
    print(Border)
    print("Step 7 : Train the Model")
    print(Border)

    model = model.fit(X_train_Scaled,Y_train)
    print("Model Training Completed")



    ##############################################
    # Step 8 : Test the Model & Accuracy
    ##############################################
    print(Border)
    print("Step 8 : Test the Model & Accuracy")
    print(Border)  
    
    Y_pred = model.predict(X_test_scaled)
    accuracy = accuracy_score(Y_test,Y_pred)
    print("Model Accuracy is :", accuracy * 100)




def main():
    MarvellousClassifier("WinePredictor.csv")


if __name__ == "__main__":
    main()