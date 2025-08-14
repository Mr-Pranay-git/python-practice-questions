# 4)Accept name and age from the user. Check if the user is a
# valid voter or not.

name = input("Enter your Name : \n")
age = int(input("Enter your Age: \n"))

if (age >=18):
    print(f"{name} is a valid voter \n")
else :
    print(f" {name} your are not eligible for voting")
    
