#List product excluding duplicates.
#List = [6,1,3,5,6,3,1]
#Output: 90
list = [6,1,3,5,6,3,1]
list_2=[]
i=0
while i<len(list):
    if list[i] not in list_2:
        list_2.append(list[i])
    i+=1
print(list_2)
j=0
product=1
while j<len(list_2):
    product=product*list_2[j]
    j+=1
print(product)
