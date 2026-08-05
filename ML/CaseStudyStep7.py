import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split

from sklearn .tree import DecisionTreeClassifier
Border="-"*30
#####################################
# Step 1 load data set
#####################################

print(Border)
print("step 1 load data set")
print(Border)

datapath="iris.csv"

df = pd.read_csv(datapath)
print("dataset loaded sucessfully")
print("initial emtry from dataset are:")
print(df.head())



#####################################
# Step 2 Data Analysis (EDA)
#####################################

print(Border)
print("Data Analysis...")
print(Border)


print("shape of data set:",df.shape)#shape dias
print("column names:",list(df.columns))#header of column

print("missing values par column:")
print(df.isnull().sum())#null value show 

print("class distribution (species count)")
print(df["species"].value_counts()) #column count all

print("statistical report of dataset")
print(df.describe)



#####################################
# Step 3 Deside independent and Dependent variables
#####################################

print(Border) 
print("Step 3 Deside independent and Dependent variables")
print(Border)

#  x : independent variable /features
#  Y  : Dependent variables /Labels

feature_cols=[
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)"

]

X=df[feature_cols]
Y=df["species"]

print("X shaoe ",X.shape)
print("Y shape",Y.shape)


#####################################
# Step 4 Visualisation of dataset
#####################################

print(Border)
print("Step 4 Visualisation of dataset")
print(Border)

#scater plot
plt.figure(figsize=(7,5))
for sp in df["species"].unique():
    temp=df[df["species"]==sp]
    plt.scatter(temp["petal length (cm)"],temp["petal width (cm)"],label=sp)

plt.title("marvellous")
plt.xlabel("petal length (cm)") 
plt.ylabel("petal width (cm)")  

plt.legend()
plt.grid()
plt.show()


#####################################
# Step 5 Split the data set training and testing
#####################################
print(Border)
print(" Step 5 Split the data set training and testing")
print(Border)


X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)
print("Data set spliting activity done ")

print("X:",X.shape)#(150,4)
print("Y:",Y.shape)#(150)
print("X_train :",X_train.shape)#(75,4)
print("X_test :",X_test.shape)   #(75,4)

print("Y_train :",Y_train.shape)#(75)
print("Y_test :",Y_test.shape)#(75)


#####################################
# Step 6 Build the Model 
#####################################

print(Border)
print("Build the model")
print(Border)

model=DecisionTreeClassifier(max_depth=5)

print("model gets created sucessfully")

#####################################
# Step 7 train the model
#####################################
print(Border)
print("train the model")
print(Border)

model.fit(X_train,Y_train)

print("model train sucessfully")
