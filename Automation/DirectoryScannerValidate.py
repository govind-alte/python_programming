#all fun are use  in the ione time 
import sys 
import os
import time
import schedule

def DirectoryScanner(DirectoryPath="Marvellous"):
    Border="-"*40
    timestamp=time.ctime()

    logfileName="marvellous%s.log"%(timestamp)
    logfileName=logfileName.replace(" ","_")
    logfileName=logfileName.replace(":","_")


    Ret=False
    Ret=os.path.exists(DirectoryPath)

    


    if(Ret==False):
        print("Marvellous Automation Error:There is no such directory  with name",DirectoryPath)
        return 
    
    
    
    Ret=os.path.isdir(DirectoryPath)

    if Ret==False:
        print("marvellous automation error: it is not directory  with name ",DirectoryPath)
        return

    
    print("file name is :",logfileName)

    


    fobj=open(logfileName,"w")
    fobj.write(Border+"\n")

    fobj.write("M Automation Script \n")
    
    fobj.write(Border+"\n\n")
    print("filr from directory are","\n\n")
    fobj.write(Border+"\n")

    
    
    for folderName,SubFolder,FileName in os.walk(DirectoryPath):
        for Fname in FileName:
            fobj.write(Fname+"\n")
           
    fobj.write("log filr get created at:"+timestamp)
    fobj.write(Border+"\n")        
    fobj.close()        


def main():
    Border="-"*40
    print(Border)
    
    print("MArvellous Automation Script")
    
    print(Border)

    if (len(sys.argv))==2:

        if (sys.argv[1]=="--h" or sys.argv[1]=="--h"):
            print("this automation use to travel directory ")
            print("for better usage check --u flag")


        elif (sys.argv[1]=="--u" or sys.arg[1]=="--u"): 
            print("the script as")
            print("python filrname.py Directoryname")
            print("directoryName Should be Absulte path")

        

            
        else:
            
            schedule.every(1).minute.do(DirectoryScanner,sys.argv[1])
            while True:
                schedule.run_pending()
                time.sleep()
            

    else:
        print("invalid number")
        print("--u for information")

    print(Border)
    
    print(" thank you for using MArvellous Automation Script")
    print(Border)


if __name__=="__main__":
    main()
