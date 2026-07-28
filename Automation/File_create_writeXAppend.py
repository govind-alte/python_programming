def main():
    try:
        fobj= open("Demo.txt","a")
        print("file gets opened")

        fobj.write("  pune  maharashtra")
        fobj.close()

    
    except FileNotFoundError as fobj:

        print("file not present in directory")
if __name__=="__main__":
    main()
