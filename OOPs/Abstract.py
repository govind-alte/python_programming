from abc import ABC,abstractmethod
class Bace(ABC):
    def Addition(self,No1,No2):
        pass

class child(Bace):
    def Addition(self, No1, No2):
        return No1+ No2
    
obj=child()
Ret=obj.Addition(11,11)
print(Ret)    
        