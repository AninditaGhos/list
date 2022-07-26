#Write a Python program to join adjacent members of a given list.
#Original list:
#['1', '2', '3', '4', '5', '6', '7', '8']
#Join adjacent members of a given list:
#['12', '34', '56', '78']
#Original list:
#['1', '2', '3']
#Join adjacent members of a given list:
#['12']
list=['1', '2', '3', '4', '5', '6', '7', '8']
i=0
list2=[]
while i<len(list):
    a=(list[i]+list[i+1])
    list2.append(a)
    i+=2
print(list2)