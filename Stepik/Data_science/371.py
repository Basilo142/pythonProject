key = input()
val = input()
s1 = input()
s1out = str()
s2 = input()
s2out = str()
dic1 = {}
dic2 = {}
for i in range(len(key)):
    dic1[key[i]] = val[i]
    dic2[val[i]] = key[i]
for i in s1:
    s1out = s1out+str(dic1[i])
for i in s2:
    s2out = s2out+str(dic2[i])
print(s1out)
print(s2out)
