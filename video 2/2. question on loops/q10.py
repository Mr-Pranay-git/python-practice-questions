# 0) Accept a number and check if it is a pallindromic number
# (If number and its reverse are equal)
# Ex - 12321 - Ret-verse - 12321

n = int(input("Enter the number "))
org_no = n 
rev = 0
while n>0 :
    z = n%10
    rev = rev* 10 + z
    n= n//10

if rev == org_no:
    print("paladromic number")
else :
    print("not a palandromic number")