# 3) Print positive and negative elements of an List in seprate lists

a = [1,-10, -49, 9 , 6,-5]

pos =[]
neg =[]

for i in a:
    if i>0:
        pos.append(i)
    elif i<0:
        neg.append(i)

print(f'positive ={pos} \n negative ={neg}')