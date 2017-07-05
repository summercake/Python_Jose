import timeit

n = "-".join(str(n) for n in range(100))
print(n)

# % timeit "-".join(str(n) for n in range(100))
