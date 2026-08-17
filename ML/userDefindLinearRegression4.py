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
        Sum_x=Sum_x+X[i]
        Sum_y=Sum_y+Y[i]

    mean_x=Sum_x/len(X) 
    mean_y=Sum_y/len(Y)   

    print("mean_x is:",mean_x)
    print("mean_y is:",mean_y)


    n=len(X)#5
    numerator=0
    denomerator=0


    #calculate slope M value
    for i in range(n):
        numerator=numerator+((X[i]-mean_x)*(Y[i]-mean_y))
        denomerator=denomerator+((X[i]-mean_x)**2)

    m=numerator/denomerator
    print("slope of line M is ",m)  

    #-----------------------------------------------------------------------
    # c value 
    # y=mx+c
    # c=y-mx  
    #c= ymean - m * xmean

    C=mean_y-m*mean_x  # 3.6-0.4*0.3=2.4
    print("Y intercept that is C ",C)


def main():
    marvellousPredictor()

if __name__=="__main__":
    main()
