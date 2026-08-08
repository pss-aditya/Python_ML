class Demo:
    def __init__(self,A):
        self.no = A
        
    def __add__(self, other):
        print("Inside __add__")
    
obj1 = Demo(11)
obj2 = Demo(21)

print(obj1 + obj2) #obj1.__add__(obj2) ->__add__(obj1,obj2)
        