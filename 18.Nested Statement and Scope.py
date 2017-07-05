x = 25


def printer():
    x = 50
    return x


print(x)
print(printer())


def great():
    name = 'Jack'

    def hello():
        print('Hello ' + name)

    hello()


great()

x = 50


def func():
    global x
    print('This func is now using the global x')
    print('Because of global x is: ', x)
    x = 2
    print('Ran func(), changed global x to ', x)


print('Before calling func(), x is: ', x)
func()
print('Value of x (outside of func()) is: ', x)
