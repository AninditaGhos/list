#
list=[1,2,1,3,1,4,1,5,1,6]
i=1
while i<len(list)-1:
    if(list[i]+1)==list[i+2]:
        print("Equal")
    else:
        print("Not equal")
    i+=2
    print(list[i])