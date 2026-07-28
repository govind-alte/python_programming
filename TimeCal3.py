import time
def factorial(no):
    fact=1
    for i in range(1,no+1):
        fact=fact*i

    return fact    


def main():
    value=int(input("Enter nuber:"))

    start_time=time.time()
    Ret=factorial(value)

    end_time=time.time()
    print("factorial is:",Ret)

    print(f"time requred is:{end_time -start_time}second")

if __name__=="__main__":
    main()  