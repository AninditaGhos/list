#Write a code that prints the maximum in this list.
#numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]

numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0
max=numbers[0]
while i<len(numbers):
    if numbers[i]>max:
        max=numbers[i]
    i=i+1
print(max)