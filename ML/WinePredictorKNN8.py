
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



    #step3 :  seprate independent and dependent variables
    print(border)
    print("step 3 : seprate independent and dependent variables")
    print(border)

    X=df.drop(columns=['Class']) #class sodun sarv ghe 
    Y=df['Class'] # fakt hech ghe 

    print("shape of x :",X.shape)
    print("shape of Y :",Y.shape)

    print(border)
    print("input columns :",X.columns.to_list())
    print("output columns: Class ")


    #step 4 :  split dataset training and testing-------------------------------------
    print(border)
    print("step 4 : split dataset training and testing")
    print(border)


    X_train,X_test, Y_train, Y_test=train_test_split(X,Y,test_size=0.5,random_state=42,stratify=Y)
    print(border)
    print("detsild of trsind and testing data")

    print("shape of X_train:",X_train.shape)
    print("shape of X_test:",X_test.shape)
    print("shape of Y_train:",Y_train.shape)
    print("shape of Y_test:",X_test.shape)



    
    #step 5 :  Feature scaling-------------------------------------
    print(border)
    print("step 5 : Feature scaling")
    print(border)

    scalar=StandardScaler()
    X_train_scaled=scalar.fit_transform(X_train)
    X_test_scaled=scalar.fit_transform(X_test)
    print("feature scaling done")
    print(border)


    #step6 hyperparameter tuning

    accuracy_score=[]
    K_values=range(1,21)


    for k in K_values:
        model= KNeighborsClassifier(n_neighbors=k)
        model=model.fit(X_train_scaled,Y_train)
        Y_pred=model.predict(X_test_scaled)
        accuracy=accuracy_score(Y_test,Y_pred)
        accuracy_score.append(accuracy)
    print("accuracy report :")
    for no in accuracy_score:
        print(no) 

    print(border)

    print("graphical representation")

    plt.figure(figsize=(8,5))
    plt.plot(K_values,accuracy_score,marker='o')
    plt.title("K value of accuracy")
    plt.xlabel("value of k")
    plt.ylabel("accracy")
    plt.grid(True)
    plt.xticks(list(K_values()))
    plt.show()       

    


def main():
    marvellousclassifire("WinePredictor.csv")
if __name__=="__main__":
    main()
