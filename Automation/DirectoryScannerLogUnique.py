#all fun are use  in the ione time 
import sys 
import os
import time


def DirectoryScanner(DirectoryPath):
    timestamp=time.ctime()
    logfileName="marvellous %s.log"%(timestamp)
    logfileName=logfileName.replace(" ","_")
    logfileName=logfileName.replace(":","_")
    
    print("file name is :",logfileName) 

    


    fobj=open(logfileName,"w")

    fobj.write("M Automation Script \n")

    
    
    for folderName,SubFolder,FileName in os.walk(DirectoryPath):
        for Fname in FileName:
            fobj.write(Fname+"\n")
    fobj.close()        


def main():
    Border="-"*40
    print(Border)
    
    print("MArvellous Automation Script")
    
    print(Border)

    if (len(sys.argv)==2):

        if (sys.argv[1]=="--h" or sys.argv[1]=="--h"):
            print("this automation use to travel directory ")
            print("for better usage check --u flag")


        elif (sys.argv[1]=="--u" or sys.argv[1]=="--u"): 
            print("the script as")
            print("python filrname.py Directoryname")
            print("directoryName Should be Absulte path")

        

            
        else:
            DirectoryScanner(sys.argv[1])
            

    else:
        print("invalid number")
        print("--u for information")

    print(Border)
    
    print(" thank you for using MArvellous Automation Script")
    print(Border)


if __name__=="__main__":
    main()
