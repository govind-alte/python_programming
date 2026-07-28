def main():
    try:
        fobj= open("Demo.txt","r")
        print("file gets opened")

        data=fobj.read(10)

        print(data)
        fobj.close()

    
    except FileNotFoundError as fobj:

        print("file not present in directory")
if __name__=="__main__":
    main()
