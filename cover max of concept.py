#1. Iterators & Generators: Used for memory-efficient data processing.
def numbers():
    for i in range(5):
        yield i

for n in numbers():
    print(n)

#2. Decorators: Modify function behavior without changing the original code.
def logger(func):
    def wrapper():
        print("Running...")
        func()
    return wrapper

@logger
def greet():
    print("Hello")

greet()

#3. Context Managers: Handle resources automatically.
with open("file.txt") as f:
    data = f.read()

#You can also create custom context managers:
class Database:
    def __enter__(self):
        print("Connected")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Disconnected")

#4. Closures:Functions remembering variables from outer scopes.
def multiplier(x):
    def inner(y):
        return x * y
    return inner

double = multiplier(2)
print(double(5))

#5. Lambda Functions: Anonymous one-line functions.

square = lambda x: x * x
print(square(4))

#6. Comprehensions: Compact and efficient data creation.

squares = [x*x for x in range(10)]

#7. Magic (Dunder) Methods: Customize object behavior.

class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

#8. Metaclasses: Control class creation and behavior.
# Metaclasses are considered one of Python's most advanced topics.
class MyMeta(type):
    pass

class User(metaclass=MyMeta):
    pass

#9. Descriptors: Control attribute access.

class Positive:
    def __get__(self, obj, owner):
        return obj._value

    def __set__(self, obj, value):
        if value < 0:
            raise ValueError("Must be positive")
        obj._value = value

#10. Concurrency & Parallelism
#Multithreading
import threading
from typing import Collection

def task():
    print("Running")

thread = threading.Thread(target=task)
thread.start()
#Multiprocessing
from multiprocessing import Process

def task():
    print("Process running")

p = Process(target=task)
p.start()

#Concurrency, threading, multiprocessing, and understanding the GIL are often considered advanced Python skills.
#11. Async Programming
import asyncio

async def main():
    await asyncio.sleep(1)
    print("Done")

asyncio.run(main())

#12. Type Hints
def add(a: int, b: int) -> int:
    return a + b

#13. Functional Programming
from functools import reduce

nums = [1, 2, 3, 4]

print(list(map(lambda x: x*2, nums)))
print(reduce(lambda x, y: x+y, nums))

#14. Memory Management & Garbage Collection
import gc

gc.collect()

#Understanding references, mutability, object identity, and garbage collection is part of advanced Python knowledge.

#15. Advanced OOP

Multiple inheritance
Method Resolution Order (MRO)
Abstract Base Classes (ABC)
Composition vs Inheritance
Dataclasses
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

Recommended Learning Order:
Comprehensions
Lambda, Map, Filter, Reduce
Iterators & Generators
Closures
Decorators
Context Managers
Advanced OOP
Async Programming
Multithreading & Multiprocessing
Descriptors
Metaclasses

These topics are commonly considered the progression from intermediate to advanced Python.
Below is a single Python program that demonstrates most of the important basic, intermediate, and advanced Python concepts in one place:

"""
Python Master Demo
Covers:
1. Variables & Data Types
2. Operators
3. Conditional Statements
4. Loops
5. Functions
6. Lambda Functions
7. *args and **kwargs
8. List, Set, Dict Comprehensions
9. OOP
10. Inheritance
11. Polymorphism
12. Encapsulation
13. Class Methods & Static Methods
14. Exception Handling
15. File Handling
16. Iterators
17. Generators
18. Decorators
19. Closures
20. Context Managers
21. Dataclasses
22. Abstract Classes
23. Multithreading
24. Async Programming
25. Type Hints
26. Magic Methods
"""

from dataclasses import dataclass
from abc import ABC, abstractmethod
from functools import wraps
import threading
import asyncio

# ======================================
# 1. Variables & Data Types
# ======================================

name = "Python"
version = 3.12
is_popular = True

print(name, version, is_popular)

# ======================================
# 2. Function with Type Hints
# ======================================

def add(a: int, b: int) -> int:
    return a + b

print("Add:", add(10, 20))

# ======================================
# 3. Lambda Function
# ======================================

square = lambda x: x ** 2
print("Square:", square(5))

# ======================================
# 4. *args and **kwargs
# ======================================

