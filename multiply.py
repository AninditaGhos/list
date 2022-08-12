# Write a Python program to multiply all the items in a list.
num=[3,5,6,7,2]
i=0
mul=1
while i<len(num):
    mul=mul*num[i]
    i+=1
print(mul)