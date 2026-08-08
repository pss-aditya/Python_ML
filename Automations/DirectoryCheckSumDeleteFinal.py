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

    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):
        for Fname in FileName:
            Fname = os.path.join(FolderName, Fname)
            
            CheckSum = CalculateCheckSum(Fname) 
               
            if CheckSum in Duplicate:
                Duplicate[CheckSum].append(Fname)
            else:
                Duplicate[CheckSum] = [Fname]
                
    return Duplicate

def DeleteDuplicate(DirectoryName):
    myDict = FindDuplicate(DirectoryName)

    Result = list(filter(lambda x : len(x) > 1, myDict.values()))
    
    Count = 0
    TotalDeleted = 0

    for value in Result:
        for subvalue in value:
            
            Count += 1
            if (Count > 1):
                os.remove(subvalue)
                TotalDeleted += 1
        Count = 0
     
    print("Total Deleted Files are :", TotalDeleted)
    
   
def main():    

    Data = DeleteDuplicate("Test")

if __name__ =="__main__":
    main()