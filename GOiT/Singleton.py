class Singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance


se1 = Singleton()
se2 = Singleton()


print(se1 == se2)
print(se1)
print(se2)
