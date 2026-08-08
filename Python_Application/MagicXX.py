class Demo:
    def __init__(self,A):
        self.no = A
        
    def __add__(self, other):
        print("Inside __add__")
        return self.no + other.no
    
    def __sub__(self, other):
        print("Inside __sub__")
        return self.no - other.no
    
    def __mul__(self, other):
        print("Inside __mul__")
        return self.no * other.no
    
    def __truediv__(self, other):
        print("Inside __truedrive__")
        return self.no / other.no
    
    
obj1 = Demo(11)
obj2 = Demo(21)

print(obj1 + obj2) 
print(obj1 - obj2) 
print(obj1 * obj2) 
print(obj1 / obj2) 
        