#Write a Python program to add a number to each element
#  in a given list of numbers.
#Original lists=[3, 8, 9, 4, 5, 0, 5, 0, 3]
#Add 3 to each element in the said list:
#[6, 11, 12, 7, 8, 3, 8, 3, 6]
#Original lists:
#[3.2, 8, 9.9, 4.2, 5, 0.1, 5, 3.11, 0]
#Add 0.51 to each element in the said list:
#[3.71, 8.51, 10.41, 4.71, 5.51, 0.61, 5.51, 3.62, 0.51]
#num=int(input("Enter the number:-"))
#lists=[3, 8, 9, 4, 5, 0, 5, 0, 3]
num=float(input("Enter the number:-"))
lists=[3.2, 8, 9.9, 4.2, 5, 0.1, 5, 3.11, 0]
i=0
list=[]
while i<len(lists):
    count=0
    count=count+(lists[i]+num)
    list.append(count)
    i+=1
print(list)