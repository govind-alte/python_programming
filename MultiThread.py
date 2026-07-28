import threading

def display():
    print("inside display",threading.get_ident())
def main():
    print("inside main",threading.get_ident())
    display()
if __name__=="__main__":
    main()