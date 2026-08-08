def main():
    try:
        open("Demo.txt","r")
        print("File is Opened")
    except FileNotFoundError as fobj:
        print("File is not present in current Directory")

if __name__ == "__main__":
    main()