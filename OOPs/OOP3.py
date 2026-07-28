class demo:
    value1=10
    value2=20



    def __init__(self):
        self.No1=11
        self.No2=21


    def fun(self):
        print(self.No2)
        print(demo.value2)  

    @classmethod
    def sun(cls):
        print(demo.value1)  


obj=demo()
obj.fun()
obj.sun()















