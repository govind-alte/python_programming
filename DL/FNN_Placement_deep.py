#-----------------------------------------------------------------------
#Deep learning pipeline
#----------------------------------------------------------------------
# 1.l load  the data from csv
# 2. data analyasis
# 3. preprocessing 
# 4. train test split
# 5. fetatures scaling 
# 6 .FNN model training 
# 7. model predication / Evaluation
# 8. graphical representation
# 9. model preserve
# 10.model loading preserve
# 11.test unseen data
#-------------------------------------------------------------------------

import pandas as pd 
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
import joblib
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier


#-----------------------------------------------------------------------
# step 1 load the data 
#----------------------------------------------------------------------
print("read the dataset ")
data=pd.read_csv("placement_data.csv")
print("complete dataset :")
print(data)


#-----------------------------------------------------------------------
# step 2 data analysis
#----------------------------------------------------------------------
print("data Analysis")
print("first 5 rows :")
print(data.head())

print("columns name :")
print(data.columns)

print("shape of dataset:")
print(data.shape)

print("statistical summry")
print(data.describe())

#-----------------------------------------------------------------------
# step 3 Preprocessing
#----------------------------------------------------------------------
print("step 3 Preprocessing:")
X=data[['Aptitude','Coding','Communication','Academics','Internship']]
Y=data['placed']

print("input features ")
print(X.head())

print("target:")
print(Y.head())

#-----------------------------------------------------------------------
# step 4 Train test splite
#----------------------------------------------------------------------
print("step 4 Train test splite")
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.30,random_state=42)
print("training input shape:")
print("X shape :",X_train.shape)
print("X shape :",X_test.shape)
print("X shape :",Y_train.shape)
print("X shape :",Y_test.shape)



#-----------------------------------------------------------------------
# step 5 Features scaling 
#----------------------------------------------------------------------
print("step 5 Features scaling ")
scaler=StandardScaler()
X_train_scaled=scaler.fit_transform(X_train)
X_test_scaled=scaler.fit_transform(X_test)

print("scaled training dara:")
print(X_train_scaled[:5])


#-----------------------------------------------------------------------
# step 6 FNN model training
#----------------------------------------------------------------------
print("step 6 FNN model training")
model=MLPClassifier(
    hidden_layer_sizes=(8,4),
    activation="relu",
    solver="adam",
    max_iter=1000,
    random_state=42
)
print(model)
print("train model")
model.fit(X_train_scaled,Y_train)
print("model trainf completed:")


#-----------------------------------------------------------------------
# step 7 model Evaluation
#----------------------------------------------------------------------
print("step 7 model Evaluation")
Y_pred=model.predict(X_test_scaled)

accuracy=accuracy_score(Y_test,Y_pred)
print("Accuracy is:",accuracy)

cm=confusion_matrix(Y_pred,Y_test)
print("Confution metrix:",cm)

print("predict th eprobablity:")
Y_prob=model.predict_proba(X_test_scaled)
print(Y_prob[:5])

#-----------------------------------------------------------------------
# step 9 model Preserve 
#----------------------------------------------------------------------
print("step 9 model Preserve")
joblib.dump(model,"placement_fnn_model.pkl")
joblib.dump(scaler,"placement_scaler.pkl")

print("model and scaler get dump succesfully:")




#-----------------------------------------------------------------------
# step 10 loading and preserve
#----------------------------------------------------------------------

print("step 10 loading and preserve")
loaded_model=joblib.load("placement_fnn_model.pkl")
loaded_scaler=joblib.load("placement_scaler.pkl")
print("model gets loaded successfully")


#-----------------------------------------------------------------------
# step 11 test unseen data
#Aptitude         70
#Coding           75
#Communication    80
#Acadamics        85
#internship       1
#----------------------------------------------------------------------
print("step 11 test unseen data")
new_student=pd.DataFrame([[70,75,80,85,1]],columns=['Aptitude','Coding','Communication','Academics','Internship'])

new_student_scaled=loaded_scaler.transform(new_student)

new_prediction=loaded_model.predict(new_student_scaled)

new_probablity=loaded_model.predict_proba(new_student_scaled)

print("new student data :")
print(new_student)

print("prediction probablity:",new_probablity)

if new_prediction[0]==1:
    print("prediction placed")
else:
    print("prediction not pleaced ")