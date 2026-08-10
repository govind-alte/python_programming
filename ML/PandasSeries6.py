import pandas as pd
def main():

    sobj=pd.Series([11,21,51,101],index=["C","C++","java","python"])
    print(sobj)
    print(sobj["Python"])

if __name__=="__main__":

    main()
    