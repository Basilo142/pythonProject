summ=0
while True:
    x=input("Введите число: ")
    if x=='stop':
        break
    x=int(x)
    summ+=x
print(summ)
input()