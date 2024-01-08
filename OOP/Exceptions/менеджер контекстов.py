class CustomManagerContext:
    def __enter__(self):
        print('Start manager context')
        return 'Hello world!'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('End manager context')
        print(exc_type, exc_val, exc_tb, sep=',')
        if isinstance(exc_val, ZeroDivisionError):
            print('Нельзя делить на ноль')
            return True
        return True

    @staticmethod
    def primer():
        for i in range(5):
            print('hello')



class FileContext:
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode

    def __enter__(self):
        print('Open file')
        self.file = open(self.path, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Close file')
        self.file.close()




with FileContext('asdasd.txt', 'r') as file:
    print(file.read())