def checkEven(No):
    if (No%2==0):
        print("Its even number :")
    else:
        print("its odd number :")    

def main():
    value = int(input("Enter number :"))
    checkEven(value)

if __name__=="__main__" :
    main()   