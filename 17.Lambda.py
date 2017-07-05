def square(num):
    result = num ** 2
    return result


print(square(2))


def square(num): return num ** 2


print(square(5))

square2 = lambda num: num ** 2
print(square2(2))

even = lambda num: num % 2 == 0
print(even(4))

first = lambda s: s[0]
print(first('hello'))

rev = lambda s: s[::-1]
print(rev('hello'))


def adder(x, y):
    return x + y


print(adder(1, 1))
adder1 = lambda x, y: x + y
print(adder1(5, 5))

len_check = lambda item: len(item)
print(len_check('how many chars does this string have?'))
