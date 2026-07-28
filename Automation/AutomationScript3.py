import sys 

def main():

    if (len(sys.argv)==2):

        if (sys.argv[1]=="--h" or sys.argv[1]=="--h"):
            print("hello"  or sys.argv[1]=="--h")
        elif (sys.argv[1]=="--u"): 
            print("usage")

        

            
        else:
            DirectoryName=sys.argv[1]
            print("Directory name is",DirectoryName)
    else:
        print("invalid number")
        print("--u for information")
        


if __name__=="__main__":
    main()
