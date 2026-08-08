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
    
    Duplicate = {}
    
    Unique = 0
    Same  = 0
    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):
        for Fname in FileName:
            Fname = os.path.join(FolderName, Fname)
            
            CheckSum = CalculateCheckSum(Fname) 
        
            print(f"{Fname} :  {CheckSum} ")
               
            if CheckSum in Duplicate:
                Same = Same + 1
                Duplicate[CheckSum].append(Fname)
            else:
                Unique = Unique + 1
                Duplicate[CheckSum] = [Fname]
    print("Unique File Found are    :", Unique)
    print("Duplicate File Found are :", Same)
    print("File Found are in Key Value pair :", Duplicate)
    

def main():
    

    Ret = FindDuplicate("Test")
    
    

if __name__ =="__main__":
    main()