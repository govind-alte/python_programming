def checkEven(No):
    if (No%2==0):
        return True
    else:
        return False

def main():
    value = int(input("Enter number :"))
    Ret= checkEven(value)

    if Ret==True:
        print("iots even number:")
    else:
        print("it odd number :")    

if __name__=="__main__" :
    main()   