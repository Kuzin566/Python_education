# from tkinter import Label
#
# label1 = Label(text="Hello Python", fg="#eee", bg="#333")
# label2 = Label(text = "Username")
# label3 = Label(text = "Password", font=("Comic Sans MS", 24, "bold") ,
#                bd=20, bg='#ffaaaa')


class CustomLabel:
    def __init__(self, **kwargs):
        self.id = None
        self.offer_id = None
        # self.text = text
        self.__dict__.update(kwargs)

    def config(self, **kwargs):
        for key, value in kwargs.items():
            self.__dict__.update(kwargs)


# label = CustomLabel(text="Hello", bd=20, bg='#ffaaaa')
#
# print(label.__dict__) # {'text': 'Hello', 'bd': 20, 'bg': '#ffaaaa'}
#
# label.config(color='red', bd=100)
#
# print(label.__dict__) # {'text': 'Hello', 'bd': 100, 'bg': '#ffaaaa', 'color': 'red'}

offer = CustomLabel(id=150)
print(offer.id)