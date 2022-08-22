#Write a Python program to split a given list into specified sized chunks.
#Original list:
#[12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
#Split the said list into equal size 3
#[[12, 45, 23], [67, 78, 90], [45, 32, 100], [76, 38, 62], [73, 29, 83]]
#Split the said list into equal size 4
#[[12, 45, 23, 67], [78, 90, 45, 32], [100, 76, 38, 62], [73, 29, 83]]

list=[12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
i=0
list1=[]
num=int(input("ENter the number:- "))
while i<len(list):
    list1.append(list[i:i+num])
    i+=3
print(list1)