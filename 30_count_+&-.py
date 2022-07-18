#Given a list of numbers, write a Python program to count positive and negative numbers in a List.
#Example:
#list1 = [2, -7, 5, -64, -14]
#Output: pos = 2, neg = 3
#Iist2 = [-12, 14, 95, 3]
#Output: pos = 3, neg = 1
#list1 = [2, -7, 5, -64, -14]
list1 = [-12, 14, 95, 3]
i=0
positive=0
negative=0
while i<len(list1):
    if list1[i]<0:
        negative+=1
    elif list1[i]>0:
        positive+=1
    else:
        pass
    i+=1
print(positive)
print(negative)