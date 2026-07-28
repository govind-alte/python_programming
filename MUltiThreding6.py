
import time
import threading

def SumEven(No):

    sum=0
    for i in range(2,No,2):
        sum=sum+i
    print("sumition of even:", sum)    

def SumOdd(No):

    
    sum=0
    for i in range(1,No,2):
        sum=sum+i
    print("sumition of odd:", sum)  

def main():

    start_time=time.perf_counter()

    t1=threading.Thread(target=SumEven,args=(10,))
    
    t2=threading.Thread(target=SumOdd,args=(10,))

    t1.start()
    t2.start()


    end_time=time.perf_counter()


    print(f"time required is :{end_time-start_time:.4f}")

if __name__=="__main__":
    main()