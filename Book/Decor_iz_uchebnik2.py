password=input('Пароль= ')

def test_passw(p):
    print(('test_passw'))
    def decor(f):
        print('decor')
        if p=="10":
            print('if ==10')
            return f
        else:
            print('else')
            return lambda : "Доступ закрыт"
    print('end deco , pre return deco')
    return decor

@test_passw(password)
def func():
    print('func')
    return print('Доступ открыт')

print(func())


