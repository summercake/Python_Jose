# 元组 ()
# 元组中的数据不可重复
# 元组创建后不可修改 mutable
# 创建后不可增删改
# 只能修改定义

t = (1, 2, 3, 4)
print(type(t))
t = ('one', 2)
print(t[0], t[1])
print(t[-1])
print(t.index('one'))
print(t.count('one'))
l = [1, 2, 3]
t = (1, 2, 3)
l[0] = 's'
# tuple is immutable
# t[0] = 's'
