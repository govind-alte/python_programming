#seek (kute /kuthun)
#kuthun :0/1/2  0 starting  ,1 current, 2 end
def main():
    try:
        fobj= open("Demo.txt","r")
        print("file gets opened")

        fobj.seek(10,0) 

        data=fobj.read(10)

        print(data)
        

       

    
    except FileNotFoundError as fobj:

        print("file not present in directory")
if __name__=="__main__":
    main()
