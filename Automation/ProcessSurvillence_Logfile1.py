#python processsurvileence.py 2 marvellouslog\
#python processsurvileence.py  time_interval Foldername
#len(sys.argv)->3


import psutil
import sys
import os


def PlatformSurvillence(FolderName):
    border="-"*50
    Ret=False
    Ret=os.path.exists(FolderName)
    
    if Ret==True:
        Ret=os.path.isdir(FolderName)
        if(Ret==False):
            print("unable to folder name existing but is not directory")
            return
    else:
        os.mkdir(FolderName)  
        print("Directory for the log file get created sucessfully")  






def main():



    border="-"*50
    print(border)
    print("--marvellous platform survillence system--- ")
    print(border)
    #--h and --u
    if(len(sys.argv)==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("use to perform")
            print("1: imformation or running process")
            print("2:imformation about RAM")
            print("3:secondary storage HDD")
            print("4:microprocessor")
            print("5:auto schedule periodically")
            print("6:Record into Log file")
            print("7:log file  through mail periodically")

        elif (sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("use they automation scrip as:")
            print(f"python{sys.argv[0]}time_interval FolderName")
            print("Time_interval : time minites for execution ")
            print("FolderName : Name of folder ")


        else:
            print("unable matching argument") 
            print("plz use --h and --u for getting match !!!!!!")


    elif (len(sys.argv)==3):
        PlatformSurvillence(sys.argv[2])

    else:
        print("invalid number of argument.......")
        print("unable to proceed as argument are not matching.....")
        print("please use --h or --u flag getting more details.....")    




    print(border)
    print("thank you for using our Automation system")
    print("--marvellous platform survillence system--- ")
    print(border)
if __name__=="__main__":
    main()
