#-----------------------------------
#                LIST          TUPLE
#-----------------------------------
# Ordered        Yes            No
# Indexed        Yes            No
# Mutable        Yes            No(change hot nahi)
# Hetrogenous    Yes            Yes
# (Multiple datatype theu shakto)
#-----------------------------------
#data is immutable manje je change hot nahi 


def main():
    Data1=[10,3.14,True,"Pune"] #List
    Data2=(10,3.14,True,"Pune") #tuple
    
    
    print(Data1)
    print(Data2)
    
    print(Data1[0])
    print(Data2[0])

if __name__ == "__main__":
    main()
    