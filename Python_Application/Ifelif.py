print("---Ticket Pricing software---")
print("Please Enter your Age")
Age=int(input())

if(Age <= 5):
    print("You are free")
elif(Age>5 and Age <= 18):
    print("Price:900")
elif(Age >18 and Age <=40):
    print("price:1200")
else:
    print("price:500")          
