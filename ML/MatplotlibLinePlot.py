import matplotlib.pyplot as plt

def main():
    X=[1,2,3,4,5]
    Y=[10,25,18,35,30]
    plt.plot(
        X,    #value of x 
        Y,
        marker="o",
        linestyle="--",
        linewidth=3,
        markersize=7,
        label="Marks"
        )
    
    plt.title("marvellous line plot")
    plt.xlabel("student number ")
    plt.ylabel("Mark")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__=="__main__":
    main()