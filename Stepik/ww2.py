x = [int(i) for i in input().split()]
y = []
if len(x)== 1:
    y=x
else:
    y.append(x[-1]+x[1])
    for i in range(1,len(x)-1):
        y.append(x[i-1]+x[i+1])
    y.append(x[-2]+x[0])
for i in y:
    print(i, end=' ')