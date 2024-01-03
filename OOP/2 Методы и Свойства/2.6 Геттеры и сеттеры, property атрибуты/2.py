
class UserMail:
    def __init__(self, login, email):
        self.login = login
        self.__email = email


    def get_email(self):
        return self.__email

    def set_email(self, email):
        if email.count('@') == 1 and email.count('.') == 1:
            if email.rfind('@') < email.rfind('.'):
                self.__email = email
            else:
                print(f"ErrorMail:{email}")
        else:
            print(f"ErrorMail:{email}")

    email = property(fget=get_email, fset=set_email)


a = UserMail("Nick", "Kuzin566@mail.ru")
a.set_email("kuzin666@mail.ru")
print(a.get_email())