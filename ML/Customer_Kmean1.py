import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


def main():
    #step1 load the data 

    df=pd.read_csv("Mall_Customers.csv")

    print("data set with value ")
    print(df.head())

    print("missing value ")
    print(df.isnull().sum())
    
if __name__=="__main__":
    main()
