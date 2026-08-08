import pandas as pd 

def main():
   Data = {
       "Name"     : ["Aditya","Vipul","Adarsh"],
       "Age"      : [27,28,25],
       "City"     : ["Pune", "Kolhapur","Satara"]
       
   }
   
   print(Data)
   print(type(Data))
   print(Data["Name"])
    

if __name__ == "__main__":
    main()