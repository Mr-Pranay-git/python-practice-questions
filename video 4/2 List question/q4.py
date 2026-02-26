# 4)find the greatest element and print its index too.
# {2, 96, 69, 77, 145, 20} = Max element = 145 found at 4 index

a =  [2, 96, 69, 77, 145, 20]

Max = 0
index = 0
for i in range(len(a)):
    if a[i]>Max:
        Max = a[i]
        index = i
    else:
        continue

print(f'Greatest = {Max} \nindex = {index}')