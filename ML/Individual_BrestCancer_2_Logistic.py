import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix



#load the data set------------------------------- 
print("load the dataset")
df=pd.read_csv("breast-cancer-wisconsin.csv")
print("shape of dataset :",df.shape)
print("first record")
print(df.head())


#-------------------------------------------------
#Seperate featueres and labels 
#-------------------------------------------------
print("festures and labels")
X=df.drop("target",axis=1)
Y=df["target"]
print("x shape:",X.shape)
print("x shape:",X.shape)


print("Splite dataset for  training and testing ")
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)



print("scale the featuers---------------------")
scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.fit_transform(X_test)

print("Create the model---------------------- ")
model=LogisticRegression(max_iter=1000) 


print("Train the model---------------------------")
model=model.fit(X_train,Y_train)


print("Test the model------------------------ ")
Y_pred=model.predict(X_test)


print("Evaluate the model----------------------")

print("accuracy_score:",accuracy_score(Y_test,Y_pred))
print("confusion metricx")
print(confusion_matrix(Y_test,Y_pred))






