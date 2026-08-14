import pandas as pd
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay
)

Border = "-"*70
# ============================================================
# Dataset Loading
# ============================================================

print(Border)
print("Load the Dataset")
print(Border)

Datapath = "student_performance_ml.csv"
df = pd.read_csv(Datapath)

# ============================================================
# Q1. Decision Tree Model Training
# ============================================================

print(Border)
print("Decision Tree Model Training")
print(Border)

feature_columns = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
]

X = df[feature_columns]
Y = df["FinalResult"]

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.20,random_state = 42)

model = DecisionTreeClassifier()
model.fit(X_train,Y_train)
print("Decision Tree model trained successfully.","\n")

# ============================================================
# Q2. Prediction
# ============================================================

print(Border)
print("Prediction")
print(Border)

Y_pred = model.predict(X_test)
print("Predicted Values :",Y_pred,"\n")
print("Actual Values    :",Y_test.values,"\n")


# ============================================================
# Q3. Accuracy
# ============================================================

print(Border)
print("Model Accuracy")
print(Border)

accuracy = accuracy_score(Y_test,Y_pred) * 100
print(f"Model Accuracy: {accuracy :.2f}%")

# ============================================================
# Q4. Confusion Matrix
# ============================================================

print(Border)
print("Confusion Matrix")
print(Border)

cm = confusion_matrix(Y_test,Y_pred)
print("Confusion Matrix  :",cm)

cm_display = ConfusionMatrixDisplay(
    confusion_matrix = cm, 
    display_labels = ["Fail","Pass"]
)

cm_display.plot()

print("\nTrue Positive (TP): Actual Pass and Predicted Pass.")
print("True Negative (TN): Actual Fail and Predicted Fail.")
print("False Positive (FP): Actual Fail but Predicted Pass.")
print("False Negative (FN): Actual Pass but Predicted Fail.")

plt.show()


# ============================================================
# Q5. Training Accuracy vs Testing Accuracy
# ============================================================

print("\n" + Border)
print("Training Accuracy vs Testing Accuracy")
print(Border)

train_prediction = model.predict(X_train)
train_accuracy = accuracy_score(Y_train,train_prediction) * 100

testing_prediction = model.predict(X_test)
testing_accuracy = accuracy_score(Y_test,testing_prediction) * 100

print(f"Training Accuracy: {train_accuracy:.2f}%")
print(f"Testing Accuracy : {testing_accuracy:.2f}%")

print("--                           Observation                           --")
if train_accuracy > testing_accuracy:
    print("Training accuracy is higher than testing accuracy.")
if train_accuracy - testing_accuracy > 10:
    print("The model may be overfitting.")
elif testing_accuracy > train_accuracy:
    print("The model may be underfitting.")
else:
    print("Training and testing accuracies are relatively close.")


# ============================================================
# Q6. max_depth Comparison
# ============================================================

print("\n" + Border)
print("Max Depth Comparison")
print(Border)


model_depth1 = DecisionTreeClassifier(max_depth = 1)
model_depth1.fit(X_train,Y_train)
predict_model1 = model_depth1.predict(X_test)
accuracy_depth1 = accuracy_score(Y_test,predict_model1)* 100

model_depth3 = DecisionTreeClassifier(max_depth = 3)
model_depth3.fit(X_train,Y_train)
predict_model3 = model_depth3.predict(X_test)
accuracy_depth3 = accuracy_score(Y_test,predict_model3)* 100



model_depth_none = DecisionTreeClassifier(max_depth = None)
model_depth_none.fit(X_train,Y_train)
predict_model_none = model_depth_none.predict(X_test)
accuracy_depth_none = accuracy_score(Y_test,predict_model_none)* 100

print(f"max_depth = 1    : {accuracy_depth1:.2f}%")
print(f"max_depth = 3    : {accuracy_depth3:.2f}%")
print(f"max_depth = None : {accuracy_depth_none:.2f}%")



# ============================================================
# Q7. New Student Prediction
# ============================================================

print("\n" + Border)
print("New Student Prediction")
print(Border)


new_student = pd.DataFrame(
    {
        "StudyHours" : [6],
        "Attendance":[85],
        "PreviousScore":[66],
        "AssignmentsCompleted":[7],
        "SleepHours":[7]       
    }
)
new_prediction = model.predict(new_student)

print("\nNew Student Details:",new_student)

if new_prediction[0] == 1:
    print("\nPrediction: PASS")
else:
    print("\nPrediction: FAIL")
    
# ============================================================
# Q8. Final Conclusion
# ============================================================

print("\n" + Border)
print("Final Conclusion")
print(Border)

print("Decision Tree Classifier was trained using the student performance dataset.")
print("The model was used to predict results for the test data.")
print(f"The testing accuracy of the model is {testing_accuracy:.2f}%.")
print("A confusion matrix was generated to analyze correct and incorrect predictions.")
print("Training and testing accuracy were compared.")
print("Different max_depth values were tested and compared.")
print("Finally, the model was used to predict the result of a new student.")
    
