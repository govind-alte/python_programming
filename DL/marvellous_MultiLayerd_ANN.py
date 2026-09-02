import numpy as np
import math


#------------------------------------------------
# step 1 :Input Lyaer 
#------------------------------------------------
x1=2.0
x2=3.0   
print("step 1 :Input Lyaer ")#input layer  store two value  in 
print("input features: X")
print("x1:",x1)
print("x2:",x2)



#------------------------------------------------
# step 2: hidden layer
#------------------------------------------------
print("Hidden layers 2 Neurons")
print("hidden Nuron 1")
w11=0.5
w12=-0.2
b1=0.1
print("weights:")
print("w11:",w11)
print("w12:",w12)

print("bias :")
print("b1:",b1)

print("weights sum:")
print("z1=(x1*w11)+(x2*w12)+b1")

z1=(x1*w11)+(x2*w12)+b1
print("weights sum :",z1)
h1=max(0,z1)
print("output of hidden neurons:",h1)

###############################################

print("hidden Nuron 2")
w21=0.8
w22=0.4
b2=-0.1
print("weights:")
print("w21:",w21)
print("w22:",w22)

print("bias :")
print("b2:",b2)

print("weights sum:")
print("z2=(x1*w21)+(x2*w22)+b2")

z2=(x1*w21)+(x2*w22)+b2
print("weights sum :",z2)
h2=max(0,z2)
print("output of hidden neurons:",h2)



#------------------------------------------------
# step 3 :output layer
#------------------------------------------------
w_out1=1.0
W_out2=-1.5
b_out=0.2

print("output layer:")
print("weights :")
print("w_out1:",w_out1)
print("w_out2:",W_out2)
print("bias:")
print("b_out:",b_out)

z_out=h1*w_out1+h2*W_out2+b_out
print("weighted sum :",z_out)

#Sigmoid
z=1/(1+math.exp(-z_out))
print("---------------------------------------------------")
print("---------------Neural Network Summary---------------")
print("----------------------------------------------------")
print("inport layer")
print("x1:",x1)
print("x2:",x2)

print("Hiddem layer")
print("h1:",h1)
print("h2:",h2)

print("Output layer:")
print("z:",z)

print("prediction of neural network")
if (z>=0.5):
    print("predicted as POSITIVE CLASS")
else:
    print("predicted as NIGATIVE CLASS")


#------------------------------------------------
# step 1 :Input Lyaer 
#------------------------------------------------
