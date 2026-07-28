#importhing required libraries 
import sys 
import os
import time
import schedule

#Function name:   DirectoryScanner
#input :          NAme of Directory
#Description:     deletes all empty files periodically
#date:             19/07/2026
#author:           Alte Govind Jagannath

def DirectoryScanner(DirectoryPath):
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

    Totalfile=0
    Emptyfile=0


    for folderName,SubFolder,FileName in os.walk(DirectoryPath):
        for Fname in FileName:
            Totalfile=Totalfile+1

            Fname=os.path.join(folderName,Fname)
            fobj.write(f"{Fname}:{os.path.getsize(Fname)}bytes\n")

            #print(f"file name{Fname}:{os.path.getsize(Fname)} bytes")
            if (os.path.getsize(Fname)==0):
                Emptyfile=Emptyfile+1
                os.remove(Fname)

    fobj.write(Border+"\n")
    print(f"total file scan :{Totalfile}\n")
    fobj.write(f"Total empty files found and deleted :{Emptyfile}\n")

    fobj.write(Border+"\n")       
    fobj.write("log filr get created at:"+timestamp)
    fobj.write(Border+"\n")
            
    fobj.close()        


#Function name:   main
#input :          command line argument
#Description:     in cntrol the script 
#date:             19/07/2026
#author:           Alte Govind Jagannath
def main():
    Border="-"*40
    print(Border)
    
    print("MArvellous Automation Script")
    
    print(Border)

    if (len(sys.argv)==2):

        if (sys.argv[1] =="--h" or sys.argv[1] =="--h"):
            print("this automation use to travel directory ")
            print("for better usage check --u flag")


        elif (sys.argv[1] =="--u" or sys.argv[1] =="--u"): 
            print("the script as")
            print("python filename.py Directoryname")
            print("directoryName Should be Absulte path")

        

            
        else:
            
            schedule.every(1).minute.do(DirectoryScanner,sys.argv[1])
            
            while True:
                schedule.run_pending()
                time.sleep(1)
            

    else:
        print("invalid number")
        print("--u for information")

    print(Border)
    
    print(" thank you for using MArvellous Automation Script")
    print(Border)

 # Starter of authomation script



if __name__=="__main__":
    main()
