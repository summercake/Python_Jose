# 列表 []
# 存储多个数据
# 可以存储不同类型的数据
# 添加数据到列表的最后, 不会合并两个列表 .append(数据或列表)
# 添加数据到列表的最后, 会合并两个列表 .extend(数据或列表)
# 添加数据到指定索引 .insert(索引, 数据)
# 根据索引删除数据 .pop(索引) 如果没有索引, 则默认为最后一位
# 根据数据内容删除数据 .removed(数据)
# 根据索引删除列表数据 del xxx[索引]
# 查找列表中的数据 if 123 in list, if 123 not in list


my_list = [1, 2, 3, 'i love big bra']
print(my_list)
print(len(my_list))
print(my_list[0])
print(my_list[1:])
print(my_list[:3])
print(my_list + ['new item'])
print(my_list * 2)
print(my_list.__add__(['新东东']))
my_list.append('新东东')
print(my_list)
new_list = [1, 2, 5, 3, 4, 10]
new_list.reverse()
print(new_list)
new_list.sort()
print(new_list)
new_list.reverse()
print(new_list)
matrix = [my_list, new_list]
print(matrix)
print(matrix[1])
final = [row[0] for row in matrix]
print(final)
print(new_list.pop())

