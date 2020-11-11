import random
#r=int(random(1,100))
#print(r)
w=int()
i=int()
s=[]
while w!=99:
    w=random.randint(1,1000)
    i=i+1
    s.append(w)
    if i==1000:
        break
s.sort()
print('s= ',s)
print('длина',len(s))

