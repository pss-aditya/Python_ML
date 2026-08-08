no = 11 #Global Variable

def Display():
    print("From Display  : ", no)
    print("Value of a is :", a)
    pass

def Demo():
    a = 21   #Local Variable
    print("From Demo     : ", no)
    print("Value of a is : ", a)
    pass

Display()
Demo()
