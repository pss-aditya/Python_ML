def CheckEven(No):
    return (No % 2 == 0)

def Increment(No):
    return (No + 1)

def main():
    Data = [13,12,8,10,11,20]
    print("Input data is     : ", Data)
    
    FData = list(filter(CheckEven,Data))  # filter(functionName,iterable) it should return boolean
    print("Data After Filter : ", FData)
    
    MData = list(map(Increment,FData))    #map ha boolen ghet nai tyamule tyla fdata pass kela
    print("Data After Map    : ", MData)
    
   
    
    
if __name__ == "__main__": 
    main()