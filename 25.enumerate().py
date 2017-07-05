l = ['a', 'b', 'c']
count = 0
for item in l:
    print(item)
    print(count)
    count += 1

for count1, item in enumerate(l):
    print(count1)
    print(item)

for count2, item in enumerate(l):
    if count2 >= 2:
        break
    else:
        print(item)
