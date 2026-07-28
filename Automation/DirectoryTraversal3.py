import os

def main():
    for FolderName,SubFolder,FileName in os.walk("Marvellous"):
        print("Folder Name",FolderName)

        for subf in SubFolder:
            print("SubFolder",subf)


        for Fname in FileName:
            print("FileName:",Fname)    
if __name__=="__main__":
    main()
