# In Python, every thing is an object
l = [1, 2, 3]
print(l.count(2))

print(type({'k1': 1}))


def square(num):
    return num * num


print(type(square))


class Sample(object):
    pass


x = Sample()
print(type(x))


# Initial
class Dog(object):
    species = 'mammal'

    def __init__(self, breed, name, fur=True):
        self.breed = breed
        self.name = name
        self.fur = fur


sam = Dog(breed='Lab', name='Sammy', fur=False)
print(
    sam.breed,
    sam.name,
    sam.fur
)


# Method
class Circle(object):
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * Circle.pi

    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_radius(self):
        return self.radius


c = Circle(radius=10)
print(c.pi)
print(c.area())
print(c.get_radius())
print(c.set_radius(20))
print(c.radius)
print(c.get_radius())


# Inheritance
class Animal(object):
    def __init__(self):
        print("Animal Created")

    def who_am_i(self):
        print('Animal')

    def eat(self):
        print('Eating')


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Dog Created')

    def who_am_i(self):
        print('Dog')

    def bark(self):
        print('woof!')


d = Dog()
print(d.who_am_i())
print(d.eat())
print(d.bark())


class Book(object):
    def __init__(self, title, author, pages):
        print('A book has been created')
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: %s, Author: %s, pages: %s" % (self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book is gone!")


b = Book('python', 'Jose', 100)
print(b.author)
print(b.title)
print(b.pages)
print(b)
print(len(b))
del b
