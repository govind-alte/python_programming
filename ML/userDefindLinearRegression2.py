import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def marvellousPredictor():
    #load data
    X=[1,2,3,4,5]
    Y=[3,4,2,4,5]
    print("values  of independent variable",X)
    print("values  of dependent variable",Y)


    mean_x=np.mean(X)#this line direct use numpy calculation 
    mean_y=np.mean(Y) 

    print("mean_x is:",mean_x)
    print("mean_y is:",mean_y)


def main():
    marvellousPredictor()

if __name__=="__main__":
    main()
