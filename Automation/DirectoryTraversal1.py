import os

def main():
    for FolderName,SubFilder,FileName in os.walk("Marvellous"):
        print(FolderName)
if __name__=="__main__":
    main()
