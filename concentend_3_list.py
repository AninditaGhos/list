#Write a Python program to concatenate element-wise three given lists.
#Original lists:
#['0', '1', '2', '3', '4']
#['red', 'green', 'black', 'blue', 'white']
#['100', '200', '300', '400', '500']
#Concatenate element-wise three said lists:
#['0red100', '1green200', '2black300', '3blue400', '4white500']
list=['0', '1', '2', '3', '4']
list1=['red', 'green', 'black', 'blue', 'white']
list2=['100', '200', '300', '400', '500']
list3=[]
i=0
while i<len(list):
    a=(list[i])
    b=a+(list1[i])
    c=b+(list2[i])
    list3.append (c)
    i+=1
print(list3)