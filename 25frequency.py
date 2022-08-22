#Given a List, extract all elements whose frequency is greater than K.
#Input: test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8], K = 3
#Output: [4, 3]
#Explanation: Both elements occur 4 times.
#Input: test_list = [4, 6, 4, 3, 3, 4, 3, 4, 6, 6], K = 2
#Output: [4, 3, 6]
#Explanation: Occur 4, 3, and 3 times respectively.

list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
k=3
i=0
list1=[]
while i < len(list):
    frequency=list.count(i)
    if frequency > k and i not in list1:
        list1.append(i)
    i+=1
print(list1)

list = [4, 6, 4, 3, 3, 4, 3, 4, 6, 6]
k=2
i=0
list1=[]
while i < len(list):
    frequency = list.count(i)
    if frequency > k and i not in list1:
        list1.append(i)
    i+=1
print(list1)