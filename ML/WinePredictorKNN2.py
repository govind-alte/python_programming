
import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier    #algoriyham
from sklearn.metrics import accuracy_score,confusion_matrix  #FT FN TP TN
from sklearn.preprocessing import StandardScaler 

def marvellousclassifire(datapath):
    border="-"*40
    print(border)
    print("step 1 load the dataset from csv")
    print(border)

    df=pd.read_csv(datapath)

    print(border)
    print("some entries from dataset")
    print(df.head())
    print(border)



   #step 2  clean the data set ####################################################3
    
    print(border)
    print("step 2 : clean the dataset  ")
    print(border)

    df.dropna(inplace=True)
    print("shape of dataser :",df.shape)
    print("total records:",df.shape[0])
    print("total columns:",df.shape[1])
    print(border)



    


def main():
    marvellousclassifire("WinePredictor.csv")
if __name__=="__main__":
    main()
