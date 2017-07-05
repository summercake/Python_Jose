from collections import Counter

# 统计集合中有每个元素各有多少个
l = [1, 2, 3, 4, 5, 1, 3, 4, 5, 6, 1]
print(Counter(l))

s = 'sdagsfdlkajglsdfka'
print(Counter(s))

s = 'How many times does each word show up in this sentence word word shoe up up'
words = s.split()
print(Counter(words))
c = Counter(words)
print(sum(c.values()))
