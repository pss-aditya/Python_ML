# factorial no 5 : 1* 2 * 3* 4* 5* 
def factorial(no):
    Fact = 1
    
    for i in range(1,no+1):
        Fact = Fact * i
        
    return Fact

def main():
    Value = int(input("Enter the number:"))
    
    Ret = factorial(Value)
     
    print(f"Factorial of {Value} is {Ret}")
    



if __name__ =="__main__":
    main()