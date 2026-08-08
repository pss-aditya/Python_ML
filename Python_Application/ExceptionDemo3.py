def main():
    Ans = 0 
    try:
        
        print("Enter First Number:")
        No1 = int(input())
    
        print("Enter Second Number:")
        No2 = int(input())
        
        Ans = No1/No2
        
        print("Division is successful")
        
    except ZeroDivisionError as zobj:
        print("Exception occured due to 2nd operand is zero :", zobj)
    
    except ValueError as vobj:
        print("Exception occured due to invalid datatype :" , vobj)
        
    print("Division is :", Ans)
        
    
if __name__ == "__main__":
    main()