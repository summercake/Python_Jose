try:
    2 + '2'
except:
    print('There was a type error')
finally:
    print('Finally this was printed')

try:
    f = open('test.txt')
    f.write('Test write this')
except:
    print('Error in writing to the file')
else:
    print('File write was a success')
finally:
    print('Done!!!')


# def ask_int():
#     try:
#         val = int(raw_input('Please enter an integer: '))
#     except:
#         print('Looks like you did not enter an integer!')
#     finally:
#         print('Finally block executed')
#     print(val)

