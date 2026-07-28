def main():
    Ans=0

    try:
        print("Enter first number")
        No1=int(input())

        
        print("Enter Second number")
        No2=int(input())

        Ans=No1 / No2
        print("Division is succesful")

    except ZeroDivisionError as Zobj:
        print("Exceptioan occured due to second operand is zero:",Zobj)  


    except ValueError as vobj:
        print("Exception ocuured due to invalid data typr:",vobj)

    except Exception as eobj:                  #handle all the error one time 
        print("Exception ocuured :",eobj)  

    finally:
        print("inside finally block:")      


    print("Result is :",Ans)

if __name__=="__main__":                                                                 
    main()