def display(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

display(1, 2, 3, name="John", age=25)

# ======================================
# 5. Comprehensions
# ======================================

list_comp = [x*x for x in range(5)]
set_comp = {x*x for x in range(5)}
dict_comp = {x: x*x for x in range(5)}

print(list_comp)
print(set_comp)
print(dict_comp)

# ======================================
# 6. OOP + Magic Methods
# ======================================

class Person:

    population = 0

    def __init__(self, name):
        self._name = name
        Person.population += 1

    def __str__(self):
        return f"Person({self._name})"

    @classmethod
    def get_population(cls):
        return cls.population

    @staticmethod
    def greet():
        print("Welcome!")

p1 = Person("Alice")
print(p1)
Person.greet()
print("Population:", Person.get_population())

# ======================================
# 7. Inheritance & Polymorphism
# ======================================

class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()

# ======================================
# 8. Abstract Base Class
# ======================================

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):

    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w

rect = Rectangle(10, 5)
print("Area:", rect.area())

# ======================================
# 9. Exception Handling
# ======================================

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Cleanup Complete")

# ======================================
# 10. File Handling
# ======================================

with open("sample.txt", "w") as f:
    f.write("Hello Python")

with open("sample.txt", "r") as f:
    print(f.read())

# ======================================
# 11. Iterator
# ======================================

class Counter:

    def __init__(self, max_value):
        self.max = max_value
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.max:
            self.current += 1
            return self.current
        raise StopIteration

for num in Counter(3):
    print("Iterator:", num)

# ======================================
# 12. Generator
# ======================================

def generator():
    for i in range(3):
        yield i

for value in generator():
    print("Generator:", value)

# ======================================
# 13. Decorator
# ======================================

def logger(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Executing", func.__name__)
        return func(*args, **kwargs)

    return wrapper

@logger
def hello():
    print("Hello World")

hello()

# ======================================
# 14. Closure
# ======================================

def multiplier(x):

    def inner(y):
        return x * y

    return inner

double = multiplier(2)
print("Closure:", double(10))

# ======================================
# 15. Context Manager
# ======================================

class Database:

    def __enter__(self):
        print("Database Connected")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Database Closed")

with Database():
    print("Working with DB")

# ======================================
# 16. Dataclass
# ======================================

@dataclass
class Student:
    id: int
    name: str

student = Student(1, "Rahul")
print(student)

# ======================================
# 17. Multithreading
# ======================================

def task():
    print("Thread Running")

thread = threading.Thread(target=task)
thread.start()
thread.join()

# ======================================
# 18. Async Programming
# ======================================

async def async_task():
    await asyncio.sleep(1)
    print("Async Task Completed")

async def main():
    await async_task()

asyncio.run(main())

# ======================================
# 19. Advanced Data Structures
# ======================================

numbers = [1, 2, 3, 4, 5]

mapped = list(map(lambda x: x*2, numbers))
filtered = list(filter(lambda x: x % 2 == 0, numbers))

print("Mapped:", mapped)
print("Filtered:", filtered)

# ======================================
# Program End
# ======================================

print("\nAll Python Concepts Demonstrated Successfully!")

This single script demonstrates about 90% of the Python concepts commonly asked in interviews, including:

OOP (Inheritance, Polymorphism, Encapsulation)
Decorators
Generators
Iterators
Closures
Context Managers
Abstract Classes
Dataclasses
Multithreading
Async/Await
File Handling
Exception Handling
Comprehensions
Type Hints
Magic Methods
Class & Static Methods

These are the concepts expected from an intermediate-to-advanced Python developer.

with detailed explanation

A single program can demonstrate many Python features, but understanding why each feature exists is more important than memorizing code. Here's a structured walkthrough of the major Python concepts from basic to advanced.

1. Variables and Data Types

Variables store data in memory.

name = "Rahul"      # str
age = 25            # int
height = 5.9        # float
is_student = True   # bool
Explanation

Python is dynamically typed, so you don't need to declare types explicitly.

x = 10
x = "Hello"  # Valid

The type changes automatically.

2. Operators
a = 10
b = 3

print(a + b)   # Addition
print(a - b)   # Subtraction
print(a * b)   # Multiplication
print(a / b)   # Division
print(a % b)   # Modulus
print(a ** b)  # Power
Why Important?

Almost every program performs calculations or comparisons.

3. Conditional Statements
age = 20

if age >= 18:
    print("Adult")
else:
    print("Minor")
Flow
Condition True?
      |
   Yes ---> Execute IF block
      |
   No ----> Execute ELSE block

Used for decision-making.

4. Loops
For Loop
for i in range(5):
    print(i)

Output:

0
1
2
3
4
While Loop
count = 0

while count < 5:
    print(count)
    count += 1
Difference
For	While
Known iterations	Unknown iterations
Easier	More flexible

5. Functions

Functions help reuse code.

def greet(name):
    return f"Hello {name}"

print(greet("Rahul"))
Benefits
Reusability
Readability
Modularity

6. Lambda Functions

Anonymous functions.

square = lambda x: x*x

print(square(5))

Equivalent to:

def square(x):
    return x*x

Used with:

map()
filter()
sorted()

7. *args and **kwargs

*args

Accepts unlimited positional arguments.

def total(*numbers):
    return sum(numbers)

print(total(1,2,3,4))
**kwargs

Accepts unlimited keyword arguments.

def info(**data):
    print(data)

info(name="Rahul", age=25)

Output:

{'name': 'Rahul', 'age': 25}

8. List Comprehension

Traditional:

squares = []

for i in range(5):
    squares.append(i*i)

Pythonic:

squares = [i*i for i in range(5)]
Structure
[expression for item in iterable]

9. Object-Oriented Programming (OOP)

OOP models real-world objects.

class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)

