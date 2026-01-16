# 2) Arrange string characters such that lowercase letters should
# come first in another string.

a = "Hello EVERY oNE"
lower =''
upper =''
for i in range (0,len(a)):
    if a[i].islower():
        lower += a[i]
    elif a[i].isupper():
        upper += a[i]

new_string = lower+upper
print(new_string)
