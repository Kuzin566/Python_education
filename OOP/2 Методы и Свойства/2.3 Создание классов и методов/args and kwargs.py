# a, b, *c = [1, True, 4, 6, 'hello ', 7, 9]
# print(a, b, c)
#
# a, *b, c = [1, True, 4, 6, 'hello ', 7, 9]
# print(a, b, c)
#
# *a, b, c = [1, True, 4, 6, 'hello ', 7, 9]
# print(a, b, c)
#
#
# def f(*args):
#     s = 0
#     for i in args:
#         s += i
#     print(s)
#
# f(1,2,3,4,5,6)
#
# def outPrint(*args, sep='#', end='@'):
#     print(args, sep, end)
#
# outPrint(1, 2, 3, 4, 5, 6, sep='999')
# outPrint(1, 2, 3, end='111')
# outPrint(1, 2)

def f(**kwargs):
    for k, v in kwargs.items():
        print(k,v)

f(a=1, b=2, c=3)
def f(*args, **kwargs):
    print(args, kwargs)

f(1, 2, 3,  a = 4, b = 5, c = 7)