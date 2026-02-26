# 8) how many seprate elements are there in the list excluding repetation.

# l = [1,2,3,55,6,3,2,1]
l=[]
val = int(input("entr the number of elements to store "))
for i in range(val):
    enterd_val =int(input(f'value at index {i}:'))
    l.append(enterd_val)

a = set(l)
print(f'Seperate elements {len(a)}')