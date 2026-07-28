class base1:
    def fun(self):
        print("inside the the base1 fun")

class base2:
    def sun(self):
        print("inside the base2 sun")


class child(base1,base2):
    def gun(self):
        print("inside  the gun")


obj=child()
obj.fun()
obj.sun()
obj.gun()        
