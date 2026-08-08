class Base1:   
    def fun(self):
        print("Inside Base1 Fun")

class Base2:   
    def gun(self):
        print("Inside Base2 Gun")
        
class Derived(Base1, Base2):
    def son(self):
        print("Inside Derived son")


dobj = Derived()
dobj.fun()
dobj.son()
dobj.gun()