#Write a Python program to find the list with maximum and minimum length.
#Original list:
#[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
#List with maximum length of lists:
#(3, [13, 15, 17])
#List with minimum length of lists:
#(1, [0])
list=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
i=0
min=list[0]
max=list[0]
while i < len(list):
    if len(list[i]) < len(min):
        min=list[i]
    if len(list[i]) > len(max):
        max=list[i]
    else:
        pass
    i+=1
print(len(min),min)
print(len(max),max)