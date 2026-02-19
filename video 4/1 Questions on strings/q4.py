# 4)Count Vowels from given string
a = 'hello my name is mr pandu'

vowel = 0
const = 0
for i in a:
    if i in "AEIOUaeiou":
        vowel += 1
    elif i == ' ':
        continue
    else:
        const +=1
        

print(f"volews= {vowel} \nconsonent= {const} ")