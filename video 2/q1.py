# Accept two numbers and print the greatest between them

a = int(input("enter first no \n"))
b = int(input("enter second number \n"))

if(a>b):
    print(f'{a} is greater')
elif b>a:
    print(f'{b} is greater')
else:
    print("both numbers are equal")