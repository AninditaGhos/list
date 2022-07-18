#All together
#Write a code that works for all lists. It should print the output as the following like for all 
#the odd numbers and all the even numbers and for all the numbers in the given list, it should
#calculate the following :
#count
#sum
#average
#and then print it.

elements=[23,14,56,12,19,9,15,25,31,42,43]
i=0
count_even=0
even=0
count_odd=0
odd=0
average_even=0
average_odd=0
sum=0
average_all_num=0
while i<len(elements):
    sum+=elements[i]
    if elements[i]%2==0:
        count_even+=1
        even+=elements[i]
    else:
        count_odd+=1
        odd+=elements[i]
    i+=1
average_even=even/count_even
average_odd=odd/count_odd
average_all_num=sum/len(elements)
print("count of odd numbers=",count_odd)
print("count of even numbers",count_even)
print("count of all the numbers=",len(elements))
print("sum of odd numbers=",odd)
print("sum of even numbers=",even)
print("sum of all the numbers=",sum)
print("average of odd numbers=",average_odd)
print("average of even numbers=",average_even)
print("average of all the numbers=",average_all_num)