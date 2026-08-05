from sklearn import tree
#Rough=1
#Smooth=0


#Tennis=1
#Criket=0
def main():
    print("ball classification")

    Independent=[[35,1],[47,1],[90,0],[45,1],[90,0],[92,0],[35,1],[35,1],[35,1],[96,0],[45,1],[101,0],[45,1],[101,0],[45,1]]
    dependent=[1,1,2,1,2,2,1,1,1,2,1,2,1,2,1]

    print("independent:",Independent)
    print("dependent:",dependent)

if __name__=="__main__":
    main()    