class DataBase:
    __shared_attrs = {
        'name': 'thread_1',
        'data': {},
        'id': 1
    }

    def __init__(self):
        self.__dict__ = self.__shared_attrs


db1 = DataBase
db2 = DataBase
db3 = DataBase
