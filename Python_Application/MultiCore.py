#import os


#def main():
 #   print("No. of Logical Cores are :", os.cpu_count())
    



#if __name__ =="__main__":
 #   main()
    
# program to see logical and physical core and platform

import psutil
import platform
import subprocess


print("Physical Cores :", psutil.cpu_count(logical=False))
print("Logical Cores  :", psutil.cpu_count(logical=True))
print(platform.processor())
print(subprocess.check_output("wmic cpu get name").decode())