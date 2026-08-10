import pandas as pd

def main():
    data={
        "Name":["Sagar","Amit","Poojas"],
        "Age":[27,28,25],
        "City":["Pune","kolhapur","Satara"]

    }
    dobj=pd.DataFrame(data)
    print(dobj)
    #print(dobj[0])  not allowed 
    print(dobj["Age"])
    
if __name__=="__main__":
    main()
