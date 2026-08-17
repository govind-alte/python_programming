import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import joblib 
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix


#
#   Function name : Loaddata
#   description : load the data from csv
#   input : name of csv file
#   output:  data freame
#   Author : Alte govind jagannath
#   date : 16/08/2026


def Loaddata(filename):
    df=pd.read_csv(filename)
    print("dataset loaded sucessfully")
    print(df.head())
    return df

#   Function name : Loaddata
#   description : load the data from csv
#   input : none
#   output:  none
#   Author : Alte govind jagannath
#   date : 16/08/2026

#-------step 2 :-----------------------------------------------------------------------------------
#   Function name  : preProcess data
#   description    : data analysis
#   input          : dataframe
#   output         :  updated dataframe 
#   Author         : Alte govind jagannath
#   date           : 16/08/2026

def PreprocessData(df):

    df=df.drop([
        "Passengerid",
        "zero",
        "name"
    ],errors="ignore")

    # handal missing values 
    df["Age"]=df["Age"].fillna(df["Age"].median())
    df["fare"]=df["Fare"].fillna(df["Fare"].median())
    df["Embarked"]=df["Embarked"].fillna(df["Embarked"].mode()[0])

    #convert catagorical to numeric
    df=pd.get_dummies(
        df,
        columns=["Embarked"],
        drop_first=True,
        dtype=int
    )
    print(df.head())

    print("data preprocessing complite")


    return df





def main():
    #step 1
    df=Loaddata("MarvellousTitanicDataset.csv")

    #step 2
    df=PreprocessData(df)
    
if __name__=="__main__":
    main()
