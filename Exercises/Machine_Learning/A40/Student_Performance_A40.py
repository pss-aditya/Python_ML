import pandas as pd 
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix   
)

Border = "-"*70

###########################################
# Step 1 : Load the Dataset
###########################################

print(Border)
print("Load the Dataset")
print(Border)

Datapath = "student_performance_ml.csv"
df = pd.read_csv(Datapath)

###########################################
# Step 2 : Model Selection
###########################################
print(Border)
print("Model Selection")
print(Border)

features_col = [   
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
]
X = df[features_col]
Y = df["FinalResult"]

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.20,random_state=42)

#1.Initialize the model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train,Y_train)

#2. Extract feature importance array
important = model.feature_importances_

#3. Match scores with column name and sort
feature_importance_df = pd.DataFrame({
    'Features' : X_train.columns,
    'Importance' : important
}).sort_values(by='Importance', ascending = False)

print("Feature Importance is :", feature_importance_df)

#Most Important Feature
most_important = feature_importance_df.iloc[0]
print("\nMost Important Feature :")
print(
    f"{most_important['Features']} " 
    f"({most_important['Importance']:.2f})"
)

#Least Important Feature
least_important_feature = feature_importance_df['Importance'].min()
least_importance = feature_importance_df[feature_importance_df["Importance"] == least_important_feature]
print("\nLeast Important Feature(s):")

for feature in least_importance["Features"]:
    print(f"{feature} ({least_important_feature:.2f})")

########################################################
# Q2  : Remove the column SleepHours from the dataset.
#     - Train the model again
#     - Compare new accuracy with previous accuracy
#     - Does removing this feature affect performance?
########################################################

print(Border)
print("Removed SleepHours Feature")
print(Border)


X_reduced = X.drop(
    columns = ["SleepHours"]
)

# Split the reduced dataset
X_train_reduced,X_test_reduced,Y_train_reduced,Y_test_reduced = train_test_split(X_reduced,Y,test_size =0.2,random_state = 42)

# Train the model again
reduced_model = DecisionTreeClassifier(random_state=42)
reduced_model.fit(X_train_reduced,Y_train_reduced)

# Prediction
reduced_prediction = reduced_model.predict(X_test_reduced)

# New accuracy
reduced_accuracy = accuracy_score(Y_test_reduced,reduced_prediction)*100

# Original model accuracy
original_prediction = model.predict(X_test)
original_accuracy = accuracy_score(Y_test,original_prediction) *100

print(f"\nOriginal Accuracy : {original_accuracy:.2f}%")
print(f"Reduced Accuracy  : {reduced_accuracy:.2f}% \n")

print("--                       Observation                           --")

if reduced_accuracy > original_accuracy:
    print("Accuracy increased after removing SleepHours..")

elif reduced_accuracy < original_accuracy:
    print("Accuracy decreased after removing SleepHours.")

else:
    print("Accuracy remained the same after removing SleepHours.")

#######################################################################################################
# Q3 : Train the model using only
#    - StudyHours
#    - Attendance
#    - Compare the accuracy with the full-feature model. Is the model still performing well?
#######################################################################################################

print(Border)
print("StudyHours and Attendance Model")
print(Border)

# Select only StudyHours and Attendance
X_selected = df[
    [
        "StudyHours",
        "Attendance"
    ]
]

# Split the selected features
X_train_selected,X_test_selected,Y_train_selected,Y_test_selected = train_test_split(X_selected,Y,test_size=0.20,random_state=42)

# Initialize and train the model
selected_model = DecisionTreeClassifier(random_state=42)
selected_model.fit(X_train_selected,Y_train_selected)

# Prediction
selected_prediction = selected_model.predict(X_test_selected)

# Accuracy of selected-feature model
selected_accuracy = accuracy_score(Y_test_selected,selected_prediction)*100

# Compare with full-feature model
print(f"\nFull Feature Model Accuracy : {original_accuracy:.2f}%")
print(f"StudyHours + Attendance Accuracy : {selected_accuracy:.2f}%")