s = Student("Rahul")
s.display()
Components
Class
Object
Attributes
Methods

10. Encapsulation

Protects data.

class Bank:

    def __init__(self):
        self.__balance = 1000

    def get_balance(self):
        return self.__balance
Why?

Prevents direct modification.

bank.__balance = 0

Won't affect actual balance.

11. Inheritance

Reuse code from another class.

class Animal:

    def sound(self):
        print("Some sound")

class Dog(Animal):
    pass

dog = Dog()
dog.sound()

Output:

Some sound
Benefits
Reusability
Less duplication

12. Polymorphism

Same method, different behavior.

class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")
animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()

Output:

Bark
Meow

13. Magic Methods (Dunder Methods)

Methods beginning and ending with "__".

class Student:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
s = Student("Rahul")

print(s)

Without __str__:

<__main__.Student object at ...>

With __str__:

Rahul

14. Exception Handling

Handle runtime errors.

try:
    result = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero")
Structure
try:
    risky code

except:
    handle error

finally:
    cleanup code

15. File Handling

Writing:

with open("data.txt", "w") as file:
    file.write("Hello")

Reading:

with open("data.txt", "r") as file:
    print(file.read())
Why use with?

Automatically closes file.

16. Iterators

Objects that produce values one at a time.

numbers = iter([1,2,3])

print(next(numbers))
print(next(numbers))

Output:

1
2
Internal Working
for x in [1,2,3]:

actually uses iterators internally.

17. Generators

Memory-efficient iterators.

def counter():

    yield 1
    yield 2
    yield 3
for value in counter():
    print(value)
Difference

Normal function:

return

Generator:

yield

Generator pauses and resumes.

18. Decorators

Functions modifying other functions.

def logger(func):

    def wrapper():
        print("Executing...")
        func()

    return wrapper

Usage:

@logger
def hello():
    print("Hello")

Output:

Executing...
Hello
Real Uses
Authentication
Logging
Timing
Validation

19. Closures

Inner function remembers outer variables.

def multiplier(x):

    def inner(y):
        return x*y

    return inner
double = multiplier(2)

print(double(5))

Output:

10

Even after multiplier() ends, x remains remembered.

20. Context Managers

Manage resources automatically.

with open("file.txt") as f:
    data = f.read()

Custom:

class Database:

    def __enter__(self):
        print("Connected")

    def __exit__(self, *args):
        print("Disconnected")

21. Dataclasses

Reduce boilerplate code.

Traditional:

