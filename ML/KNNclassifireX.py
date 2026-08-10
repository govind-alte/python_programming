
import numpy as np 
from sklearn.neighbors import KNeighborsClassifier

def main():
   #independent variable
       X=np.array([[1,2],[3,2],[3,1],[5,6]])
   
       Y=np.array(["Red","Red","Blue","Blue"])
       new_point=np.array([3,3])
   
       print("Independent variable is :")
       print(X)
   
       print("Dependent variable is :")
       print(Y)
   
       print("Testing point is :")
       print(new_point)
if __name__=="__main__":
    main()
