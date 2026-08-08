print("-------------------------------------")
print("-------Ticket Pricing Software-------")
print("-------------------------------------")
Age = int(input ("Enter your age:"))

if(Age <= 5):
    print("Your ticket is Free")
elif(Age > 5 and Age <= 18):
    print("Your ticket price is 900$ ")
elif(Age >18 and Age <= 40):
    print("Your ticket price is 1200$ ")
else:
    print("Your ticket price is 500&")