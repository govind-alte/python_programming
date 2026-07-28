import sys 

def main():
    print("--------------------------------------------------------")
    print("MArvellous Automation Script")
    print("--------------------------------------------------------")

    if (len(sys.argv))==2:

        if (sys.argv[1]=="--h" or sys.argv[1]=="--h"):
            print("this automation use to travel directory ")
            print("for better usage check --u flag")


        elif (sys.argv[1]=="--u" or sys.arg[1]=="--u"): 
            print("the script as")
            print("python filrname.py Directoryname")
            print("directoryName Should be Absulte path")

        

            
        else:
            DirectoryName=sys.argv[1]
            print("Directory name is",DirectoryName)

    else:
        print("invalid number")
        print("--u for information")

    
    print("--------------------------------------------------------")
    print(" thank you for using MArvellous Automation Script")
    print("--------------------------------------------------------")    
        


if __name__=="__main__":
    main()
