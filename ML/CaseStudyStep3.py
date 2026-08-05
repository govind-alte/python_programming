import pandas as pd
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
    "sepal length (cm)",            #4 column store in  variable feature_col
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)"

]

X=df[feature_cols]    #feature_col all column store in X variable 
Y=df["species"]       ## species column store in Y variable

print("X shape",X.shape) 
print("Y shape",Y.shape)