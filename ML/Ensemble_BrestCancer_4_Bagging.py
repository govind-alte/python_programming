import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import BaggingClassifier
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
from sklearn.tree import DecisionTreeClassifier



#step 1 load the data set------------------------------------------------------------ 

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

#splite the dataset-------------------------------------------------------------------
print("Splite dataset for  training and testing ")
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)

#scale the dataset--------------------------------------------------------------------
print("Scale the featuers")
scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.fit_transform(X_test)

#--------------------------------------------------------------------------------------
#create bagging model 
print("Create the base model ")
base_model=DecisionTreeClassifier(random_state=42)

print("Create the bagging ")
model=BaggingClassifier(estimator=base_model,n_estimators=10,random_state=42)

#--------------------------------------------------------------------------------------

print("Trasin model")
model=model.fit(X_train,Y_train)

#--------------------------------------------------------------------------------------
print("Test the model ")
Y_pred=model.predict(X_test)
#--------------------------------------------------------------------------------------

print("Evaluate gthe model ")

print("accuracy_score:",accuracy_score(Y_test,Y_pred))
print("Confusion metricx")
print(confusion_matrix(Y_test,Y_pred))






