class Demo:
    Value1 = 10  #both  value1 and value2 are class variable
    Value2 = 20
        
    def __init__(self):
        self.No1 = 11
        self.No2 = 21
    
    #Instance Method
    def fun(self):
        print("Inside instance method named as fun")
        print(self.No1) 
        print(self.No2) 
        print(Demo.Value1) #to access class variable there are 2 ways see oop1.py line by 14 we used self and here demo thename of class
        print(Demo.Value2) 
       
#object creation dobj       
dobj1 = Demo()
dobj1.fun()