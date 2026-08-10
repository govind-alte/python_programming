import matplotlib.pyplot as plt

def main():
    language=["C","C++","Java","Python"]
    Student=[30,40,35,55]

    plt.bar(
        language,
        Student,
        width=0.6,
        edgecolor="red",
        linewidth=1,   #width of bar border 
        alpha=0.8,     # transperance 0.0 to 1.0  color light and dark
        label="Sudent"

    )
    plt.title("marvellous bar ploat ")
    plt.xlabel("languages")
    plt.ylabel("number of student")
    plt.legend() 
    plt.show()

if __name__=="__main__":
    main()