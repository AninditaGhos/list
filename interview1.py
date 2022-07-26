#Write a python program to find the count of an elememt appearing in a list 
#take the element as user input.
num=int(input("Enter the number:-"))
list=[1,2,4,2,7,9,3,3,8,7,2]
i=0
count=0
while i<len(list):
    if num==list[i]:
        count+=1
    else:
        pass
    i+=1
print(count)