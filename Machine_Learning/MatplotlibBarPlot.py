import matplotlib.pyplot as plt

def main():
    language = ["C", "C++", "Java", "Python"]
    students = [30,40,35,55]
    plt.bar(
        language,                  # Values of X-axis
        students,                  # Values of Y-axis
        width = 0.6,               # width of bar
        edgecolor = "black",       # border colors of  bar
        linewidth = 1,             # width of bar border
        alpha = 0.8,               # transperance 0.0 to 1.0
        label = "Students"         # legend text
    )
    plt.title("Bar Plot")
    plt.xlabel("Languages")
    plt.ylabel("No. of Student")
    plt.grid(True)
    plt.legend()
    plt.show()
if __name__ == "__main__":
    main()