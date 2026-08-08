class Arithematic:
    def Addition(self,No1 ,  No2):
        Ans = No1 + No2 
        return Ans

    def Substraction(self,No1 , No2):
        Ans = No1 - No2
        return Ans
    
Aobj = Arithematic()

Value1 = int(input("Enter the First   Number : "))
Value2 = int(input("Enter the  Second Number : "))
  
# Ret = Addition(Aboj.Value1, Value2)  
Ret = Aobj.Addition(Value1, Value2) 
print("Addition is : ", Ret)

# Ret = Substraction(Aboj.Value1, Value2)
Ret = Aobj.Substraction(Value1, Value2) 
print("Substraction is : ", Ret)
