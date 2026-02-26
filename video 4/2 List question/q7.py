# 7)Pallindromic List - Write a program to check if elements of an
# List are same or not it read from front or bacExample : arr=[2,3,15,3,2]

a=[2,3,15,3,2]
# b=a[::-1]
# print(b)

# OR

b = []
for i in range(len(a)-1,-1,-1):
    b.append(a[i])

if b == a:
    print("palindrome")
else:
    print("not a palindrome")
