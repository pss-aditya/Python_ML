def AreaOfCircle(Radius,PI=3.14):
    Ans = PI* Radius *Radius
    return Ans
    
def main():
    Ret = AreaOfCircle(10.5)
    print("Area of Circle is:",Ret)
    
    Ret = AreaOfCircle(10.5, 7.12)
    print("Area of Circle is:",Ret)
    

if __name__ == "__main__":
    main()
