#Write a Python program to remove duplicates from a list. 
list=[2,3,4,5,77,3,4,1,88,4,88]
i=0
list1=[]
while i<len(list):
    if list[i] not in list1:
        list1.append(list[i])
    i+=1
print(list1)