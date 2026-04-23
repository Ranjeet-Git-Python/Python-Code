class Dog:
# Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

# Create instances
dog1 = Dog("Buddy", 5)
dog2 = Dog("Milo", 3)

# Access class attribute
print(dog1.species) # Canis familiaris
print(Dog.species) # Canis familiaris

# Access instance attributes
print(dog1.name) # Buddy
print(dog2.name) # Milo