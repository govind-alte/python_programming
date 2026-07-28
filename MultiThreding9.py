
import time
import threading

def SumEven(No):

    print("TID of sumeven thred is:",threading.get_ident())   




def SumOdd(No):

    print("TID of Sumodd thred is:",threading.get_ident()) 
    

def main():
    print("TID of main thred is:",threading.get_ident()) 

    start_time=time.perf_counter()

    t1=threading.Thread(target=SumEven,args=(10000,))
    
    t2=threading.Thread(target=SumOdd,args=(10000,))

    t1.start()
    t2.start()

    t1.join
    t2.join


    end_time=time.perf_counter()


    print(f"time required is :{end_time-start_time:.4f}")

if __name__=="__main__":
    main()