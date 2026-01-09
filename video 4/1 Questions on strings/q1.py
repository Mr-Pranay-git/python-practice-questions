# 1)Print string in reverse, its length, in uppercase, lowercase and
# copy into another string.

a = 'Hello Lets Start'
print(a.upper())
print(a.lower())

name = ''
for i in range (len(a)-1,-1,-1):
    name += a[i]

print(name)