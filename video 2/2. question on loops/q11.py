# 11) strong number

# n = 145

# sum = 0
# while n>0:
#     digit = n%10
#     for i in range(1,digit):
#          digit = digit * i

#     sum = sum + digit
#     n = n//10

# print(sum)

# 4! = 4*3*2*1



n = int(input("Check your number is strong ?  "))
temp = n
sum = 0

while temp>0:
   digit = temp%10
   fact= 1
   for i in range(1,digit+1):
      fact *= i
   sum += fact 
   temp =temp//10

if sum == n:
   print("the number is strong")
else:
   print("the nunber is not a strong number")