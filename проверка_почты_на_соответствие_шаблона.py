import re
email= input("Введите Ваш e-mail: ")
pe= r"^([a-z0-9_.-]+)@(([a-z0-9-]+\.)+[a-z]{2,6})$"
p = re.compile(pe, re.I | re.S)
m = p.search(email)
if not m:
    print("E-mail не соответствует шаблону")
else:
    print("E-mail", m.group(0), 'соответствует...')
    print("ящик: ", m.group(1), 'домен', m.group(2))
