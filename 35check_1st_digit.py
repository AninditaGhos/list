#Write a Python program to check if first digit/character of each element in a given list
#is same or not.
#Original list:
#[1234, 122, 1984, 19372, 100]
#Check if first digit in each element of the said given list is same or not!
#True
#Original list:
#[1234, 922, 1984, 19372, 100]
#Check if the first digit in each element of the given list is the same or not!
#False
#Original list:
#['aabc', 'abc', 'ab', 'a']
#Check if first character in each element of the said given list is same or not!
#True
#Original list:
#['aabc', 'abc', 'ab', 'ha']
#Check if first character in each element of the said given list is same or not!
#False

list=[1234, 122, 1984, 19372, 100]
i=0
while i<len(list)-1:
    a=str(list[i])
    b=str(list[i+1])
    j=0
    if int(a[j])==int(b[j]):
        print("True")
    else:
        print("False")
    i+=1

list=[1234, 922, 1984, 19372, 100]
i=0
while i<len(list)-1:
    a=str(list[i])
    b=str(list[i+1])
    j=0
    if (a[j])==(b[j]):
        print("True")
    else:
        print("False")
        break
    i+=1


list=['aabc', 'abc', 'ab', 'a']
i=0
while i<len(list)-1:
    a=str(list[i])
    b=str(list[i+1])
    j=0
    if (a[j])==(b[j]):
        print("True")
    else:
        print("False")
    i+=1