#Count unique values inside a list.
#input_list = [1, 2, 2, 5, 8, 4, 4, 8]
#Count = 5 #because [1,2,5,8,4] are unique values.
input_list = [1, 2, 2, 5, 8, 4, 4, 8]
list_2=[]
i=0
count=0
while i<len(input_list):
    if input_list[i] not in list_2:
        list_2.append(input_list[i])
        count=count+1
    i+=1
print(count)