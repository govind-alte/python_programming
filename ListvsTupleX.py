#----------------------------------------------
#                 List        Tuple
#ordered          yes          yes
#indexed           yes          yes
#mutable           yes          no
#Heterogeneous      yes          yes
def main():
    data1=[10,3.14,True,"pune"]#list
    data2=(10,3.14,True,"pune")#tuple
    
    print(data1)
    print(data2)

    print(data1[0])
    print(data2[0])


if __name__=="__main__":
    main()
    