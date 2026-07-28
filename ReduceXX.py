from functools import reduce    #reduce imported from out side 

checkEven=lambda No:(No%2==0)   #its a lambda functions  find the even 

increment=lambda No:  No+1      #addition the value 

Addition=lambda No1,No2: No1+No2

def main ():                      #main functions
    data = [13 ,12,8,10,11,20]

    print("input data is :",data)
     
    Fdata=list(filter(checkEven,data))#filtering the value  
    print("data after filter:",Fdata) 

    Mdata=list(map(increment ,Fdata)) #mapping  the value
    print("data after Mdata:",Mdata)

    Rdata=reduce(Addition,Mdata,)    #reducing the value
    print("dfata after reduce",Rdata)
    

if __name__=="__main__":
    main() 