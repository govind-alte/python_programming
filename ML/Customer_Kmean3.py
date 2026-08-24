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


    print("step 2 feature selection")
    X=df[["AnnualIncome","SpendingScore"]]
    print("selected features:")
    print(X.head())


    print("step 3 scale the data")
    scalar=StandardScaler()
    X_scaled=scalar.fit_transform(X)
    print("scaled data")
    print(X_scaled[:5])
    
if __name__=="__main__":
    main()
