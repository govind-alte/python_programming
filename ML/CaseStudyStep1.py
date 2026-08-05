import pandas as pd #pd is nicke name of pandas 
Border="-"*30
#####################################
# Step 1 load data set
#####################################

print(Border)
print("step 1 load data set")
print(Border)

datapath="iris.csv"#call the file which file contain the data load and store this datapath

df = pd.read_csv(datapath)#df mains dataframe(df) pd used read the data adns store data in df  //read kelela data df made thevla 
print("dataset loaded sucessfully")
print("initial emtry from dataset are:")
print(df.head()) # only header data give mi first fev lines   df aata csv file ahe 

