# OOP Concepts: Inheritance, super(), public, protected, private

class Animal:
    def __init__(self, name, species, age):
        self.name = name            # public - accessible anywhere
        self._species = species     # protected - convention: use within class and subclasses
        self.__age = age            # private - name-mangled, only accessible within this class

    def speak(self):
        print(f"{self.name} makes a sound.")

    def get_age(self):
        # public method to access private attribute
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive.")

    def _describe_species(self):
        # protected method - intended for use in subclasses
        return f"Species: {self._species}"

    def __secret(self):
        # private method - not accessible outside this class
        return "This is a private method."

    def show_info(self):
        print(f"Name: {self.name}, {self._describe_species()}, Age: {self.__age}")
        print(self.__secret())  # private method called within the class


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, "Canine", age)  # calling parent __init__ via super()
        self.breed = breed  # public

    def speak(self):
        # overriding parent method
        print(f"{self.name} says: Woof!")

    def show_breed_info(self):
        # accessing protected attribute from parent
        print(f"{self.name} is a {self.breed}. {self._describe_species()}")

    # cannot directly access self.__age (private to Animal)
    # but can use the public getter
    def show_age(self):
        print(f"{self.name} is {self.get_age()} years old.")


class GuideDog(Dog):
    def __init__(self, name, age, breed, owner):
        super().__init__(name, age, breed)  # calling Dog's __init__
        self.owner = owner  # public

    def speak(self):
        print(f"{self.name} (guide dog for {self.owner}) says: Woof!")

    def show_full_info(self):
        self.show_breed_info()
        self.show_age()
        print(f"Owner: {self.owner}")


# --- Demo ---

print("=== Animal ===")
a = Animal("Generic Animal", "Unknown", 5)
a.show_info()
print(a.name)           # public - works fine
print(a._species)       # protected - works but not recommended outside class
# print(a.__age)        # ERROR: private, name-mangled to _Animal__age
print(a.get_age())      # access private via public getter

print("\n=== Dog ===")
d = Dog("Rex", 3, "German Shepherd")
d.speak()
d.show_breed_info()
d.show_age()

print("\n=== GuideDog ===")
g = GuideDog("Buddy", 4, "Labrador", "John")
g.speak()
g.show_full_info()

# Accessing private via name mangling (not recommended, but possible)
print("\n=== Name Mangling (not recommended) ===")
print(a._Animal__age)   # Python's name mangling: _ClassName__attribute
