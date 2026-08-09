import numpy as np 
import math
def MarvellousEucDistance(P1, P2):
    Answer = math.sqrt((P1['X']-P2['X'])**2 + (P1['Y']- P2['Y'])**2)
    return Answer
    
def MarvellousKNNClassifier(K = 3):
    Border = "-"*50
    Data = [
        {'point' : 'A', 'X' : 1, 'Y' : 2, 'label' : 'Red' },
        {'point' : 'B', 'X' : 2, 'Y' : 3, 'label' : 'Red' },
        {'point' : 'C', 'X' : 3, 'Y' : 1, 'label' : 'Blue'},
        {'point' : 'D', 'X' : 5, 'Y' : 6, 'label' : 'Blue'},
        {'point' : 'E', 'X' : 6, 'Y' : 6, 'label' : 'Blue'},
        {'point' : 'F', 'X' : 3, 'Y' : 4, 'label' : 'Red' },
        {'point' : 'G', 'X' : 3, 'Y' : 2, 'label' : 'Red' }
    ]
    
    print(Border)
    print("User Defined KNN Classifier")
    print(Border)
    
    for i in Data:
        print(i)
        
    print(Border)
    
    new_point = {'X' : 3, 'Y' : 3}
    
    print("Distances of all Points are : ")
    print(Border)
    
    for D in Data :
        D['distance'] = MarvellousEucDistance(D,new_point)
         
    for D in Data:
        print(D) 
         
    print(Border)
    
    sorted_data = sorted(Data,key = lambda item : item ['distance'])
    
    print(Border)
    print("Sorted Data is :")
    print(Border)
    
    for D in sorted_data:
        print(D)
    print(Border)
    
   
    
    nearest = sorted_data[:K]
    
    print(Border)
    print("Nearest member are :")
    print(Border)
    
    for D in nearest:
        print(D)
    
    print(Border)
    
    # Voting
    votes = {}
    
    for neighbors in nearest:
        label = neighbors['label']
        votes[label] = votes.get(label,0) + 1
        
    print(Border)
    print("Voting Result is :")
    for D in votes:
        print("Name : ",D,"Number of votes  :",votes[D])
    print(Border)
    
    iMax = 0
    Name = ""
    
    for D in votes:
        if votes[D] > iMax :
            iMax = votes[D]
            Name = D
    print("Final Prediction is :", Name)   
    print(Border)

    
def main():
    MarvellousKNNClassifier(5)
      
if __name__ == "__main__":
    main()