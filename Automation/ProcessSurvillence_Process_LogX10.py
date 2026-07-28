#python processsurvileence.py 2 marvellouslog\
#python processsurvileence.py  time_interval Foldername
#len(sys.argv)->3


import psutil
import sys
import os
import time
import schedule

def ProcessScan():

    listprocess=[]

    for proc in psutil.process_iter():
        info= proc.as_dict(attrs=["pid","name","username","status"])
        info["cpu_percent"]=proc.cpu_percent(None)
        info["memory_percent"]= proc.memory_percent()

        listprocess.append(info)
    return listprocess

        


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

#######
    timestamp=time.strftime("%Y-%m-%d_%H-%M-%S")

    FileName=os.path.join(FolderName,"Marvellous_%s.Log" %timestamp)

    fobj=open(FileName,"w")
    print(f"Log file get created with name{FileName}")

    fobj.write(border+"\n")
    fobj.write("--marvellous platform survillence system--- \n")
    fobj.write("log file get creates ar:"+timestamp+"\n")
    fobj.write(border+"\n\n")

    fobj.write("------------system Report--------------\n")

    #cpu information-------------------------------------------
    fobj.write("CPU information")
    fobj.write("CPU number of core :%s \n" %psutil.cpu_count())
    fobj.write("cpu usage :%s %%\n" %psutil.cpu_percent())
    fobj.write(border+"\n")

    #RAM information-----------------------------------------
    memory = psutil.virtual_memory()
    fobj.write("Memory information")
    fobj.write("RAM usage :%s %%\n" %memory.percent)
    fobj.write("total RAM avalible  :%s\n" %memory.total)
    fobj.write(border+"\n")

    #Network information-------------------------------------
    netobj=psutil.net_io_counters()

    fobj.write("Network Report\n")
    fobj.write("sent: %.2f MB\n" %(netobj.bytes_sent / (1024*1024)))
    fobj.write("Recive: %.2f MB\n" %(netobj.bytes_recv / (1024*1024)))
    fobj.write(border+"\n")

    #process Log-----------------------------------------------
    data=ProcessScan()
    for info in data:
       # fobj.write(f"{info}\n")
       fobj.write("PID : %s\n" %info.get("pid"))
       fobj.write("Name : %s\n" %info.get("name"))
       fobj.write("UserNmae : %s\n" %info.get("username"))
       fobj.write("Status : %s\n" %info.get("status"))
       fobj.write("CPU usage : %.2f\n" %info.get("cpu_percent"))
       fobj.write("RAM usage : %.2f\n" %info.get("memory_percent"))
           
       fobj.write(border+"\n")
        



    

    fobj.write(border+"\n")
    fobj.write("------------End of Log file------------\n")
    fobj.write(border+"\n")

    fobj.close()
    


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
        #PlatformSurvillence(sys.argv[2])
        #print("CPU usage:",psutil.cpu_percent())
        print("schedular started sucessfully")
        print("press ctrel + c to abort automation script")
        
        schedule.every(int(sys.argv[1])).minutes.do(PlatformSurvillence,sys.argv[2])
        while True:
            schedule.run_pending()
            time.sleep(1)

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
