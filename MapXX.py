checkEven=lambda No:(No%2==0)

increment=lambda No: No+1

def main ():
    data = [13 ,12,8,10,11,20]

    print("input data is :",data)
    
    Fdata=list(filter(checkEven,data))

    print("data after filter:",Fdata)

    Mdata=list(map(increment ,Fdata))
    print("data after Mdata:",Mdata)

if __name__=="__main__":
    main() 