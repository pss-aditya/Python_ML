import sys

def main():
    
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation Script use to travel the Directory")
            print("For Better usage check --U flag")
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please exceute the Script as ")
            print("python FileName.py DirectoryName")
            print("DirectoryName should be Absolute Path")
        else:
            DirectoryName = sys.argv[1]
            print("Directory Name is :", DirectoryName)
    else:
        print("Invalid No of Arguments")
        print("Please use --h or --u for more information")
    

if __name__ == "__main__":
    main()
    