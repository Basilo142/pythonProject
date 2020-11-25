import hashlib
p11=input('Введите пароль 1 : ')
p22=input('Повторите пароль : ')
p1=hashlib.md5(p11.encode())
p2=hashlib.md5(p22.encode())
print(p1)
print(p2)
if p1.hexdigest()==p2.hexdigest(): print('Все ок!')
else:
     print("Упс!")