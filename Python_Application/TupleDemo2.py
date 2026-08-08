def main():
    Data=(10,20,30,40)
    
    print(type(Data))
    print("Length of Data is :",len(Data))
    
    print(Data[0])
    print(Data[1])
    print(Data[2])
    print(Data[3])
    
    Data[1] = 21
    print("Updated Data of 1 is :", Data)

if __name__ == "__main__":
    main()
    #data is immutable