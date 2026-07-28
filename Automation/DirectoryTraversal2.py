import os

def main():
    for FolderName,SubFolder,FileName in os.walk("Marvellous"):
        print("FolderName:",FolderName)

        for subf in SubFolder:
            print("SubFolder",subf)
if __name__=="__main__":
    main()
