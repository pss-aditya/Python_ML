#seek(kuthe,kuthun)


def main():
    try:
        fobj = open("Demo.txt","r")
        print("File is Opened")
        
        fobj.seek(10,0)
        
        Data = fobj.read()
        
        print(Data)
        
    except FileNotFoundError as fobj:
        print("File is not present in current Directory")

if __name__ == "__main__":
    main()