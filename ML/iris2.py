from sklearn.datasets import load_iris

def main():
    print("-"*30)
    print("iris classification case study ")
    print("-"*30)

    dataset= load_iris()

    #meta data of dataset
    print("independent variables are :")
    print(dataset.feature_names)
    print("Dependent variables are:")
    print(dataset.targat_names)

if __name__=="__main__":
    main()
