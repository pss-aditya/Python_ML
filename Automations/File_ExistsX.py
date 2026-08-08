import os

def main():
    
    if(os.path.exists("Demo.txt")):
        print("File is present in Current Directory")
    else:
        print("There is no such file present")

if __name__ == "__main__":
    main()