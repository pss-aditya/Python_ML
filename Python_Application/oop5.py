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
        print(Demo.Value1)
    
    @classmethod
    def gun(cls):
        print("Inside instance method named as gun")
        #print(Demo.No1) not allowed 
        #print(Demo.No2) not allowed
        print(cls.Value1)
        print(cls.Value2)

#call with object  
dobj1 = Demo()      
dobj1.gun()
