import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.ensemble import BaggingRegressor



#----------------------------------------------
#step 1 load the dataset
#------------------------------------------
print("load tghe dataset")
df=pd.read_csv("california_housing.csv")
print("shape of dataset :",df.shape)

print(df.head())




#----------------------------------------------
#step 2 seperate feastures and labels 
#------------------------------------------
print("seperate feastures and labels ")

X=df.drop("target",axis=1)
Y=df["target"]
print("shape of X :",X.shape)
print("shape of Y :",Y.shape)


print("splite dataset for training and testing ")
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)

print("create the base_model")
base_model=DecisionTreeRegressor(random_state=42)

print("train the model ")
model=BaggingRegressor(random_state=42,estimator=base_model,n_estimators=10)

model=model.fit(X_train,Y_train)


print("testing the model ")
Y_pred=model.predict(X_test)

print("evaluate the model ")
print("MSE:",mean_squared_error(Y_pred,Y_test))
print("R2:",r2_score(Y_test,Y_pred))


