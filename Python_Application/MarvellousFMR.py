
CheckEven = lambda No : (No % 2 == 0)
Increment = lambda No :(No + 1)
Addition = lambda No1, No2 : ( No1 + No2)

def FilterX(Task,Elements):
    Result = []
    
    for no in Elements:
        Ret = Task(no)  # CheckEven(no)
        
        if(Ret == True):
            Result.append(no)
    
    return Result

def MapX(Task, Elements):
    
    Result = []
    
    for no in Elements:
        Ret = Task(no)  #Increment(no) 
        Result.append(no)
        
    return Result
    

def ReduceX(Task, Elements):
    
    Sum = 0
    
    for no in Elements:
        Sum = Task(Sum,no)
        
    return Sum
    

def main():
    Data = [13,12,8,10,11,20]
    print("Input data is        : ", Data)
    
    FData = list(FilterX(CheckEven,Data))  # filter(functionName,iterable) it should return boolean value ekch
    print("Data After Filter    : ", FData)
    
    MData = list(MapX(Increment,FData))    #map ha boolen ghet nai tyamule tyla fdata pass kela value ekch
    print("Data After Map       : ", MData)
    
    RData = ReduceX(Addition, MData) # value 2 dyche like no 1 ani no 2
    print("Data after Reduce is : ", RData)
    
   
    
    
if __name__ == "__main__": 
    main()