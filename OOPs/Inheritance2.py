class base:
    def __init__(self):
        print("inside the parent classs")

class child(base):
    def __init__(self):
        super().__init__()
    
        print("inside the child class")
            
obj=child()