class Arithmatic:
    def __init__(self,A,B):
        self.No1=A
        self.No2=B
        
    def Addition(self):
        Ans= self.No1 + self.No2
        return Ans

    def subtraction(self):
        Ans= self.No1-self.No2


value1=int(input("enter the first number:"))
value2=int(input("enter seond number:"))
obj=Arithmatic()
Ret=obj.Addition(value1,value2)
print(Ret)
Ret1=obj.subtraction(value1,value2)
print(Ret1)