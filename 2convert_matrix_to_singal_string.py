#Convert Character Matrix to single String;
#The original list is: [ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
#The String after join: gfgisbest
list=[ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
i=0
list1=""
while i<len(list):
    j=0
    while j<len(list[i]):
        list1=list1+(list[i][j])
        j+=1
    i+=1
print(list1)
