import sys
import os
import hashlib

def CalculateCheckSum(FileName):
    
    fobj = open(FileName,"rb") 
    hobj = hashlib.md5()
    Buffer =  fobj.read(1024)
    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)
    
    fobj.close()
    return hobj.hexdigest()

def FindDuplicate(DirectoryName):
    Ret = False
    
    Ret = os.path.exists(DirectoryName)
    if Ret == False:
        print("Path Don't Exists")
        return
    
    Ret = os.path.isdir(DirectoryName)
    if Ret == False:
        print("Dir doesn't Exists")
        return
    
    Ret = os.path.isfile(DirectoryName)
    if Ret == False:
        print("File Doesnt Exists")
        return
    
    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):
        for Fname in FileName:
            Fname = os.path.join(FolderName, Fname)
            
            CheckSum = CalculateCheckSum(Fname)
        
            print(f"{Fname} : {CheckSum} ")
    

def main():
    

    Ret = FindDuplicate("Marvellous")
    
    

if __name__ =="__main__":
    main()