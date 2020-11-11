tnumb = 0

def conver(tnumb):
    try:
        whot = int(input('''Какой тип числа Вы вводите: 
-Если это int нажмите 1 
-Если это hex нажмите 2 
-Если это bin нажмите 3
-Если это 32b нажмите 4
\nВаш выбор - '''))

        if whot == 1:
            tnumb = int(input('Введите значение  '))
            print("hex: {0:x}; \nbin: {0:b}; \nint: {0:d}".format(tnumb))
            print('конец')
        elif whot == 2:
            tnumb = int(input('Введите значение  '), 16)
            print("int: {0:d}; \nbin: {0:b}; \nhex: {0:x}".format(tnumb))
            print('конец')
        elif whot == 3:
            tnumb = int(input('Введите значение  '), 2)
            print("hex: {0:x}; \nint: {0:d}; \nbin: {0:b}".format(tnumb))
            print('конец')
        elif whot == 4:
            tnumb = int(input('Введите значение  '), 32)
            print("hex: {0:x}; \nint: {0:d}; \nbin: {0:b}".format(tnumb))
            print('конец')
        else:
            print('\nЧто-то пошло не так((((...\nПопробуй еще раз)\n')
            print('P.S. Если хотите выйти нажмите "Q"\nЧто бы продолжить "Enter"')
            ex = input('-?')
            if ex == 'q' or ex == 'Q':
                return
            else:
                return (conver(tnumb))
    # except ValueError:
    except BaseException:
        print('\nЧто-то пошло не так((((...\nПопробуй еще раз)\n')
        print('P.S. Если хотите выйти нажмите "Q"\nЧто бы продолжить "Enter"')
        ex = input('-?')
        if ex == 'q' or ex == 'Q':
            return
        else:
            return conver(tnumb)

    input()
    return (conver(tnumb))
print(conver(tnumb))
