class Arithematic:
    def Addition(No1 ,  No2):
        Ans = No1 + No2 
        return Ans

    def Substraction(No1 , No2):
        Ans = No1 - No2
        return Ans
    
Aobj = Arithematic()

Value1 = int(input("Enter the First   Number : "))
Value2 = int(input("Enter the  Second Number : "))
    
# Ret = Addition(Aboj.Value1, Value2) asa jaat ahe so self pahije next code bg
Ret = Aobj.Addition(Value1, Value2) #Error
print("Addition is : ", Ret)


Ret = Aobj.Substraction(Value1, Value2) # Error
print("Substraction is : ", Ret)
