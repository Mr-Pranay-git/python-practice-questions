# 8) 

n = int(input("Enter the number "))

count =0
for i in range(1,n+1):
    if n%i == 0 :
        count = count+1
    
if  count == 2:
    print("the number is prime")
else:
    print("composit numbers")
