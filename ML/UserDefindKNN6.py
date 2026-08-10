import math
import numpy as np

def MarvellousEucDistance(P1,P2):
    Ans=math.sqrt((P1['X']-P2['X'])**2 +(P1['Y']-P2['Y'])**2)
    return Ans

def MarvellousKNNClassifire():
    border="-"*30
    data=[
        {'point':'A','X':1,'Y':2,'label':'Red'},
        {'point':'B','X':2,'Y':3,'label':'Red'},
        {'point':'C','X':3,'Y':1,'label':'Blue'},
        {'point':'D','X':5,'Y':6,'label':'Blue'}
    ]
    print(border)
    print("marvellous  KNN classifire")
    print(border)


    for i in data:
        print(i)

    print(border)
    new_point={'X':3,'Y':3}


    print("distancees all poinr:")


    for d in data:
        d['distance']=(MarvellousEucDistance(d,new_point))

    for d in data:
        print(d)   


    sorted_data=sorted(data,key=lambda item: ['distance'])


    print(border)
    print("sorded data: ")
    for d in sorted_data:
        print(d)   



          


def main():
    MarvellousKNNClassifire()
if __name__=="__main__":
    main()
