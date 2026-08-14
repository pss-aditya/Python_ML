import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



Border = "-"*70

# ============================================================
# Q1. Load the dataset and display basic information
# ============================================================


print(Border)
print("Load the dataset")
print(Border)

df = pd.read_csv("student_performance_ml.csv")

print("\nFirst 5 records :")
print(df.head())

print("\nLast 5 records :")
print(df.tail())

print("\nTotal number of rows and columns :")
print(df.shape)

print("\nList of column names :")
print(df.columns.tolist())

print("\nData types of each column :")
print(df.dtypes,"\n")


# ============================================================
# Q2. Total students, Passed students, Failed students
# ============================================================

print(Border)
print("Total students, Passed students, Failed students")
print(Border)

passStudents = (df["FinalResult"] == 1).sum()
failedStudents = (df["FinalResult"] == 0).sum()

print("\nTotal number of Rows in Dataset :", len(df))  
print("\nCount of Passed Student is      :", passStudents)
print("\nCount of Failed Student is      :", failedStudents,"\n") 


# ============================================================
# Q3. Statistical calculations
# ============================================================

print(Border)
print("Statistical calculations")
print(Border)

AverageStudyHour = df['StudyHours'].mean()
AverageAttendance = df['Attendance'].mean()
Max_PreviousScore = df['PreviousScore'].max()
Min_SleepHours = df['SleepHours'].min()

print(f"Average Study Hours of Student is    : {AverageStudyHour}""\n")
print(f"Average Attendance of Student is     : {AverageAttendance}""\n")
print(f"Maximum PreviousScore of Student is  : {Max_PreviousScore}""\n")
print(f"Minimum Sleep Hour of Student is     : {Min_SleepHours}""\n")


# ============================================================
# Q4. FinalResult distribution
# ============================================================

print(Border)
print("Final Result Distribution")
print(Border)   

result_count = df['FinalResult'].value_counts()
total_students = len(df)
pass_count = result_count.get(1,0)
fail_count = result_count.get(0,0)
pass_percentage = pass_count/total_students * 100
fail_percentage = fail_count/total_students * 100
difference = abs (pass_percentage - fail_percentage)

print(f"Pass Students Percentage is          : {pass_percentage}\n")
print(f"Fail Students Percentage is          : {fail_percentage}\n")
print(f"Difference in Students Percentage is : {difference}\n")

print("--                          Observation is                         --")
if difference <= 10:
    print("-->   The Difference is close so we can say Dataset is balanced   <--""\n")
else:
    print("-->    The Difference is Huge so we can say it is not balanced    <--""\n")
    
    
# ============================================================
# Q5. StudyHours and Attendance vs FinalResult
# ============================================================

print(Border)
print("StudyHours and Attendance vs FinalResult")
print(Border) 

study_result = df.groupby("StudyHours")["FinalResult"].mean() * 100
attendance_result = df.groupby("Attendance")["FinalResult"].mean() * 100

study_result = study_result.map(lambda x: f"{x:.0f}%")
attendance_result = attendance_result.map(lambda x: f"{x:.0f}%")

print(f"Pass percentage according to StudyHours : {study_result}\n")
print(f"Pass percentage according to Attendance : {attendance_result}\n")

print("--                                   Observation                          --")
print("1. Students with StudyHours up to 4.0 have a 0% observed pass rate, while students with 4.2 or more StudyHours have a 100% observed pass rate.")
print("2. This indicates that higher StudyHours are strongly associated with passing in this dataset.")
print("3. Students with Attendance up to 75% have a 0% observed pass rate, while students with 76% or higher Attendance have a 100% observed pass rate.")
print("4. This indicates that higher Attendance is strongly associated with better FinalResult in this dataset.")



# ============================================================
# Q6. Histogram of StudyHours
# ============================================================

print(Border)
print("Histogram of StudyHours")
print(Border) 

plt.figure(figsize=(8, 5))

plt.hist(
    df["StudyHours"],
    bins=10,
    edgecolor="black"
)

plt.xlabel("Study Hours")
plt.ylabel("Frequency")
plt.title("Distribution of Study Hours")

plt.show()

print("--                         Histogram Observation                         --")
print("The histogram shows how StudyHours are distributed among the students.")
print("The height of each bar represents the number of students in that range of study hours.")


# ============================================================
# Q7. Scatter plot: StudyHours vs PreviousScore
# Different colors for Pass and Fail
# ============================================================

print(Border)
print("Scatter plot")
print(Border) 

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x="StudyHours",
    y="PreviousScore",
    hue="FinalResult"
)

plt.xlabel("Study Hours")
plt.ylabel("Previous Score")
plt.title("Study Hours vs Previous Score")

plt.show()


# ============================================================
# Q8. Boxplot of Attendance
# Identify outliers
# ============================================================

print(Border)
print("Boxplot of Attendance")
print(Border) 

plt.figure(figsize=(8, 5))

sns.boxplot(
    y=df["Attendance"]
)

plt.ylabel("Attendance")
plt.title("Attendance Boxplot")

plt.show()

# Calculate IQR and identify outliers
Q1 = df["Attendance"].quantile(0.25)
Q3 = df["Attendance"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = df[
    (df["Attendance"] < lower_limit) |
    (df["Attendance"] > upper_limit)
]

print("\nAttendance Q1       :", Q1)
print("Attendance Q3         :", Q3)
print("IQR                   :", IQR)

print("\nLower limit         :", lower_limit)
print("Upper limit           :", upper_limit)

print("\nNumber of outliers  :", len(outliers))

if len(outliers) > 0:
    print("Outliers are present in Attendance.")
    print("\nOutlier values:")
    print(outliers["Attendance"].tolist())
else:
    print("No outliers are present in Attendance.")


# ============================================================
# Q9. AssignmentsCompleted vs FinalResult
# ============================================================

print(Border)
print("AssignmentsCompleted vs FinalResult")
print(Border) 


plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df,
    x="FinalResult",
    y="AssignmentsCompleted"
)

plt.xlabel("Final Result (0 = Fail, 1 = Pass)")
plt.ylabel("Assignments Completed")
plt.title("Assignments Completed vs Final Result")

plt.show()

assignment_average = df.groupby("FinalResult")[
    "AssignmentsCompleted"
].mean()

print("Average AssignmentsCompleted by FinalResult:",assignment_average, "\n")

if assignment_average.loc[1] > assignment_average.loc[0]:
    print("--                         Observation                         --")
    print("Students who passed completed more assignments on average than students who failed.")
else:
    print("--                         Observation                         --")
    print("Students who passed did not complete more assignments on average than students who failed.")


# ============================================================
# Q10. SleepHours vs FinalResult
# ============================================================

print(Border)
print("SleepHours vs FinalResult")
print(Border) 

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df,
    x="FinalResult",
    y="SleepHours"
)

plt.xlabel("Final Result (0 = Fail, 1 = Pass)")
plt.ylabel("Sleep Hours")
plt.title("Sleep Hours vs Final Result")

plt.show()

sleep_average = df.groupby("FinalResult")[
    "SleepHours"
].mean()

print("Average SleepHours by FinalResult:",sleep_average, "\n")

print("--                                      Observation                                               --")

if sleep_average.loc[1] > sleep_average.loc[0]:
    print("Students who passed have higher average SleepHours than students who failed.")
elif sleep_average.loc[1] < sleep_average.loc[0]:
    print("Students who passed have lower average SleepHours than students who failed.")
else:
    print("Both groups have the same average SleepHours.")

print("Sleeping more does not automatically guarantee success.","\n")
print("SleepHours and FinalResult show a relationship in the dataset,")

