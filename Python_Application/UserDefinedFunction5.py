#Accept : Multiple Parameters
#Return : Multiple Value

def Marvellous(Value1,Value2):
    print("Inside Marvellous :", Value1,Value2)
    return 21,51

def main():
    Ret1, Ret2 = Marvellous(11,22) 
    print("Return Value is :", Ret1, Ret2)  

if __name__ =="__main__":
    main()