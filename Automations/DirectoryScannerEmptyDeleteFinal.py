#######################################################################
# 
#  Importing required Libraries
#
#######################################################################


import sys
import os
import time
import schedule

###########################################################################
#  Function Name :                   DirectoryScanner
#  Input :                           Name of Directory
#  Description :                     Deletes all empty files periodically
#  Date :                            19/07/2026
#  Author :                          Aditya Govind Valekar
#
###########################################################################
def DirectoryScanner(DirectoryPath):
    Border = "-"*40
    
    timestamp = time.ctime()
    
    LogFileName = "Marvellous %s.log"%(timestamp)
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")
    
    Ret = False
    
    Ret = os.path.exists(DirectoryPath)
    if(Ret == False):
        print("Marvellous Automation Error : There is no such Directory with name",DirectoryPath)
        return 
    
    
    Ret  =  os.path.isdir(DirectoryPath)
    if(Ret == False):
        print("Marvellous Automation Error : It is not a Directory with name ", DirectoryPath)
        return
    
    print("Log File is created with name:", LogFileName)
    
    fobj = open(LogFileName,"w")
    
    fobj.write(Border + "\n\n")
    fobj.write(" Marvellous Automation Script \n")
    fobj.write(Border + "\n\n")
    
    fobj.write("Files from the directory are : \n\n")
    fobj.write(Border + "\n")
    
    TotalFiles = 0
    EmptyFiles = 0
    
    for FolderName,SubFolder,FileName in os.walk(DirectoryPath):
        for fname in FileName :
            TotalFiles = TotalFiles + 1
            fname = os.path.join(FolderName,fname)
            fobj.write(f"{fname} : {os.path.getsize(fname)} bytes\n")
            
            if os.path.getsize(fname) == 0:
                EmptyFiles = EmptyFiles + 1
                os.remove(fname)
    fobj.write(Border + "\n")
    fobj.write(f"Total Files Scanned :  {TotalFiles}\n")
    fobj.write(f"Total Empty Files Found and Delete :  {EmptyFiles}\n")

        
            
    fobj.write(Border + "\n")
    fobj.write("Log File is created at :" +timestamp)
    fobj.write("\n"+ Border + "\n")
          
    fobj.close()
    
#######################################################################
#  Function Name :                   DirectoryScanner
#  Input :                           Command Line Argument
#  Description :                     It controls the scripts
#  Date :                            19/07/2026
#  Author :                          Aditya Govind Valekar
#
#######################################################################
def main():
    
    Border = "-"*50
    print(Border)
    print("          Marvellous Automation Script         ")
    print(Border)
    
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation Script use to travel the Directory")
            print("For Better usage check --U flag")
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please exceute the Script as ")
            print("python FileName.py DirectoryName")
            print("DirectoryName should be Absolute Path")
        else:
            schedule.every(1).minute.do(DirectoryScanner,sys.argv[1])
            
            while True:
               schedule.run_pending()
               time.sleep(1)
                
    else:
        print("Invalid No of Arguments")
        print("Please use --h or --u for more information")
    
    print(Border)
    print("   Thank You for using  Automation Script     ")
    print(Border)
    
#######################################################################
# 
#  Starter of Automation Script
#
#######################################################################
if __name__ == "__main__":
    main()
    