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


    # step 2 remove unwanted columns--------------------------------------------
    print(border)
    print("step 2 remove unwanted columns ")
    print(border)

    if "Unnamed: 0" in df.columns:
        df=df.drop(columns=["Unnamed: 0"])

    print(df.head())

    #step 3: missing value ------------------------------------------------------
    print(border)
    print("step 3 check missing value  ")
    print(border)

    print("Total missing value :")
    print(df.isnull().sum())

    #step 4  : statistical summery-------------------------------------------------------------
    print
    (border)
    print("step 4  : statistical summery")
    print(border)

    print(df.describe())


     #step 5 : Correlation------------------------
    print(border)
    print("step 5 : Correlation")
    print(border)
    print(df.corr())

    #step 6 : splite independent and dependent variavle------------------------
    print(border)
    print("step 6 : seprate independent and dependent variavle ")
    print(border)

    X=df[["TV","radio","newspaper"]]
    Y=df["sales"]
    print("independent variable :")
    print(X.head())
    print("dependent variable :")
    print(Y.head())

    #step 7 : splite dataset----------------------------------
    print(border)
    print("step 7 : splite dataset ")
    print(border)

    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,train_size=0.2,random_state=42)

    print("Training data :",X_train.shape)
    print("data:",X_test.shape)

    #step 8 : splite dataset------------------------------------------------
    print(border)
    print("step 8 : Create and train model  ")

    print(border)
    model=LinearRegression()
    model=model.fit(X_train,Y_train)
    print("Model train Sucessfully")

    #step 9 : splite dataset--------------------------------------------------------
    print(border)
    print("step 9 : Test the model  ")
    print(border)

    Y_pred=model.predict(X_test)
    print("Expected answer :")
    print(Y_test[:3])

    print("Predicted  answer :")
    print(Y_pred[:3])
    




        



    




def main():
    marvellousRegression("Advertising.csv")
if  __name__=="__main__":
    main()

