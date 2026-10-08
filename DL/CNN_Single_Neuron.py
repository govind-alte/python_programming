import tensorflow as tf

inputs= tf.constant([1.0,2.0,3.0])

weights= tf.constant([0.5,-2.0,0.8])

bias=tf.constant(0.1)

weighted_sum=tf.reduce_sum(inputs*weights)+bias

print("ionputs: ",inputs.numpy())                     #1.0,2.0,3.0
print("weights:",weights.numpy())                     #0.5 ,-2.0,0.8
print("bias:",bias.numpy())                           #1.0
print("weighted_Sum:",weighted_sum.numpy())           #2.6

output= tf.sigmoid(weighted_sum)                      #0.93

print("output is:",output.numpy())                    #0.93







