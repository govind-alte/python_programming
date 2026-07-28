import sys 

def main():

    if (len(sys.argv)==2):
        DirectoryName=sys.argv[1]
        print("Directory name is",DirectoryName)
    else:
        print("invalid number")
        


if __name__=="__main__":
    main()
