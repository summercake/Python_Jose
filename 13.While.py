# while test:
#     code statement
# else:
#     final code statements

x = 0
while x < 10:
    print('x is currently: ', x)
    x += 1
else:
    print('All Done!!!')

# while test:
#     code statement
#     if test:
#         break
#     if test:
#         continue
# else:
#     code statement

x = 0
while x <= 10:
    print('x is currently ', x)
    print('x is still lees than 10, adding 1 to x')
    x += 1
    if x == 3:
        print('Hey x equals 3!')
        print('break!!!')
        if x > 2:
            print(1)
        else:
            print(2)
        break
    else:
        print('continuing...')
        continue
else:
    print('%s already is greater than 10 ' % x)


