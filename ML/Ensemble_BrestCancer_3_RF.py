import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

#use the random forestclassifire
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score,classification_report,confusion_matrix



#step 1 load the dataset------------------------------------------------------ 

print("load the dataset")
df=pd.read_csv("breast_cancer.csv")
print("shape of dataset :",df.shape)
print("first record")
print(df.head())


#-------------------------------------------------
#step 2 sepefrate featueres and labels 
#-------------------------------------------------

print("festures and labels")

X=df.drop("target",axis=1)
Y=df["target"]

print("x shape:",X.shape)
print("x shape:",X.shape)

#step 3 : splite dataset--------------------------------------------------------
print("splite dataset for  training and testing ")
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)


#step 4: scaled the feature-----------------------------------------------------
print("scale the featuers")
scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.fit_transform(X_test)

#step 5: create the model--------------------------------------------------------
print("crate the model ")
model=RandomForestClassifier(n_estimators=10,random_state=42) 

# train the model ---------------------------------------------------------------
print("trasin model")
model=model.fit(X_train,Y_train)

#test the model -----------------------------------------------------------------
print("test the model ")
Y_pred=model.predict(X_test)

#Evaluate the model--------------------------------------------------------------
print("Evaluate the model ")
print("accuracy_score:",accuracy_score(Y_test,Y_pred))
print("confusion metricx")
print(confusion_matrix(Y_test,Y_pred))






