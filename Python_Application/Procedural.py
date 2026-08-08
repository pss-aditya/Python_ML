def Addition(No1 ,  No2):
    Ans = No1 + No2 
    return Ans

def Substraction(No1 , No2):
    Ans = No1 - No2
    return Ans

Value1 = int(input("Enter the First   Number : "))
Value2 = int(input("Enter the  Second Number : "))
    
Ret = Addition(Value1, Value2)
print("Addition is : ", Ret)

Ret = Substraction(Value1, Value2)
print("Substraction is : ", Ret)
