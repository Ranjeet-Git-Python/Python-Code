class Animal:
    name1 = "saru"
    def __init__(self,name,bridg):
        self.name = name
        self.bridg = bridg
    def balk(self):
        print("animal speak ")
class Dog(Animal):
    name2 = "dogi"
    def __init__(self,name,bridg,color):
        super().__init__(name,bridg)
        self.color = color
    def walk(self):
        print("Dog speaks also")
        print("color",self.color, self.name1)
    @property
    def speek(self):
        print(self.color)
    @classmethod
    def bite(cls):
        print(cls.name1)
        return cls.name2
    @staticmethod
    def bark_sound():
        return "Woof! Woof!"
        
obj = Dog("pupi","German","Black")
obj.balk()
obj.walk()
obj.speek
print(Dog.bite())
print(Dog.bark_sound())
print(type(obj))
print(type(Dog))
print(type(Animal))