#Write a Python program to get the largest number from a list
num=[3,33,6,12,34,76,3,45]
i=0
largest=num[0]
while i<len(num):
    if num[i]>largest:
        largest=num[i]
    i+=1
print(largest)