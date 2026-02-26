# 5) Find the second greatest element and print its index too.
# {2, 96, 69, 77, 145, 20} = Max element = 145 found at 4 index

a = [1,5,2,4,9,10,15,14,5]
max = 0
max2 = 0
index1 =0

for i in range(len(a)):
    if a[i]>max:
        max2 = max
        index2= index1
        max = a[i]
        index1 = i
        
    elif a[i]>max2:
        max2 = a[i]
    
    
print(f'Greatest = {max}, index = {index1} \nSecond Greatest = {max2}, index = {index2} ')