#Given the start and end of a range, write a Python program to print all negative numbers in a given
#range.
#Example:
#Input: start = -4, end = 5
#Output: -4, -3, -2, -1
#Input: start = -3, end = 4
#Output: -3, -2, -1
num=int(input("Enter the number: "))
num1=int(input("Enter the number: "))
while num<=num1:
    if num<0:
        print(num,end=",")
    num+=1