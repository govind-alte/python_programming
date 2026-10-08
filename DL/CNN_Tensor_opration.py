import tensorflow as tf
tensor1=tf.constant(10,20,30)
twnsor2=tf.constant([1,2,3])

addition=tf.add(tensor1,twnsor2)
print("add:",addition)#11 ,22,33

Subtraction=tf.add(tensor1,twnsor2)
print("Sub:",Subtraction)#9,18,27

multiplication=tf.add(tensor1,twnsor2)
print("multi:",multiplication)#10,40,90

division=tf.add(tensor1,twnsor2)
print("div :",division)#10.0,10.0,10.0

square=tf.square(tensor1)
print("square:",square)#100,400,900

sum=tf.reduce_sum(tensor1)
print("reduce sum",sum)#60


mean=tf.reduce_mean(tensor1)
print("mean is :",mean)#20

3/




