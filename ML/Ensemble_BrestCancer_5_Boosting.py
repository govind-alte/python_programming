import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
from sklearn.ensemble import AdaBoostClassifier





#step 1 load the data set 

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

print("splite dataset for  training and testing ")
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)

#-------------------------------------------------------------------------------

print("scale the featuers")
scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.fit_transform(X_test)
#-----------------------------------------------------------------------------
print("Create the Boosting  model ")
model=AdaBoostClassifier(n_estimators=50,learning_rate=1.0,random_state=42)

#-----------------------------------------------------------------------------

print("Trasin model")
model=model.fit(X_train,Y_train)

#-----------------------------------------------------------------------------
print("Test the model ")
Y_pred=model.predict(X_test)
#-----------------------------------------------------------------------------

print("Evaluate gthe model ")

print("accuracy_score:",accuracy_score(Y_test,Y_pred))
print("confusion metricx")
print(confusion_matrix(Y_test,Y_pred))






