import pandas as pd
import joblib
def LoadModel(Filename):

    model=joblib.load(Filename)
    print("model load sucessfully ")
    print(model.feature_names_in_)

    return model

def Predict(model):
    print("enter information ")
    Pclass=int(input("enter (1/2/3)"))
    Sex= int(input("enter sex :(0-m/1:f)"))

    Age=int(input("enter age "))
    sibsp=int(input("enter sibsp"))
    Parch=int(input("enter parch"))
    Fare=int(input("enter fare"))

    Embarked=float(input("enter (0/1/2)"))

    passenger=pd.DataFrame([{
        "Pclass":Pclass,
        "Sex":Sex,
        "Age":Age,
        "sibsp":sibsp,
        "Parch":Parch,
        "Fare":Fare,
        "Embarked_1.0":1 if Embarked==1 else 0,
        "Embarked_2.0":2 if Embarked==2 else 0




    }])
    passenger=passenger[model.]



def main():
    model=LoadModel("marvellousTitanic.pkl")
    Predict(model)




if __name__=="__main__": 
    main() 