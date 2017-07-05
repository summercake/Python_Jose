# l = [1, 2, 3, 4, 5]
# l.append(6)
# print(l)
# print(l.count(3))
# print(help(l.count))
# print(help(l.pop))
# print(l.pop(3))


def name_of_function():
    print('This is a function')


name_of_function()


def my_addition_func(arg1, arg2):
    print(arg1 + arg2)


my_addition_func(1, 2)


def say_hello(name):
    print('hello ' + name)


say_hello('Jack')


def add_num(num1, num2):
    return num1 + num2


print(add_num(1, 2))


def is_prime(num):
    for n in range(2, num):
        if num % n == 0:
            print('Not Prime')
            break
    else:
        print('The number is prime!!!')


is_prime(12)
