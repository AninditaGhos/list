#Write a Python program to join two given list of lists of same length, element wise.
#Original lists:
list=[[10, 20], [30, 40], [50, 60], [30, 20, 80]]
list2=[[61], [12, 14, 15], [12, 13, 19, 20], [12]]
i=0
while i<len(list):
    print(list[i]+list2[i],end=",")
    i+=1