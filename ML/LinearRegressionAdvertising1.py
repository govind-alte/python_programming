import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score


def marvellousRegression(datapath):
    border="-"*40
    #step 1 load the data ------------------------------------------------
    print(border)
    print("step 1 load the data ")
    print(border)

    df=pd.read_csv(datapath)

    print(df.head())

    




def main():
    marvellousRegression("Advertising.csv")
if  __name__=="__main__":
    main()

