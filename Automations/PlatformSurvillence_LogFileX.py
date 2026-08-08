# python ProcessSurvillence.py      2       MarvellousLog
# python ProcessSurvillence.py timeinterval FolderName
#                  0                 1          2
#  len.(sys.argv) --->3


import time 
import psutil
import sys
import os
import schedule



def PlatformSurvillence(FolderName):
    Border = "-"*60
    
    Ret = False
    Ret = os.path.exists(FolderName)
    if (Ret == True):
        Ret = os.path.isdir(FolderName)
        if Ret == False:
            print("Unable to proceed as Directory name is existing but its not a directory")
            return
    else:
        os.mkdir(FolderName)
        print("Folder has been created successfully for Log File.")
        
        
    timestamp = time.strftime("%Y_%m_%d_%H_%M_%S")
    FileName = os.path.join(FolderName, "Marvellous_%s.log" %timestamp)
    fobj = open(FileName,"w")
    fobj.write("------------------- Log File --------------")
    
    print(f"Log file gets created Successfully with name {FileName}")
    
def main():
    Border = "-"*60
    print(Border)
    print("  Marvellous Platform Survillence System  ")
    print(Border)
    
    # --h and --u handle will be done here 
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This Automation script is used to perform :-")
            print("1 : It fetch the information of running processess")
            print("2 : It fetch the information about the Primary Storage as RAM")
            print("3 : It fetch the information about the Secondary Storage as HDD")
            print("4 : It fetch the information about the microporcessor")
            print("5 : It gets auto scheduled periodically")
            print("6 : It maintains all records into log file")
            print("7 : It sends the log files through mail periodically")
            
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the Automation Script as :- ")
            print(f"python {sys.argv[0]} Time_Interval Folder_Name")
            print("Time_Interval : Time in minutes for periodic execution")
            print("Folder_Name   :  Name of folder for log File creation")
        else:
            print("Unable to proceed as Arguement are not matching")
            print("Please use --h or --u flag for getting more details")
            
    
    #Actual Project code
    elif(len(sys.argv) == 3):
            PlatformSurvillence(sys.argv[2])
            
            
    else:
        print("Unable to proceed as Arguement are not matching")
        print("Invalid No of Arguement ")
        print("Please use --h or --u flag for getting more details")
    
    
    print(Border)
    print("Thank you for using Marvellous Platform Survillence System")
    print(Border)


if __name__ == "__main__":
    main()