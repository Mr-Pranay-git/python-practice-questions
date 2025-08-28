#  print factorial of a number 

n = int(input("Enter the number for factorial: "))
# 4*3*2*1
fact = 1
for i in range(n,0, -1):
    fact = i * fact
print(fact)