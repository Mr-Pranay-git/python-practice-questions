# Accept a number and check if it a perfect number or not.
# A number whose sum of factors(excluding number itself) = Number 
# ex- 6 = 1,2,3 = 6

n = int(input("Enter your number "))
sum =0
for i in range (1,n):
    if n%i ==0:
        sum = sum + i 

if n == sum:
    print('yes, is a perfect number')
else:
    print("the  number is not a perfrct")