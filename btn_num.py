#Write a code, that counts the numbers between 20 and 40 and then print its count.
numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0
btn_num=0
while i<len(numbers):
    if numbers[i]>20 and numbers[i]<40:
        btn_num=btn_num+1
    else:
        pass
    i+=1
print("The count of  number between 20 to 40 is: " +str(btn_num))