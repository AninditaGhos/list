#Input: list1 = [1,2,4], list2 = [1,3,4]
#Output: [1,1,2,3,4,4]
list1=[1,2,3]
list2=[1,3,4]
i=0
list3=[]
while i< len(list1):
    list3.append(list1[i])
    i+=1
j=0
while j<len(list2):
    list3.append(list2[j])
    j+=1
print(list3)
list3.sort()
print(list3)