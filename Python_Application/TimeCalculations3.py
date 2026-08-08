import time

def factorial(no):
    Fact = 1
    
    for i in range(1,no+1):
        Fact = Fact * i
        
    return Fact

def main():
    Value = int(input("Enter the number:"))
    
    start_Time = time.time()
    
    Ret = factorial(Value)
    
    end_time = time.time()
     
    print(f"Factorial of {Value} is {Ret}")
    
    print(f"Time required is :{end_time - start_Time} seconds")
    



if __name__ =="__main__":
    main()