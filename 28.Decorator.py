# def fun():
#     return 1
#
#
# print(fun())
#
# s = 'This is a global variable'
#
#
# def func():
#     print(locals())
#
#
# print(globals().keys())
#
# print(func())
#
#
# def hello(name='Jose'):
#     return 'Hello ' + name
#
#
# print(hello())
# greet = hello
# print(greet)
# print(greet())


# def hello(name='Jose'):
#     # print('The hello() function has been executed')
#
#     def greet():
#         return '\t This is inside the greet() function'
#
#     def welcome():
#         return '\t This is inside the welcome() function'
#
#     if name == 'Jose':
#         return greet
#     else:
#         return welcome
#         # print(greet())
#         # print(welcome())
#         # print('Now we are back inside the Hello function')
#
#
# x = hello()
# print(x())


# def hello():
#     return 'Hi Jose!'
#
#
# def other(func):
#     print('Other code goes here')
#     print(func())
#
#
# other(hello)


def new_decorator(func):
    def wrap_func():
        print('Code here, before executing the func()')
        func()
        print('Code here will execute after the func()')

    return wrap_func()


def func_needs_decorator():
    print('This function needs a decorator!')


# func_needs_decorator()
# func_needs_decorator = new_decorator(func_needs_decorator)
# func_needs_decorator()


@new_decorator
def func_needs_decorator():
    print('This function needs a decorator!')
