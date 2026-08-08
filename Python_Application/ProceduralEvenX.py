
def CheckEven(No1):
    if(No1 % 2 == 0): #Logic for Even Odd
        return True
    else :
        return False
   

def main():
    Value1 = int(input("Enter the Value : \n"))
    
    Ret = CheckEven(Value1)     
    
    if(Ret == True):
        print("The Number is Even.")
    else:
        print("The Number is Odd.")
       

if __name__ == "__main__":
    main()