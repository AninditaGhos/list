#For example, if we give 9119 the function should return 811181, 
# as the square of 9 is 81 and square of 1 is 1.
list=["9","1","1","9"]
i=0
list_2=""
while i<len(list):
    a=list[i]
    b=(int(a)*int(a))
    list_2=list_2+str(b)
    i+=1
print(list_2)