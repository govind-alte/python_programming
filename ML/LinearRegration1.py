import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def marvellousPredictor():
    #load data
    X=[1,2,3,4,5]
    Y=[3,4,2,4,5]
    print("values  of independent variable",X)
    print("values  of dependent variable",Y)

    Sum_x=0
    Sum_y=0
    for i in range(len(X)):
        Sum_x=Sum_x+X[i]#0+15
        Sum_y=Sum_y+Y[i]#0+15

    mean_x=Sum_x/len(X) #15/5=0.3
    mean_y=Sum_y/len(Y) #15/5=3.6  

    print("mean_x is:",mean_x)
    print("mean_y is:",mean_y)


def main():
    marvellousPredictor()

if __name__=="__main__":
    main()
