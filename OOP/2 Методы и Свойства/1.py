class User:

    def __init__(self, login, password):
        self.login = login
        self.password = password

    @property
    def password(self):
        print('getter called')
        return self.__password


    @password.setter
    def password(self, value):
        print('setter called')
        if not isinstance(value, str):
            raise TypeError('Пароль должен быть строкой')
        if len(value) < 4 or len(value) > 12:
            raise ValueError('Пароль должен быть не менее 4 и не более 12 символов')
        self.__password = value



a = User('Коля', '123dfgd')
print(a.password)
