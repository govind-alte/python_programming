def Calculation(No1,No2):#7
        Mult=No1*No2#8
        Div=No1/No2#9
        return Mult,Div#10



def main():#3
        value1=int(input("Enter first number:"))#4
        value2=int(input("Enter second number:"))#5

        Ret1,Ret2= Calculation(value1,value2)#6

        print("Multiplication is:",Ret1)#11
        print("Division is:",Ret2)#12

if __name__=="__main__":#1
        main()# 2