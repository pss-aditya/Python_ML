import time

def factorial(no):
    Fact = 1
    
    for i in range(1,no+1):
        Fact = Fact * i
        
    return Fact

def main():
    Value = int(input("Enter the number:"))
    
    start_time = time.perf_counter()  # perf_counter() is performance counter is better than time
    Ret = factorial(Value)   
    end_time = time.perf_counter()
     
    print(f"Factorial of {Value} is {Ret}")   
    print(f"Time required is :{end_time-start_time : .5f} seconds")
    



if __name__ =="__main__":
    main()