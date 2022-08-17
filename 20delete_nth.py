#Write a function that takes one argument “n” and delete that many elements from the list.
#delete_nth ([1,1,1,1],2) # return [1,1]
#delete_nth ([20,37,20,21],1) # return [20,37,21]

#list=[20,37,20,21]
#i=0
#list1=[]
#while i<len(list):
#    if list[i] not in list1:
#        list1.append(list[i])
#    i+=1
#print(list1)

num=int(input("Enter the number: "))
list=[1,1,1,1]
i=0
list1=[]
while i<num:
    list1.append(list[i])
    i+=1
print(list1)