def Summation(Data):
 
    Sum = 0
    
    for no in Data:
        Sum = Sum + no
        
    return Sum


def main():  
    Marks = [11,21,51,101]
    
    Ret = Summation(Marks)
        
    print("Addition is :", Ret)


if __name__ == "__main__":
    main()
    
    
