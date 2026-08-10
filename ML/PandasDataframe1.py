import pandas as pd

def main():
    data={
        "Name":["Sagar","Amit","Poojas"],
        "Age":[27,28,25],
        "City":["Pune","kolhapur","Satara"]

    }
    print(data)
    print(type(data))
    print(data["Name"])
if __name__=="__main__":
    main()
