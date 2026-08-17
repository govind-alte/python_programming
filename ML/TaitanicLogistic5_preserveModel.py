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


#-------step 3 :-----------------------------------------------------------------------------------
#   Function name  : SpliteData
#   description    : spliting activity
#   input          : dataframe
#   output         : 4 subsate fro training  and testing
#   Author         : Alte govind jagannath
#   date           : 16/08/2026

def SplitData(df):
    X=df.drop("Survived",axis=1)
    Y=df["Survived"]

    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)

    print("data set spliting competed sucessfully")

    return   X_train,X_test,Y_train,Y_test



#-------step 4 :-----------------------------------------------------------------------------------
#   Function name  : TrainModel
#   description    : perform model
#   input          : training farture and label
#   output         : train model
#   Author         : Alte govind jagannath
#   date           : 16/08/2026

def TrainModel(X_train,Y_train):
    model=LogisticRegression(max_iter=1000)
    model=model.fit(X_train,Y_train)
    print("model train sucessfully")
    return model



#-------step 5:-----------------------------------------------------------------------------------
#   Function name  : EvaluateModel
#   description    : it perform model testing
#   input          : training data ,model(faetures,label)
#   output         : none
#   Author         : Alte govind jagannath
#   date           : 16/08/2026

def EvaluateModel(model,X_test,Y_test):
    Y_pred=model.predict(X_test)
    accuracy=accuracy_score(Y_test,Y_pred)
    print("Accuracy: ",accuracy)

    print(confusion_matrix(Y_test,Y_pred))
#--------------------------------------------------------------------------------------------------------------

    #-------step 6:-----------------------------------------------------------------------------------
#   Function name  : PreserveModel
#   description    : it perform model preservation into .pkl file
#   input          : model
#   output         : none
#   Author         : Alte govind jagannath
#   date           : 16/08/2026

def PreserveModel(model,filename):
    joblib.dump(model,filename)
    print("model preserve with name :",filename)


def main():
    #step 1
    df=Loaddata("MarvellousTitanicDataset.csv")

    #step 2
    df=PreprocessData(df)

    #step 3
    X_train,X_test,Y_train,Y_test=SplitData(df)

    #step 4  
    model=TrainModel(X_train,Y_train)

    #step 5
    EvaluateModel(model,X_test,Y_test)

    #Step 6
    PreserveModel(model,"marvellousTitanic.pkl")
    
if __name__=="__main__":
    main()
