def BigBazar():
        print("inside BigBazar")

        def Amul():
                print("inside amul Icecrime parlor")



def main():
        BigBazar()#allowed
        BigBazar.Amul() #error
        Amul()#error

if __name__=="__main__":
        main()