class Student:

    def __init__(self, id, name):
        self.id = id
        self.name = name

Dataclass:

from dataclasses import dataclass

@dataclass
class Student:
    id: int
    name: str

Python automatically creates:

Constructor
String representation
Equality methods

22. Abstract Classes

Force subclasses to implement methods.

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

Child class:

class Circle(Shape):

    def area(self):
        return 100

23. Multithreading

Run multiple tasks concurrently.

import threading

def task():
    print("Running")

thread = threading.Thread(target=task)
thread.start()
Use Cases
Downloading files
Background processing
GUI applications

24. Async Programming

Modern concurrency.

import asyncio

async def task():
    await asyncio.sleep(1)
    print("Done")

asyncio.run(task())
Difference
Threading	Async
Multiple threads	Single thread
OS scheduling	Event loop
More memory	Less memory

Used heavily in:

FastAPI
Web scraping
APIs

25. Type Hints
def add(a: int, b: int) -> int:
    return a + b

Benefits:

Better readability
IDE suggestions
Static analysis

26. Metaclasses (Very Advanced)

Everything in Python is an object—even classes.

class Person:
    pass

Internally:

Person = type("Person", (), {})

Custom metaclass:

class MyMeta(type):
    pass

class User(metaclass=MyMeta):
    pass

Metaclasses control class creation itself.

27. Descriptors (Expert Level)

Control attribute access.

class Positive:

    def __get__(self, obj, owner):
        return obj._value

    def __set__(self, obj, value):

        if value < 0:
            raise ValueError()

        obj._value = value

Used internally by:

properties
ORM frameworks
Django models
Roadmap to Master Python
Beginner
Variables
Data Types
Operators
Conditions
Loops
Functions
Collections
Intermediate
OOP
Exception Handling
File Handling
Modules
Comprehensions
Lambda
Advanced
Iterators
Generators
Decorators
Closures
Context Managers
Dataclasses
Multithreading
Async Programming
Expert
Descriptors
Metaclasses
Memory Management
GIL Internals
Design Patterns
Python Internals (CPython)

Mastering up to Async Programming, Decorators, Generators, Context Managers, and Advanced OOP is usually enough for most software engineering interviews and professional Python development.

If your goal is to learn Object-Oriented Programming (OOP) completely, the best approach is to build one realistic project that demonstrates every OOP concept.

The following program covers:

✅ Class & Object
✅ Constructor (__init__)
✅ Instance Variables
✅ Class Variables
✅ Instance Methods
✅ Class Methods
✅ Static Methods
✅ Encapsulation
✅ Abstraction
✅ Inheritance
✅ Multilevel Inheritance
✅ Multiple Inheritance
✅ Polymorphism (Method Overriding)
✅ Operator Overloading
✅ Composition
✅ Aggregation
✅ Abstract Classes
✅ Magic Methods (__str__, __add__)
✅ Method Resolution Order (MRO)

Complete OOP Program
from abc import ABC, abstractmethod

# ==========================================
# 1. CLASS VARIABLE + CONSTRUCTOR
# ==========================================

class Person:

    population = 0      # Class Variable

    def __init__(self, name, age):
        self.name = name      # Instance Variable
        self.age = age

        Person.population += 1

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age : {self.age}")

    @classmethod
    def get_population(cls):
        return cls.population

    @staticmethod
    def welcome():
        print("Welcome to OOP Tutorial")

    def __str__(self):
        return f"Person({self.name},{self.age})"


# ==========================================
# 2. ENCAPSULATION
# ==========================================

class BankAccount:

    def __init__(self, balance):

        self.__balance = balance      # Private Variable

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):

        if amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance


# ==========================================
# 3. INHERITANCE
# ==========================================

class Employee(Person):

    def __init__(self, name, age, salary):

        super().__init__(name, age)

        self.salary = salary

    def display(self):

        super().display()

        print(f"Salary: {self.salary}")


# ==========================================
# 4. MULTILEVEL INHERITANCE
# ==========================================

class Manager(Employee):

    def __init__(self, name, age, salary, department):

        super().__init__(name, age, salary)

        self.department = department

    def display(self):

        super().display()

        print(f"Department: {self.department}")


