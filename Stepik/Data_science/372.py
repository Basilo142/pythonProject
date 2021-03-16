key = int(input())
dic = []
for i in range(key):
    dic.append(input().lower())
key = int(input())
out_set = set()
for i in range(key):
    words=[]
    words = input().split(' ')
    for word in words:
        if word.lower() not in dic:
            out_set.add(word.lower())
for i in out_set:
    print(i)