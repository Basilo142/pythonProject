print('Введите слово "stop" для получения результата')
summ = 0
while True:
    x=input("Введите число:  ")
    if x=='stop':
        break
    if x== "":
        print('Вы них..я не ввели!')
        continue
    if x[0]=='-' or x[0]=='+':
        if not x[1:].isdigit():
            print("Необходимо ввести число а не строку!")
            continue
    else:
        if not x.isdigit():
            print("Необходимо ввести число а не строку!")
            continue
    x=int(x)
    summ+=x
print("Сумма чисел равна - ", summ)
input()
