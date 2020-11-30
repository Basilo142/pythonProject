print("Введите слово 'stop' для получения результата")
summa=0
while True:
    x = input("Введите число : ")
    if x=="stop":
        break
    try:
        x = int(x)
    except ValueError:
        print("Необходимо ввести целое число!")
    else:
        summa+=x

print('summa =', summa)
input()