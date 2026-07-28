import sys 
import os
import hashlib

def CalculateCheckSum(FileName):
    fobj=open(FileName,"rb")

    hobj=hashlib.md5()

    Buffer=fobj.read(1024)

    while(len(Buffer)>0):
        hobj.update(Buffer)
        Buffer=fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()    

def FindDuplicate(DirectoryName):
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

    Unique=0
    Same=0


    for FolderName,SubFolder,FileName in os.walk(DirectoryName):
        for fname in FileName:
            fname=os.path.join(FolderName,fname)

            checksum=CalculateCheckSum(fname)

            print(f"{fname}:{checksum}")

            if checksum in Duplicate:
                Same=Same+1
                Duplicate [checksum].append(fname)
            else:
                Unique=Unique+1
                Duplicate[checksum]=[fname]

    print("unique file found :",Unique)
    print("Duplicate files found: ",Same)            



def main():
    FindDuplicate("Test")


if __name__=="__main__":
    
    main()
