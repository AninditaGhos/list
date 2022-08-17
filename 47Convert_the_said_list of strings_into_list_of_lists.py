#Write a Python program to convert a given list of strings into list of lists.
#Original list of strings:
#['Red', 'Maroon', 'Yellow', 'Olive']
#Convert the said list of strings into list of lists:
#[['R', 'e', 'd'], ['M', 'a', 'r', 'o', 'o', 'n'], ['Y', 'e', 'l', 'l', 'o', 'w'], ['O', 'l', 'i', 'v', 'e']]
list=['Red', 'Maroon', 'Yellow', 'Olive']
i=0
list1=[]
while i<len(list):
    l=list[i]
    l=str(l)
    list2=[]
    j=0
    while j<len(l):
        list2.append(l[j])
        j+=1 
    list1.append(list2)
    i+=1
print(list1)