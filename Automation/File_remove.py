import os

def main():
    try:
        os.remove("Demo.txt")#fobj.remove() =not applicable
        
        
        


    
    except FileNotFoundError as fobj:

        print("file not present in directory")
if __name__=="__main__":
    main()
