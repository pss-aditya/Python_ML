class Base:
    def __init__(self):
        print("Inside Base Constructor")


class Derived(Base):
    def __init__(self):
        super().__init__()
        print("Inside Derived Constructor")



dobj = Derived()

#super keyword or function calls the parent class constructor