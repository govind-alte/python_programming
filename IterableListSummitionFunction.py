
def Summation (data):#6
    sum=0
    for no in data:
        sum=sum+no
    return sum

def main():#3 
    Marks=[78,90,56,98,77]#4

    Ret=Summation(Marks)#5
    print("addition is :",Ret)        

if __name__=="__main__" :#1
    main()  #2