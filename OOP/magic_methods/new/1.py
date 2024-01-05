class Point:

    def __new__(cls, *args, **kwargs):
        print(f'вызов __new__ для {str(cls)}')
        return super().__new__(cls)

    def __init__(self, x=0, y=0):
        print(f'вызов __init__ для {str(self)}')
        self.x = x
        self.y = y


# pt = Point(1, 2)
# print(pt)


class DataBase(object):
    __instance = None

    # def __new__(cls, *args, **kwargs):
    #     if not cls.__instance:
    #         print('Создаем новый ЭК')
    #         cls.__instance = super().__new__(cls)
    #     else:
    #         print('ЭК уже был создан')
    #     return cls.__instance

    def __del__(self):
        DataBase.__instance = None

    def __init__(self, user, psw, port):
        print(f'вызов __init__ для {str(self)}')
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f"Соединение с бд {self.user}, {self.psw}, {self.port}")

    @staticmethod
    def close(self):
        print(f"PЗакрытие соединения с бд")

    @staticmethod
    def read(self):
        print(f"данные из бд")

    @staticmethod
    def write(self, data):
        print(f"Запись в БД {data}")


db = DataBase('Коля', 'asdasd', port='3453')
db2 = DataBase('Петя', 'asdasd', port='3453')
db.connect()
print(db2.user)

a = int()


