# def gencube(n):
#     out = []
#     for num in range(n):
#         out.append(num ** 3)
#     return out
#
#
# for x in gencube(10):
#     print(x)


# 生成器1
# a = (x * 2 for x in range(10))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))


# def fib(n):
#     a = 1
#     b = 1
#     output = []
#     for i in range(n):
#         output.append(a)
#         b, a = b, a + b
#         return output
#
#
# print(fib(10))

# def simple_gen():
#     for x in range(3):
#         yield x
#
# g=simple_gen()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

s = 'hello'
s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
