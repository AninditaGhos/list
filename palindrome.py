# Given an integer x, return true if x is palindrome integer.
#An integer is a palindrome when it reads the same backward as forward.
#For example, 121 is a palindrome while 123 is not.
# Example 1:
#Input: x = 121
#Input x= 10101
#Output: true
#Explanation: 121 reads as 121 from left to right and from right to left.
list=[1,2,1]
i=-1
l=0-len(list)
c=[]
while i>=l:
    c.append(list[i])
    i-=1
print(c)
if list==c:
    print("Palindrome")
else:
    print("Not palindrome")