

checkEven=lambda No:(No%2==0)   #its a lambda functions  find the even 

increment=lambda No:  No+1      #addition the value 

Addition=lambda No1,No2: No1+No2



def FilterX(Task,Elements):
    Result=[]
    for no in Elements:
        Ret=Task(no)  #checkEven (no) call

        if Ret==True:
            Result.append(no)

    return Result     



def mapx(Task ,Elements):
    Result=[]

    for no in Elements:
        Ret=Task(no)    #increment (no)
        Result.append(Ret)

    return Result


def reducex(task,Elements):
    Sum=0
    for no in Elements:
        Sum=task(Sum,no)
    return Sum    



def main ():                      #main functions
    data = [13 ,12,8,10,11,20]

    print("input data is :",data)
     
    Fdata=list(FilterX(checkEven,data))#filtering the value  
    print("data after filter:",Fdata) 

    Mdata=list(mapx(increment ,Fdata)) #mapping  the value
    print("data after Mdata:",Mdata)

    Rdata=reducex(Addition,Mdata,)    #reducing the value
    print("dfata after reduce",Rdata)
    

if __name__=="__main__":
    main() 