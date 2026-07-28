import time
def SumCube(No):
    sum=0
    for i in range(1,No+1):
        sum=sum+(i**3)
    return sum 


def main():
    data=[10000000,20000000,30000000,40000000,50000000]
    Result=[]

    stime=time.perf_counter()
    for value in data:
        Ret=SumCube(value)
        Result.append(Ret)
    etime=time.perf_counter()    
    print("Result is: ")
    print(Result)
    print(f"time: {etime-stime:.4f}:seconds")

if __name__=="__main__":
    main()