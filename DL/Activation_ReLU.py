import numpy as np

def ReLU(z):
    return max(0,z)

def marvellous_Neuron_firword(inputs,weights,bias):
    print("input are :",inputs)
    print("w",weights)
    print("b",bias)
    #z=sum(w*x for w,x in zip(weights,inputs))+bias
    z=0
    for i in range(len(inputs)):
        z=z+(inputs[i]*weights[i])
        z=z+bias
    
    print("wights sum: ",z)
    y=ReLU(z)
    return y


def main():
    print("marvellous Neural network")
    inputs=[1.0,2.0,3.0]
    weights=[0.6,0.4,-0.2]
    bias=0.5
    results=marvellous_Neuron_firword(inputs,weights,bias)
    print("predicted result:",results)
   


if __name__=="__main__":
    main()
