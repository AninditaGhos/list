#Write a program to check the alternate elements are same or not 
# from the first elements. 
list=[1,2,1,3,1,4,1,5,1,6]
i=0
while i<len(list)-2:
    if list[i]==list[i+2]:
        print("same")
    else:
        print("not same")
    i+=2