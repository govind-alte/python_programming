import sys 
import os
import hashlib

def CalculateCheckSum(FileName):#4
    fobj=open(FileName,"rb")

    hobj=hashlib.md5()

    Buffer=fobj.read(1024)

    while(len(Buffer)>0):
        hobj.update(Buffer)
        Buffer=fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()    

def FindDuplicate(DirectoryName):#3
    Ret=False
    Ret=os.path.exists(DirectoryName)

    if Ret==False:
        print("path invalid")
        return

    Ret=os.path.isdir(DirectoryName)

    if Ret==False:
        print("it is not directory")

        return

    Duplicate={}

    


    for FolderName,SubFolder,FileName in os.walk(DirectoryName):
        for fname in FileName:
            fname=os.path.join(FolderName,fname)

            checksum=CalculateCheckSum(fname)

            

            if checksum in Duplicate:
                
                Duplicate [checksum].append(fname)
            else:
            
                Duplicate[checksum]=[fname]

    return Duplicate         


def DeleteDuplicate(DirectoryName):#2
    mydict=FindDuplicate(DirectoryName)

    #Result=mydict.values()
    #return Result
    Result=list(filter(lambda x :len(x) > 1, mydict.values() ))
    
    Count=0
    TotalDeleted=0

    for value in Result:
       
        for subvalue in value:

            Count=Count+1
            if Count>1:
                print("Duplicate found:",subvalue)
                TotalDeleted=TotalDeleted+1
        Count=0
    print("totaldeleted files:",TotalDeleted)        



def main():
    Data=DeleteDuplicate("Test")
    


if __name__=="__main__":#1
    
    main()
