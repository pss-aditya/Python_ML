class Base:   
    def fun(self):
        print("Inside Base Fun")


class Derived(Base):
    def son(self):
        print("Inside Derived son")


dobj = Derived()
dobj.fun()
dobj.son()