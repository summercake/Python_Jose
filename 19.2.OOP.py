# class tcc:
#     """
#     This is a class, it's empty
#     It is used for test
#     """
#     pass
#
#
# print(tcc.__doc__)
# print(help(tcc))


class Dog:  # 创建一个类
    def __init__(self, name, newWeight, newColor):
        self.name = name
        self.weight = newWeight
        self.color = newColor

    def __str__(self):  # 一般用于测试
        return 'I am a dog'

    def bark(self):
        print('woof')

    def run(self):
        print('running')

    def eat(self):
        print('eating')
        self.weight += 5


# 实例化一个类
dog = Dog('Jimmy', 5, 'yellow')

# 添加属性
# dog.weight = 5
# dog.color = 'white'

# 调用方法和属性
print(dog.bark())
print(dog.run())
print(dog.name)
print(dog.weight)
print(dog.color)
dog.eat()
print(dog.weight)

wangcai = Dog('Monkey', 10, 'black')
print(wangcai.weight)
print(wangcai.color)
print(wangcai.name)
