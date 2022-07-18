#Given start and end of a range, write a Python program to print all positive numbers in given range.
#Example:
#Input: start = -4, end = 5
#Output: 0, 1, 2, 3, 4, 5
#Input: start = -3, end = 4
#Output: 0, 1, 2, 3, 4
num=int(input("Enter the number: "))
num1=int(input("Enter the number: "))
while num<=num1:
    if num>=0:
        print(num,end=",")
    num+=1