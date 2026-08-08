import pandas as pd 

def main():
   Data = {
       "Name"     : ["Aditya","Vipul","Adarsh"],
       "Age"      : [27,28,25],
       "City"     : ["Pune", "Kolhapur","Satara"]
       
   }
   
   dobj = pd.DataFrame(Data)
   print(dobj)
   # print(dobj[0]) ---> not allowed
   print(dobj["Age"])

if __name__ == "__main__":
    main()