class Demo:
    Value1 = 10  #both  value1 and value2 are class variable
    Value2 = 20
        
    def __init__(self):
        self.No1 = 11
        self.No2 = 21
    
    #Instance Method
    def fun(self):
        print("Inside instance method named as fun")
        print(self.No1) #11
        print(self.No2) #21
        print(self.Value1) #10
        print(self.Value2) #20
        print("Hence proved Instance can access both Class variable as well as Instance variable")
        
dobj1 = Demo()
dobj1.fun()