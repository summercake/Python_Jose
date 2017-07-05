def even_check(num):
    if num % 2 == 0:
        return True
    else:
        return False


print(even_check(35))

lst = range(10)

print(filter(even_check, lst))

print(filter(lambda num: num % 2 == 0, lst))

print(map(lambda num: num % 2 == 0, [2]))

