import os
import time
import multiprocessing

def SumEven(No):
    print(f"PID of SumEven : {os.getpid()} PPID of :{os.getppid()}")
    Sum = 0 
    
    for i in range(2,No,2):
        Sum = Sum + i
    print("Summation of Even is ------------------> :", Sum)
     
def SumOdd(No):
    print(f"PID of SumOdd : {os.getpid()} PPID of  :{os.getppid()}")
    Sum = 0
    
    for i in range(1,No,2):
        Sum = Sum + i
    print("Summation of Even is -----------------> :", Sum)
        

def main():
    print(f"PID of Main: {os.getpid()} PPID of main  : {os.getppid()}")
    start_time = time.perf_counter()
    
    tobj1 = multiprocessing.Process(target=SumEven, args = (100, ))
    tobj1.start()
    
    tobj2 = multiprocessing.Process(target=SumOdd, args = (100, ))
    tobj2.start()
    
    tobj1.join()
    tobj2.join()

    end_time = time.perf_counter()
    
    print(f"Time taken was {end_time - start_time: .4f} seconds")
    
if __name__ =="__main__":
    main()
    