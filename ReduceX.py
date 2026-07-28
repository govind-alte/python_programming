from functools import reduce

def checkEven (No):
    return(No%2==0)

def increment(No):
    return No+1

def Addition (No1,No2):
    return No1+No2

def main ():
    data = [13 ,12,8,10,11,20]

    print("input data is :",data)
    
    Fdata=list(filter(checkEven,data))#filtering
    print("data after filter:",Fdata) 

    Mdata=list(map(increment ,Fdata)) #mapping
    print("data after Mdata:",Mdata)

    Rdata=reduce(Addition,Mdata,)
    print("dfata after reduce",Rdata)
    

if __name__=="__main__":
    main() 