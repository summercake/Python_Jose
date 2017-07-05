s = set()
s.add(1)
s.add(2)
s.add(2)
s.add(4)
s.add(5)
print(s)

s = {1, 2, 3}

sc = s.copy()
s.add(4)
print(sc)

print(s.difference(sc))

s1 = {1, 2, 3}
s2 = {1, 4, 5}
s1.difference_update(s2)
print(s1)

s.add(12)
s.discard(12)
print(s)

s1 = {1, 2, 3}
s2 = {1, 2, 4}
print(s1.intersection(s2))
print(s1.intersection_update(s2))
print(s1.union(s2))
print(s1.update(s2))
