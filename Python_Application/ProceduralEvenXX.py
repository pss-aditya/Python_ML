
def CheckEven(No1):
    return(No1 % 2 == 0) #Logic for Even Odd
   

def main():
    Value1 = int(input("Enter the Value : \n"))
    
    Ret = CheckEven(Value1)     
    
    if(Ret == True):
        print("The Number is Even.")
    else:
        print("The Number is Odd.")
       

if __name__ == "__main__":
    main()