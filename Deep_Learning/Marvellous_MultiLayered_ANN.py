import numpy as np
import math

#-----------------------------------------------------------------------
# Step 1 : Input Layer 
#-----------------------------------------------------------------------

x1 = 2.0
x2 = 3.0
print("\nInput Layer ")
print("Input Features : X (This are the Features)")
print(f"x1 = {x1}")
print(f"x2 = {x2}")

#-----------------------------------------------------------------------
# Step 2 : Hidden Layer 
#-----------------------------------------------------------------------

print("\nHidden Layer (2 Neurons)")
print("--- Hidden Neuron 1 ---")
w11 = 0.5
w12 = -0.2
b1 = 0.1
print("Weights :")
print(f"w11 : {w11}")
print(f"w12 : {w12}")

print("Bias :")
print(f"b1  :{b1}")

print("Weighed Sum :")
print("z1 = (x1*w11 + x2*w12) + b1")
z1 = (x1*w11) + (x2*w12) + b1
print("Weighted Sum : z1 ", z1)

h1 = max(0,z1)
print("Output of Hidden neuron : ", h1)

###########################################################

print("\n--- Hidden Neuron 2 ---")
w21 = 0.8
w22 = 0.4
b2 = -0.1
print("Weights :")
print(f"w11 : {w21}")
print(f"w12 : {w22}")

print("Bias :")
print(f"b1  :{b2}")

print("Weighed Sum :")
print("z2 = (x1*w21 + x2*w22) + b2")
z2 = (x1*w21) + (x2*w22) + b2
print("Weighted Sum : z2 ", z2)

#ReLU
h2 = max(0,z2)
print("Output of Hidden neuron : ", h2)

#-----------------------------------------------------------------------
# Step 3 : Output  Layer 
#-----------------------------------------------------------------------

print("\nOutput Layer ")
w_out1 = 1.0
w_out2 = -1.5
b_out = 0.2

print("Weights :")
print(f"w_out1 : {w_out1}")
print(f"w_out2 : {w_out2}")

print("Bias :")
print(f"b_out  :{b_out}")

print("Weighed Sum :")
print("z_out = (h1*w_out1 + h2*w_out2) + b_out")
z_out = (h1*w_out1) + (h2*w_out2) + b_out
print("Weighted Sum : z_out ", z_out)

# sigmoid
z = 1 / (1 + math.exp(-z_out))
print("\n------------------------------------------------")
print("-------------- Neural Network Summary ----------")
print("------------------------------------------------")

print("\nInput Layer ")
print(f"x1 = {x1}")
print(f"x2 = {x2}")

print("\nHidden Layer")
print(f"h1 : {h1}")
print(f"h2 : {h2}")
print("\nOutput Layer ")
print(f"z : {z}")

print("\nPrediction of Neural Network")

if(z>=0.5):
    print("Predicted as POSITIVE CLASS")
else:
    print("Predicted as NEGATIVE CLASS")
