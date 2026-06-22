# Question from Assignment

#Program to display Data Type, Memory Address and Size   

import sys

def main():
    X = [1,2,3,4,5]
    print("Datatype of X is:",type(X))
    print("Memory Address of X is:",id(X))
    print("Size of X is:", sys.getsizeof(X))
    print("The values inside X are:", X)
    print("The length of X is:",len(X))

if __name__ =="__main__":
    main()
