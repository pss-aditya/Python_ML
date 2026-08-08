from functools import reduce

def CheckEven(No):
    return (No % 2 == 0)

def Increment(No):
    return (No + 1)

def Addition(No1, No2):
    return No1 + No2

def main():
    Data = [13,12,8,10,11,20]
    print("Input data is        : ", Data)
    
    FData = list(filter(CheckEven,Data))  # filter(functionName,iterable) it should return boolean
    print("Data After Filter    : ", FData)
    
    MData = list(map(Increment,FData))    #map ha boolen ghet nai tyamule tyla fdata pass kela
    print("Data After Map       : ", MData)
    
    RData = reduce(Addition, MData)
    print("Data after Reduce is : ", RData)
    
   
    
    
if __name__ == "__main__": 
    main()