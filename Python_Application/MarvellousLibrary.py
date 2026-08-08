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