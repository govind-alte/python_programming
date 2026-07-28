import time
def factorial(no):
    fact=1
    for i in range(1,no+1):
        fact=fact*i

    return fact    


def main():
    value=int(input("Enter nuber:"))

    start_time=time.perf_counter()
    Ret=factorial(value)

    end_time=time.perf_counter()
    
    print("factorial is:",Ret)

    print(f"time requred is:{end_time -start_time:.5f}second")

if __name__=="__main__":
    main()  