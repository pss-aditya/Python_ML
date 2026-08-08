def main():
    try:
        fobj = open("Demo.txt","a")
        print("File is Opened")
        
        fobj.write(" Pune Maharashtra")
        
        fobj.close()
    except FileNotFoundError as fobj:
        print("File is not present in current Directory")

if __name__ == "__main__":
    main()