import time
import threading

def SumEven(No):
    Sum = 0 
    
    for i in range(2,No,2):
        Sum = Sum + i
    print("Summation of Even is :", Sum)
     
def SumOdd(No):
    Sum = 0
    
    for i in range(1,No,2):
        Sum = Sum + i
    print("Summation of Even is :", Sum)
        

def main():
    start_time = time.perf_counter()
    
    tobj1 = threading.Thread(target=SumEven, args = (100000000, ))
    tobj1.start()
    
    tobj2 = threading.Thread(target=SumOdd, args = (100000000, ))
    tobj2.start()

    end_time = time.perf_counter()
    
    print(f"Time taken was {end_time - start_time: .4f} seconds")
    
if __name__ =="__main__":
    main()
    