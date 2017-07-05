l = [1, 2, 3]
l.append(4)
print(l)
print(l.count(10))
print(l.count(1))
x = [1, 2, 3]
x.append([4, 5])
print(x)
x = [1, 2, 3]
x.extend([4, 5])
print(x)
print(l.index(2))
l.insert(2, 'inserted')
print(l)
print(l.pop(0))
l.remove('inserted')
print(l)
l.reverse()
print(l)
