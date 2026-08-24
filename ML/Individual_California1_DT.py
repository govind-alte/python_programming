import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error,r2_score



#----------------------------------------------
#load the dataset
#----------------------------------------------
print("load tghe dataset")
df=pd.read_csv("california_housing.csv")
print("shape of dataset :",df.shape)
print(df.head())

#----------------------------------------------
#seperate feastures and labels 
#----------------------------------------------
print("seperate feastures and labels ")
X=df.drop("target",axis=1)
Y=df["target"]
print("shape of X :",X.shape)
print("shape of Y :",Y.shape)

#Splite dataset------------------------------------------------------------------
print("splite dataset for training and testing ")
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)

#Create the model----------------------------------------------------------------
print("Create the model")
model=DecisionTreeRegressor(random_state=42)

#Train the model-----------------------------------------------------------------
print("Train the model ")
model=model.fit(X_train,Y_train)

#Test the model------------------------------------------------------------------
print("Testing the model ")
Y_pred=model.predict(X_test)

#Evaluate the model--------------------------------------------------------------
print("Evaluate the model ")
print("MSE:",mean_squared_error(Y_pred,Y_test))
print("R2:",r2_score(Y_test,Y_pred))


