key = int(input())
finish = [0, 0]
for i in range(key):
    to = input().split(' ')
    if to[0] == 'север':
        finish[1] = finish[1] + int(to[1])
    if to[0] == 'юг':
        finish[1] = finish[1] - int(to[1])
    if to[0] == "восток":
        finish[0] = finish[0] + int(to[1])
    if to[0] == "запад":
        finish[0] = finish[0] - int(to[1])
for i in finish:
    print(i, end=' ')