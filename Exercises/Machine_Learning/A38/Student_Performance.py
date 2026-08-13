import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def main():

    # ============================================================
    # Q1. Load the dataset and display basic information
    # ============================================================

    df = pd.read_csv("student_performance_ml.csv")

    print("\n========== Q1: DATASET INFORMATION ==========")

    # First 5 records
    print("\nFirst 5 records:")
    print(df.head())

    # Last 5 records
    print("\nLast 5 records:")
    print(df.tail())

    # Number of rows and columns
    print("\nNumber of rows and columns:")
    print(df.shape)

    # Column names
    print("\nColumn names:")
    print(df.columns.tolist())

    # Data types
    print("\nData types:")
    print(df.dtypes)


    # ============================================================
    # Q2. Total students, Passed students, Failed students
    # ============================================================

    print("\n========== Q2: PASS / FAIL COUNT ==========")

    total_students = len(df)

    passed_students = (df["FinalResult"] == 1).sum()

    failed_students = (df["FinalResult"] == 0).sum()

    print("Total students :", total_students)
    print("Passed students:", passed_students)
    print("Failed students:", failed_students)


    # ============================================================
    # Q3. Statistical calculations
    # ============================================================

    print("\n========== Q3: STATISTICAL ANALYSIS ==========")

    average_study_hours = df["StudyHours"].mean()
    average_attendance = df["Attendance"].mean()
    maximum_previous_score = df["PreviousScore"].max()
    minimum_sleep_hours = df["SleepHours"].min()

    print("Average StudyHours       :", average_study_hours)
    print("Average Attendance       :", average_attendance)
    print("Maximum PreviousScore    :", maximum_previous_score)
    print("Minimum SleepHours       :", minimum_sleep_hours)


    # ============================================================
    # Q4. FinalResult distribution
    # ============================================================

    print("\n========== Q4: FINAL RESULT DISTRIBUTION ==========")

    result_counts = df["FinalResult"].value_counts()

    print("\nFinalResult counts:")
    print(result_counts)

    result_percentages = df["FinalResult"].value_counts(normalize=True) * 100

    pass_percentage = result_percentages.get(1, 0)
    fail_percentage = result_percentages.get(0, 0)

    print("\nPass percentage:", pass_percentage, "%")
    print("Fail percentage:", fail_percentage, "%")

    difference = abs(pass_percentage - fail_percentage)

    print("Difference between Pass and Fail:", difference, "%")

    print("\nObservation:")

    if difference <= 10:
        print("The dataset is approximately balanced because the Pass and Fail percentages are close.")
    else:
        print("The dataset is not balanced because there is a noticeable difference between Pass and Fail percentages.")


    # ============================================================
    # Q5. StudyHours and Attendance vs FinalResult
    # ============================================================

    print("\n========== Q5: STUDY HOURS & ATTENDANCE ANALYSIS ==========")

    average_by_result = df.groupby("FinalResult")[
        ["StudyHours", "Attendance"]
    ].mean()

    print("\nAverage StudyHours and Attendance by FinalResult:")
    print(average_by_result)

    pass_avg_study = average_by_result.loc[1, "StudyHours"]
    fail_avg_study = average_by_result.loc[0, "StudyHours"]

    pass_avg_attendance = average_by_result.loc[1, "Attendance"]
    fail_avg_attendance = average_by_result.loc[0, "Attendance"]

    print("\nObservations:")

    if pass_avg_study > fail_avg_study:
        print("1. Students who passed have higher average StudyHours than students who failed.")
    else:
        print("1. Students who passed do not have higher average StudyHours than students who failed.")

    if pass_avg_attendance > fail_avg_attendance:
        print("2. Students who passed have higher average Attendance than students who failed.")
    else:
        print("2. Students who passed do not have higher average Attendance than students who failed.")

    print("3. StudyHours shows the difference in average study time between Pass and Fail groups.")
    print("4. Attendance shows the difference in average attendance between Pass and Fail groups.")
    print("5. These observations describe relationships in this dataset; they do not prove causation.")


    # ============================================================
    # Q6. Histogram of StudyHours
    # ============================================================

    print("\n========== Q6: HISTOGRAM ==========")

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

    print("\nHistogram Observation:")
    print("The histogram shows how StudyHours are distributed among the students.")
    print("The height of each bar represents the number of students in that range of study hours.")


    # ============================================================
    # Q7. Scatter plot: StudyHours vs PreviousScore
    # Different colors for Pass and Fail
    # ============================================================

    print("\n========== Q7: SCATTER PLOT ==========")

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

    print("\n========== Q8: BOXPLOT ==========")

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

    print("\nAttendance Q1:", Q1)
    print("Attendance Q3:", Q3)
    print("IQR:", IQR)

    print("\nLower limit:", lower_limit)
    print("Upper limit:", upper_limit)

    print("\nNumber of outliers:", len(outliers))

    if len(outliers) > 0:
        print("Outliers are present in Attendance.")
        print("\nOutlier values:")
        print(outliers["Attendance"].tolist())
    else:
        print("No outliers are present in Attendance.")


    # ============================================================
    # Q9. AssignmentsCompleted vs FinalResult
    # ============================================================

    print("\n========== Q9: ASSIGNMENTS vs FINAL RESULT ==========")

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

    print("\nAverage AssignmentsCompleted by FinalResult:")
    print(assignment_average)

    if assignment_average.loc[1] > assignment_average.loc[0]:
        print("\nObservation:")
        print("Students who passed completed more assignments on average than students who failed.")
    else:
        print("\nObservation:")
        print("Students who passed did not complete more assignments on average than students who failed.")


    # ============================================================
    # Q10. SleepHours vs FinalResult
    # ============================================================

    print("\n========== Q10: SLEEP HOURS vs FINAL RESULT ==========")

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

    print("\nAverage SleepHours by FinalResult:")
    print(sleep_average)

    print("\nObservation:")

    if sleep_average.loc[1] > sleep_average.loc[0]:
        print("Students who passed have higher average SleepHours than students who failed.")
    elif sleep_average.loc[1] < sleep_average.loc[0]:
        print("Students who passed have lower average SleepHours than students who failed.")
    else:
        print("Both groups have the same average SleepHours.")

    print("\nSleeping more does not automatically guarantee success.")
    print("SleepHours and FinalResult show a relationship in the dataset,")
    print("but success depends on multiple factors.")


if __name__ == "__main__":
    main()