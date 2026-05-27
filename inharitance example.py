# OOP Concepts: Inheritance, super(), public, protected, private,
#               class variables, @property, @classmethod, @staticmethod

class Animal:
    # --- Class Variables (shared across all instances) ---
    kingdom = "Animalia"            # public class variable
    _classification = "Eukaryote"  # protected class variable
    __count = 0                     # private class variable - tracks total animals created

    def __init__(self, name, species, age):
        self.name = name            # public instance variable
        self._species = species     # protected instance variable
        self.__age = age            # private instance variable
        Animal.__count += 1         # increment class-level counter on each new instance

    # --- @property: getter for private __age ---
    @property
    def age(self):
        """Get the animal's age."""
        return self.__age

    # --- @age.setter: setter with validation ---
    @age.setter
    def age(self, value):
        if value > 0:
            self.__age = value
        else:
            print("Age must be a positive number.")

    # --- @classmethod: access/modify class-level data ---
    @classmethod
    def get_count(cls):
        """Returns total number of Animal instances created."""
        return cls.__count

    @classmethod
    def get_kingdom(cls):
        """Returns the kingdom class variable."""
        return cls.kingdom

    # --- @staticmethod: utility method, no access to class or instance ---
    @staticmethod
    def is_valid_age(age):
        """Validates if an age value is acceptable."""
        return isinstance(age, int) and age > 0

    def speak(self):
        print(f"{self.name} makes a sound.")

    def _describe_species(self):
        # protected method - intended for use in subclasses
        return f"Species: {self._species}"

    def __secret(self):
        # private method - not accessible outside this class
        return "This is a private method."

    def show_info(self):
        print(f"Name: {self.name}, {self._describe_species()}, Age: {self.__age}")
        print(self.__secret())


class Dog(Animal):
    # Class variable specific to Dog
    domesticated = True

    def __init__(self, name, age, breed):
        super().__init__(name, "Canine", age)   # calling parent __init__ via super()
        self.breed = breed                       # public instance variable

    # --- @property: computed property ---
    @property
    def profile(self):
        """Returns a formatted profile string."""
        return f"{self.name} | Breed: {self.breed} | Age: {self.age}"

    def speak(self):
        # overriding parent method
        print(f"{self.name} says: Woof!")

    def show_breed_info(self):
        # accessing protected attribute from parent
        print(f"{self.name} is a {self.breed}. {self._describe_species()}")

    def show_age(self):
        # using @property getter from Animal instead of get_age()
        print(f"{self.name} is {self.age} years old.")

    # --- @classmethod: Dog-specific class info ---
    @classmethod
    def is_domesticated(cls):
        return f"Dog domesticated: {cls.domesticated}"

    # --- @staticmethod: dog-specific utility ---
    @staticmethod
    def bark_sound():
        return "Woof! Woof!"


class GuideDog(Dog):
    # Class variable specific to GuideDog
    role = "Assistance"

    def __init__(self, name, age, breed, owner):
        super().__init__(name, age, breed)   # calling Dog's __init__
        self.owner = owner                   # public instance variable

    # --- @property: override profile from Dog ---
    @property
    def profile(self):
        base = super().profile
        return f"{base} | Owner: {self.owner} | Role: {GuideDog.role}"

    def speak(self):
        print(f"{self.name} (guide dog for {self.owner}) says: Woof!")

    def show_full_info(self):
        self.show_breed_info()
        self.show_age()
        print(f"Owner: {self.owner}")

    # --- @classmethod: guide dog role info ---
    @classmethod
    def get_role(cls):
        return f"GuideDog role: {cls.role}"


# ─────────────────────────────────────────────
# Demo
# ─────────────────────────────────────────────

print("=== Animal ===")
a = Animal("Generic Animal", "Unknown", 5)
a.show_info()
print("Kingdom (class var):", Animal.kingdom)
print("Total animals created:", Animal.get_count())   # @classmethod
print("Is 3 a valid age?", Animal.is_valid_age(3))    # @staticmethod
print("Is -1 a valid age?", Animal.is_valid_age(-1))  # @staticmethod

print("\n=== Dog ===")
d = Dog("Rex", 3, "German Shepherd")
d.speak()
d.show_breed_info()
d.show_age()
print("Dog profile (@property):", d.profile)          # @property
print(Dog.is_domesticated())                           # @classmethod
print("Bark sound (@staticmethod):", Dog.bark_sound()) # @staticmethod

print("\n=== GuideDog ===")
g = GuideDog("Buddy", 4, "Labrador", "John")
g.speak()
g.show_full_info()
print("GuideDog profile (@property):", g.profile)     # overridden @property
print(GuideDog.get_role())                             # @classmethod

print("\n=== @property setter ===")
print(f"Rex's current age: {d.age}")
d.age = 5                                              # uses @age.setter
print(f"Rex's updated age: {d.age}")
d.age = -2                                             # triggers validation

print("\n=== Class Variable - Animal count ===")
print(f"Total Animal instances created: {Animal.get_count()}")

print("\n=== Name Mangling (not recommended) ===")
print(a._Animal__age)   # Python's name mangling: _ClassName__attribute
