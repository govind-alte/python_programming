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


print("shape of data set:",df.shape)#shape is return the number or row in tables data set 
print("column names:",list(df.columns))#header of column return name of column all 

print("missing values par column:")
print(df.isnull().sum())#null value show 

print("class distribution (species count)")
print(df["species"].value_counts()) #column count all species count and show all count 

print("statistical report of dataset")
print(df.describe)

