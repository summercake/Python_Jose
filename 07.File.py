f = open('test.txt')
print(f.read())
f.seek(0)
print(f.read())
f.seek(0)
print(f.readline())
f.close()
for line in open('test.txt'):
    print(line)
for words in open('test.txt'):
    print(words)
