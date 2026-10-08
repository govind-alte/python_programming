import tensorflow as tf

weight =tf.Variable(5.0)
print("initial weight value:",weight.numpy())#5.0

weight.assign(10.0)
print("updated weight :",weight.numpy())#10.0

weight.assign_add(2.5)
print("updated weight :",weight.numpy())#12.5 updated value add 10.0 + 2.5 = 12.5

weight.assign_sub(1.5)
print("updated weight :",weight.numpy())#11.0  subtraction 12.5 - 1.5 = 11.0
