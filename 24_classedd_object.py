class MyClass:
    x=5

p1 = MyClass()
print(p1.x)


# init function
class Person:
    def __init__(self, name, age):
        self.name= name
        self.age = age

p1= Person("John", 36)
#print(p1.name)
#print(p1.age)
#an=Person
#attrs =vars(an)
print(vars(p1))

