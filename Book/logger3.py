def first_decor(func):
    def wra():
        print('This 1 - dec')
        return func()
    return wra

def second_decor(func):
    def wra():
        print('This 2 - dec')
        return func()
    return wra


@first_decor
@second_decor
def decorated():
    print('Finally')

decorated()

