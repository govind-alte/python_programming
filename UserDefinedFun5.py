#Accept: Multiple parameter
#return: Multiple value

def marvellous(Value1, Value2):
    print("Inside Marvellous:",Value1,Value2)
    return 21,51


def main():
   Ret1, Ret2 =  marvellous(11,20)
   print("Return value :",Ret1, Ret2)

if __name__=="__main__":
        main()