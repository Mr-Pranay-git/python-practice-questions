# 4) Write a Python program to combine two dictionary by adding values for common keys.

a = {1:10,2:20,3:30}
b = {3:70,8:30,9:90,1:30}

for i in b.keys():
    if i in a.keys():
        a[i] = a[i] + b[i]
    else:
        a[i] = b[i]
        

print(a)

