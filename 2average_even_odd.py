#Write a code that works for any list, it shows the two averages as the output.
#  One is the average  of even numbers and the other 
# is the average of odd numbers from the given list.
elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
even=0
num1=0
odd=0
num2=0
i=0
while i<len(elements):
    if elements[i]%2==0:
        num1+=1
        even+=elements[i]
    else:
        num2+=1
        odd+=elements[i]
    i+=1
print("Even_average=",even/num1)
print("Odd_average=",odd/num2)