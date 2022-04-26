class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        DataBase.__instance = None

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def connect(self):
        print('Connect - x={}, y={}, z={}'.format(self.x, self.y, self.z))


d1 = DataBase(2, 3, 4)
d1.connect()
d2 = DataBase(22, 33, 44)
d2.connect()
d1.connect()
