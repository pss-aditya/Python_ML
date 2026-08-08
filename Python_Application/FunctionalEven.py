CheckEven = lambda No1 : (No1 % 2 == 0)

def main():
    Value1 = int(input("Enter the Value : \n"))
    
    Ret = CheckEven(Value1)     #line 1 khali ali ani m te Ret = (Value1 % 2 == 0) remember the example of urbanclap te ghari ale
    
    if(Ret == True):
        print("The Number is Even.")
    else:
        print("The Number is Odd.")
       

if __name__ == "__main__":
    main()