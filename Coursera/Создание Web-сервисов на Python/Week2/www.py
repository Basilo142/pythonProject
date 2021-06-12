a = int(input())
b = int(input())
s = 0
k = 0
for i in range(a, b+1):
    if i % 3 == 0:
        s=s+i
        k+=1
n=s/k
print(n)