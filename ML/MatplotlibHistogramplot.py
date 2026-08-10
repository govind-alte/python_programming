import matplotlib.pyplot as plt

def main():
    marks=[45,55,60,62,67,70,72,75,78,80,85,90,92]
    plt.hist(

        marks,
        bins=5,  #number of group
        edgecolor="black",
        alpha=0.8,
        rwidth=0.9#relative width of bars

    )
    plt.title("Histogram")
    plt.xlabel("marks")
    plt.ylabel("frequncy")
    plt.show()
    plt.
    

if __name__=="__main__":
    main()