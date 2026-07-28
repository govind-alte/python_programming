def checkEven (No):
    return(No%2==0)


def main ():
    data = [13 ,12,8,10,11,20]

    print("input data is :",data)
    
    Fdata=list(filter(checkEven,data))

    print("data after filter:",Fdata)

if __name__=="__main__":
    main()    