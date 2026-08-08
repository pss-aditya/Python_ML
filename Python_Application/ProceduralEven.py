
def CheckEven(No1):
    if(No1 % 2 == 0): #Logic for Even Odd
        print("The number is Even")
    else :
        print("The number is odd")
        
    
    

def main():
    Value1 = int(input("Enter the Value : \n"))
    
    CheckEven(Value1)
       

if __name__ == "__main__":
    main()