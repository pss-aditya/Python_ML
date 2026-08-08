def main():
    try:
        fobj = open("Demo.txt","r")
        print("File is Opened")
        
        Data = fobj.read()
        
        print(Data)
        
        fobj.close()
        
    except FileNotFoundError as fobj:
        print("File is not present in current Directory")

if __name__ == "__main__":
    main()