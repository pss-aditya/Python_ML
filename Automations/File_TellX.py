def main():
    try:
        fobj = open("Demo.txt","r")
        print("File is Opened")
        
        print("File offset is : ", fobj.tell()) #0
        
        Data = fobj.read(10)
        print(Data)                             #Marvellous
        print("File offset is : ", fobj.tell()) #10

        Data = fobj.read(10)                    
        print(Data)                             
        print("File offset is : ", fobj.tell())
        fobj.close()
        
    except FileNotFoundError as fobj:
        print("File is not present in current Directory")

if __name__ == "__main__":
    main()