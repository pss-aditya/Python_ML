import time
import threading

def SumEven(No):
    print("TID OF SumEven thread is :" , threading.get_ident())
   
     
def SumOdd(No):
    print("TID OF SumOdd thread is :" , threading.get_ident())
        

def main():
    print("TID OF main thread is :" , threading.get_ident())
   
    start_time = time.perf_counter()
    
    tobj1 = threading.Thread(target=SumEven, args = (100000000, ))
    tobj1.start()
    
    tobj2 = threading.Thread(target=SumOdd, args = (100000000, ))
    tobj2.start()
    
    tobj1.join()
    tobj2.join()

    end_time = time.perf_counter()
    
    print(f"Time taken was {end_time - start_time: .4f} seconds")
    
if __name__ =="__main__":
    main()
    