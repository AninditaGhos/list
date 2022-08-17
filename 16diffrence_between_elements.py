#Write a Python program to find the difference between elements (n+1th - nth) of a given list of
# numeric
#values.
#Original list:
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Difference between elements (n+1th - nth) of the said list :
#[1, 1, 1, 1, 1, 1, 1, 1, 1]
#Original list:
#list=[2, 4, 6, 8]
#Difference between elements (n+1th - nth) of the said list [2, 2, 2]

#list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list=[2, 4, 6, 8]
i=0
list1=[]
while i<len(list)-1:
     a=list[i]
     b=list[i+1]
     list1.append(b-a)
     i+=1
print(list1)