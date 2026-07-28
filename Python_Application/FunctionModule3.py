from Marvellous import Addition 


def main():
    
    print("Enter first number :")
    Value1 =int(input())


    print("Enter second number :")
    Value2 =int(input())

    Ret = Addition(Value1,Value2)  

    print("Addition is:",Ret)

    Ret= Subtraction(Value1,Value2) #error

    print("Subtraction is:",Ret)

if __name__== "__main__":
    
    main()