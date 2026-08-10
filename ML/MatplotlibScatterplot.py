import matplotlib.pyplot as plt

def main():
    Study_hours=[1,2,3,4,5,6]
    marks=[35,42,50,62,72,85]
    plt.scatter(
        Study_hours,
        marks,
        s=100,
        marker="o",
        alpha=1.0,
        edgecolors="black",
        label="Student"
    )
    plt.title("marvellous scatter")
    plt.xlabel("Study_hours")
    plt.ylabel("marks")
    plt.grid(True)
    plt.legend()
    plt.show()
    

if __name__=="__main__":
    main()