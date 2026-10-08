import tensorflow as tf

#scaler tensor  (0D tensor)
scalar_tensor=tf.constant(11)
print("scalor tensor:",scalar_tensor)


# 1D tnsor(vector)
vector_tensor=tf.constant(11,21,51,101)
print("Vector tensor:",vector_tensor)


#2D tensor (matrix)
matrix_tensor=tf.constant([[10,20,30],[40,50,60]])
print("matrix tensor:",matrix_tensor)

#3D tensor  
tensor_3D=tf.constant([
    [[1,2],[3,4]],2 
    
    [[5,5],[6,6]],
    [[7,8],[9,10]]

])
print("3D :",tensor_3D)


