class Demo:
    value1=10
    value2=20


    def  __init__(self):
        self.No1=11
        self.No2=21


    def fun(self):
        print("inside the fun method")
        print(self.No1)

    @classmethod
    def gun(cls):
        print("inside the the class gun")
        print(Demo.value1)

    @staticmethod
    def sun():
        print("inside the sun as static")
        print(Demo.value1)   


obj=Demo()
obj.fun()
obj.gun()
obj.sun()