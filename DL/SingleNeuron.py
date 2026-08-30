import numpy as np

#step1 define input fetures that is X  

                #[x1,x2,x3]
input=np.array([2.0,3.0,4.0])
print("X:",input)

#step 2 define weight W
                # [w1,w2,w3]
weights=np.array([0.5,0.3,0.2])
print("w:",weights)

#step 3 define Bias is b
      #b 
bias =1.0
print("b:",bias)

#step4 calculate weighted sum is z
#z=x1w1 + x2w2 + x3w3 + b

#z=(2.0*0.5) + (3.0*0.3) + (4.0*0.2) + 1.0

z=np.dot(input,weights) + bias
print("z:",z)

# step 5 activation function (ReLU)
def ReLU(x):
    return max(0,x)


#step 6 final output
y=ReLU(z)
print("y:",y)

