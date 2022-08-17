list=[1,1,0,1]
i=-1
l=0-len(list)
decimal=0
power=0
while i>=l:
    if list[i] == 1:
        a=list[i]
        b=a*2
        decimal=decimal+b**power
    else:
        pass
    power=power+1
    i-=1
print(decimal)