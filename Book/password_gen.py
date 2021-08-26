import random


def password_gen(count_char=8):

    arr=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r','s','t','v','x','y','z',
         'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S','T', 'V', 'X', 'Y', 'Z',
         '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    passw=[]

    for i in range(count_char):
        passw.append(random.choice(arr))

    return "".join(passw), passw


print(password_gen())
print(password_gen(18))
print(password_gen(6))
