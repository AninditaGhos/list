paisa= [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
i=0
Crorepati=0
Lakhpati=0
Dilwale=0
while i<len(paisa):
    if paisa[i]<100000:
        Dilwale+=1
    if paisa[i]>99999 and paisa[i]<10000000:
        Lakhpati+=1
    if paisa[i]>9999999 :
        Crorepati+=1
    i+=1
print("Crorepati=",Crorepati)
print("Lakhpati=",Lakhpati)
print("Dilwale=",Dilwale)