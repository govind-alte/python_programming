import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
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
