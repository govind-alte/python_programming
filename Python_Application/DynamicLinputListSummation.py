def Summation(data):#12
    sum=0
    for no in data:  
        sum=sum+no
    return sum    


def main():#3
    size=0#4
    arr=list()#5

    print("enter the number:")#6
    size=int(input())#6

    print("enter the element")#7

    for i in range(size):#8
        no=int(input())#9
        arr.append(no)#10
         

    Ret=Summation(arr)  #11  
    print("summation is :",Ret) 

if __name__== "__main__":#1
    
    main()#2
