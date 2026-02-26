# 5)Check string is Pallindrome or not

a = 'naman'
b = ''

for i in range(len(a),-1,-1):
    b = b+ a[i]
if b==a:
    print('the entered string is pallindrome')
else:
    print('not a pallindrome')