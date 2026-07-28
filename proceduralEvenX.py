def checkEven(No):
     return(No%2==0)

def main():
    value = int(input("Enter number :"))
    Ret= checkEven(value)

    if Ret==True:
        print("its even number:")
    else:
        print("it odd number :")    

if __name__=="__main__" :
    main() 