#Write a Python program to get the smallest number from a list.
num=[3,33,6,12,34,76,2,45]
i=0
smallest=num[0]
while i<len(num):
    if i<smallest:
        smallest=num[i]
    i+=1
print(smallest)