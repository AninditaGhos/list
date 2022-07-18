#Remove duplicates from a list.
#List = [1,2,3,1,2,2]
#Output: [1,2,3]
list=[1,2,3,1,2,2]
i=0
list_2=[]
while i<len(list):
    if list[i] not in list_2:
        list_2.append(list[i])
    i+=1
print(list_2)