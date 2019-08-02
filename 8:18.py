age = [5,12,3,56,24,78,1,15,44]
index = 0
now= 0
next= now+1
sumNew =0
sumOld=0
for index < age[length-1]:
    sumNew = age[now]+ age[next]
    sumOld= sumNew+sumOld
    index+=1
    next+=1
    now+=1
print(sumOld)
