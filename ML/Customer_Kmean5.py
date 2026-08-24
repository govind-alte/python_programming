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


    #step4
    print("elbow method")
    WCSS=[]

    for k in range(1,11):
        model=KMeans(n_clusters=k,random_state=42,n_init=10)
        model.fit(X_scaled)
        WCSS.append(model.inertia_)
    print("values of wcss :")
    for i in range(len(WCSS)):
        print(f"{i+1}:{WCSS[i]}")


    #step 5 :
    print("Vsualization")
    plt.plot(range(1,11),WCSS,marker="o")
    plt.xlabel("number of clusters")
    plt.ylabel("wcss")
    plt.title("elbow method")
    plt.grid(True)
    plt.show()    

    
if __name__=="__main__":
    main()
