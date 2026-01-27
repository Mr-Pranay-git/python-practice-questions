# 3)Count all letters, digits, and special symbols from string
# Given: strl = "P@#yn26at^&i5ve"
# Expected Outcome:
# Total counts of chars, digits, and symbols
# Chars = 8
# Digits = 3
# Symbol = 4

str = "P@#yn26at^&i5ve"
Char=0
dig=0
spchr=0

for i in str:
    if i.isdigit():
        dig +=1
    elif i.isalpha():
        Char +=1
    else:
        spchr +=1
print(f'Character = {Char} \n Digit={dig} \n Special Character= {spchr}')