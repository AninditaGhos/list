marks = [[78, 76, 94, 86, 88],
[91, 71, 98, 65, 76],
[95, 45, 78, 52, 49]]
i=0
year=1
while i<len(marks):
    j=0
    sum=0
    average=0
    while j<len(marks[i]):
        sum=sum+marks[i][j]
        j+=1
    print(sum)
    average=sum/len(marks[i])
    print("average of the",year,"year is:-",average)
    i+=1
    year+=1