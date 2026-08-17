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

def main():
    Loaddata("MarvellousTitanicDataset.csv")
    pass
if __name__=="__main__":
    main()
