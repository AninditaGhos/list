#Write a Python program to pair up the consecutive elements of a given list.Original lists:
#[1, 2, 3, 4, 5, 6]
#Pair up the consecutive elements of the said list:
#[[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
#Original lists:
#[1, 2, 3, 4, 5]
#air up the consecutive elements of the said list:
#[[1, 2], [2, 3], [3, 4], [4, 5]]
list=[1, 2, 3, 4, 5, 6]
i=1
list1=[]
while i<len(list):
    list1.append([list[i]-1]+[list[i]])
    i+=1
print(list1)