# ==========================================
# 5. POLYMORPHISM
# ==========================================

class Animal:

    def sound(self):
        print("Animal Sound")


class Dog(Animal):

    def sound(self):
        print("Dog Barks")


class Cat(Animal):

    def sound(self):
        print("Cat Meows")


# ==========================================
# 6. ABSTRACTION
# ==========================================

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):

    def __init__(self, length, width):

        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):

    def __init__(self, radius):

        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


# ==========================================
# 7. OPERATOR OVERLOADING
# ==========================================

class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):

        return Number(self.value + other.value)

    def __str__(self):
        return str(self.value)


# ==========================================
# 8. COMPOSITION
# ==========================================

class Engine:

    def start(self):
        print("Engine Started")


class Car:

    def __init__(self):

        self.engine = Engine()

    def start_car(self):

        self.engine.start()

        print("Car Running")


# ==========================================
# 9. AGGREGATION
# ==========================================

class Department:

    def __init__(self, name):

        self.name = name


class University:

    def __init__(self, department):

        self.department = department


# ==========================================
# 10. MULTIPLE INHERITANCE
# ==========================================

class Father:

    def skills(self):
        print("Driving")


class Mother:

    def skills(self):
        print("Cooking")


class Child(Father, Mother):
    pass


# ==========================================
# MAIN PROGRAM
# ==========================================

print("\nCLASS & OBJECT")

p = Person("Rahul", 25)

p.display()

print(p)

print("Population:", Person.get_population())

Person.welcome()


print("\nENCAPSULATION")

account = BankAccount(1000)

account.deposit(500)

account.withdraw(200)

print("Balance:", account.get_balance())


print("\nINHERITANCE")

emp = Employee("John", 30, 50000)

emp.display()


print("\nMULTILEVEL INHERITANCE")

mgr = Manager("David", 40, 90000, "IT")

mgr.display()


print("\nPOLYMORPHISM")

animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()


print("\nABSTRACTION")

r = Rectangle(10, 5)

c = Circle(7)

print("Rectangle Area:", r.area())

print("Circle Area:", c.area())


print("\nOPERATOR OVERLOADING")

n1 = Number(10)

n2 = Number(20)

n3 = n1 + n2

print(n3)


print("\nCOMPOSITION")

car = Car()

car.start_car()


print("\nAGGREGATION")

dept = Department("Computer Science")

uni = University(dept)

print("Department:", uni.department.name)


print("\nMULTIPLE INHERITANCE")

child = Child()

child.skills()

print("\nMRO")

print(Child.__mro__)
OOP Concepts Explained

1. Class and Object

A class is a blueprint.

class Student:
    pass

Object:

s1 = Student()

Think:

Class  -> Car Design
Object -> Actual Car

2. Encapsulation

Hide data and provide controlled access.

self.__balance

Cannot access directly:

account.__balance

Use methods:

account.get_balance()

3. Inheritance

Reuse existing code.

class Employee(Person):

Employee gets all Person features.

4. Polymorphism

Same method, different behavior.

dog.sound()
cat.sound()

Output:

Dog Barks
Cat Meows

5. Abstraction

Hide implementation details.

User only knows:

shape.area()

Not how it is calculated.

6. Composition

"Has-A" relationship.

Car HAS-A Engine
Car
 └── Engine
7. Aggregation

Weak relationship.

University HAS-A Department

Department can exist independently.

8. Multiple Inheritance
class Child(Father, Mother)

Child inherits from both classes.

9. Operator Overloading

Customize operators.

n1 + n2

Internally:

n1.__add__(n2)

10. MRO (Method Resolution Order)

For:

class Child(Father, Mother)

Python searches:

Child
 ↓
Father
 ↓
Mother
 ↓
object

Check using:

print(Child.__mro__)

This is close to a complete OOP reference program for Python interviews and advanced learning.
Common dunder methods:

| Method   | Purpose              |
| -------- | -------------------- |
| **init** | Constructor          |
| **str**  | Print object         |
| **repr** | Debug representation |
| **len**  | len()                |
| **add**  | + operator           |
| **eq**   | == operator          |
| **iter** | Iterator             |
