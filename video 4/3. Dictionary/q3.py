# 3) count the frequency of each elements in a list

a = [1,1,4,4,2,2,2,3,2,3,2,3,5,5,6,4,12,3,57]
dict = {}
for i in a:
    if i in dict.keys():
        dict[i] = dict[i] + 1
    else:
        dict[i] = 1 

print(dict)