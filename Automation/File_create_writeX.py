def main():
    try:
        fobj= open("Demo.txt","w")
        print("file gets opened")

        fobj.write("marvellous infosystems")
        fobj.close()

    
    except FileNotFoundError as fobj:

        print("file not present in directory")
if __name__=="__main__":
    main()
