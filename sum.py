#Write a Python program to sum all the items in a list. 
num=[1,2,3,4,5,6,7,8,9]
i=0
sum=0
while i<len(num):
    sum=sum+num[i]
    i+=1
print(sum)