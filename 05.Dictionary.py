# 字典 {}
# 字典就是键值对组成的集合
# 字典可以被嵌套到列表中 [{'k1':1,'k2':2},{'z1':3,'z2':4}]
# 字典的CURD
# 创建 dic = {}
# 添加 dic['key'] = value
# 修改 dic['key'] = value2
# 删除 del dic['key']
# 查看字典中的键 .keys()
# 查看字典中的值 .values()
# 查看字典中的键值 .items()

my_dict = {'key1': 'value1', 'key2': 'value2'}
print(my_dict['key1'])
my_dict = {'k1': 123, 'k2': 3.4, 'k3': 'string'}
print(my_dict['k2'])
print(my_dict['k3'][0])
print(my_dict['k1'] - 120)
my_dict['k1'] = my_dict['k1'] - 120
print(my_dict['k1'])
my_dict['k1'] += 100
print(my_dict['k1'])
d = {}
d['k1'] = 'Dog'
d['k2'] = 'Cat'
print(d)
c = {'k1': {'d1': {'m1': 'java'}}}
print(c['k1']['d1']['m1'])
print(c['k1']['d1']['m1'].upper())
print(d.keys())
print(d.values())
print(len(d), len(c), len(my_dict))