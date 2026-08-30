import numpy as np

def ReLU(z):
    return max(0,z)

def Marvellous_Neuron_Forward(inputs,weights,bias):
    print("\nInputs are  (X): ", inputs)
    print("\nWeights are (W): ", weights)
    print("\nBias are     (b): ", bias)
    
    z = 0
    for i in range(len(inputs)):
        z = z + (inputs[i] * weights[i])
    
    z = z + bias
    #z = sum(w * x for w, x in zip(weights, inputs)) + bias
    print("\nWeighted Sum (z): ", z)
    
    y = ReLU(z)
    
    return y
    

def main():
    print("---------------- Marvellous Neural Network -------------")
    
    inputs = [1.0,2.0,3.0]
    weights = [0.6,0.4,-0.2]
    bias = 0.5
    
    result = Marvellous_Neuron_Forward(inputs,weights,bias)
    
    print("\nPredicted Result : ", result)

if __name__ == "__main__":
    main()