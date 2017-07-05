#
#  for item in object:
#     statements to do stuff
#

l = [1, 2, 3, 4, 5]
for v in l:
    print(v)

for num in l:
    if num % 2 == 0:
        print(num)
    else:
        print('{x} is a odd number'.format(x=num))
        print('%s is a odd number' % num)

list_num = 0
for num in l:
    list_num += num
print(list_num)

s = 'this is a string!'
for l in s:
    print(l)

tup = (1, 2, 3, 4, 5)
for t in tup:
    print(t)

l = [(2, 4), (6, 8), (10, 12)]
for tup in l:
    print(tup)
for (t1, t2) in l:
    print(t1)

d = {'k1': 1, 'k2': 2, 'k3': 3, 'k4': 4}
for item in d:
    print(item)

for (k, v) in d.items():
    print(k)
    print(v)
