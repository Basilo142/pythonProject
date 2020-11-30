class My:
    def __enter__(self):
        print("Вызван метод __enter__()")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Вызван метод __exit__()")
        if exc_type is None:
            print("Исключение не возникло")
        else:
            print("Value =", exc_val)
            return False
print("Последовательность при отсутствии исключения:")
with My():
    print("Блок внутри wiht")
print("\nПоследовательность при наличии исключения:")
with My() as SA:
    print("Блок внутри wiht-2")
    #raise TypeError("Исключение TypeError")


with open("text.txt", "a", encoding="utf-8") as f:
    f.write("Cnhjrf\n")

