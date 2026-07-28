import os

def main():
        ret=os.path.exists("Demo1.txt")

        if ret==True:
              print("Yes")

        else:
              print("No")      


        print("file not present in directory")
if __name__=="__main__":
    main()
