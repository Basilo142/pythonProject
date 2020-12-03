# class ImVa:
#     def __init__(self, acc):
#         self.acc = acc
#     def __get__(self, obj, obj_typ):
#         return self.acc
#
#     def __set__(self, obj, value):
#
#         with open('log.txt', 'r') as f:
#             a=int(f.read())
#         with open('log.txt', 'w') as f:
#             a_value=a+int(value)
#             f.write(str(a_value))
#         self.acc = value
#
# class Account:
#     acc = ImVa(1000)
#
#
# bob = Account()
# bob.acc = 200
#
# with open('log.txt', 'r') as f:
#     print(f.read())
#
# bob.acc = 500
#
# with open('log.txt', 'r') as f:
#     print(f.read())

class Meta(type):
    def __new__(cls, name, parents, attrs):
        print("Создан {}".format(name))

        if 'class_id' not in attrs:
            attrs['class_id'] = name.lower()

        return super().__new__(cls, name, parents, attrs)

class A(metaclass=Meta):
    pass

print(A.class_id)

