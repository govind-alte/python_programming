def main():
    try:
        open("Demo.txt","w")
        print("file gets opened")


    
    except FileNotFoundError as fobj:

        print("file not present in directory")
if __name__=="__main__":
    main()
