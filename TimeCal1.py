
def factorial(no):
    fact=1
    for i in range(1,no+1):
        fact=fact*i

    return fact    


def main():
    value=int(input("Enter nuber:"))
    Ret=factorial(value)
    print("factorial is:0",Ret)

if __name__=="__main__":
    main()    