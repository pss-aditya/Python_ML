import os

def main():
    ret = os.path.exists("Demo.txt")  
    
    if(ret == True):
        print("File is present in Current Directory")
    else:
        print("There is no such file present")

if __name__ == "__main__":
    main()