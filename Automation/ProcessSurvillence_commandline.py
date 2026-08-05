#python processsurvileence.py 2 marvellouslog\
#python processsurvileence.py  time_interval Foldername
#len(sys.argv)->3


import psutil
import sys
import os


def main():
    border="-"*50
    print(border)
    print("--marvellous platform survillence system--- ")
    print(border)
    #--h and --u
    if(len(sys.argv)==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("use to perform")
            print("1:Imformation or running process")
            print("2:Imformation about RAM")
            print("3:secondary storage HDD")
            print("4:Microprocessor")
            print("5:Auto schedule periodically")
            print("6:Record into Log file")
            print("7:log file  through mail periodically")

        elif (sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("use they automation scrip as:")
            print(f"python{sys.argv[0]}time_interval FolderName")
            print("Time_interval : time minites for execution ")
            print("FolderName : Name of folder ")


        else:
            print("unable matching argument") 
            print("")


    elif (len(sys.argv)==3):
        pass

    else:
        print("invalid number of argument")
        print("unable to proceed as argument are not matching")
        print("please use --h or --u flag getting more details")    




    print(border)
    print("thank you for using our Automation system")
    print("--marvellous platform survillence system--- ")
    print(border)
if __name__=="__main__":
    main()
