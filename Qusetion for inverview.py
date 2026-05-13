# 1st way
'''Question: Given two dictionaries, merge them into a single dictionary 
where the keys are the unique keys from both dictionaries and the values 
are lists of values from the original dictionaries that correspond to those keys.
If a key is only present in one dictionary, its value should be a list containing 
just that value.'''
d1 = {"a": 1, "b": 2, "e":6}
d2 = {"b": 3, "c": 4}
all_keys = set(d1.keys()) | set(d2.keys())
print(all_keys)
#Output: {'a': [1], 'b': [2, 3], 'c': [4]}
d5 ={}
for i in all_keys:
    values =[]
    if i in d1:
        values.append(d1[i])
    if i in d2:
        values.append(d2[i])
    d5[i] = values
print(d5)

#2nd way
def merge_and_group(dict1, dict2):
    combined = {}
    # Get all unique keys from both dictionaries
    all_keys = set(dict1.keys()) | set(dict2.keys())
    
    for key in all_keys:
        values = []
        if key in dict1:
            values.append(dict1[key])
        if key in dict2:
            values.append(dict2[key])
        combined[key] = values
        
    return combined

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
print(f"Grouped Merge: {merge_and_group(d1, d2)}")

#question2: Given a dictionary where the keys are authors and the values are lists of their books, create a new dictionary that inverts this relationship, where the keys are book titles and the values are the corresponding authors.
d1 = {"Orwell": ["1984", "Animal Farm"], "Huxley": ["Brave New World"]}
#output = {'1984': 'Orwell', 'Animal Farm': 'Orwell', 'Brave New World': 'Huxley'}
k1 = d1.keys()
v1 = d1.values()
d2 = {}
print(k1)
print(v1)
for i in v1:
    for j in range(len(i)):
        d2[i[j]] = 0
        
print(d2)
#2nd way
def invert_bibliography(data):
    inverted = {}
    for author, books in data.items():
        for book in books:
            inverted[book] = author
    return inverted

# Usage
authors = {
    "Orwell": ["1984", "Animal Farm"],
    "Huxley": ["Brave New World"]
}
print(f"Inverted Index: {invert_bibliography(authors)}")

'''Question3: Given a list of dictionaries (representing employees), sort them based on their “salary” in descending order using a lambda function.'''

employees = [{"name": "A", "salary": 50}, {"name": "B", "salary": 70}, {"name": "C", "salary": 60}]
d1 = sorted(employees,key = lambda x:x["salary"],reverse = True)
d2 = sorted(employees, key = lambda x:x["name"], reverse = True)
print(d1)
print(d2)

#Question4: Given two lists, determine if one is a subset of the other, if they are disjoint, or if they share some common elements. Use set operations to find the relationships between the two lists.
def validate_relationships(list1, list2):
    a = set(list1)
    b = set(list2)
    
    if a.issubset(b):
        print("Set A is a subset of Set B.")
    elif a.issuperset(b):
        print("Set A is a superset of Set B.")
    
    if a.isdisjoint(b):
        print("The sets are disjoint (they share no elements).")
    else:
        print(f"The sets share these elements: {a & b}")

validate_relationships([1, 2], [1, 2, 3, 4])

#Question5: Given two sets, determine if one is a subset of the other, if they are disjoint, or if they share some common elements. Use set operations to find the relationships between the two sets.  
setA = {1, 2, 3}
setB = {1, 2, 3, 4, 5}
print("A is subset of B: ", setA.issubset(setB))
print("B is superset of A : ",setB.issuperset(setA))
print("A is subset of B: " , setA.isdisjoint(setB))


list1 = [101, 102, 103]
list2 = [103, 104, 105]
set1 = set(list1)
set2 = set(list2)
#Expected Output: {101, 102, 104, 105}
# Symmetric difference
difference = set1 ^ set2
print(difference)
diff1 = (set1 or set2) - (set1 and set2)
diff2 = (set1 and set2) -(set1 or set2)
diff3 = diff1.union(diff2)
print(diff1)
print(diff3)

#question6: '''Write a function that generates the Power Set of a given set (a set of all possible subsets, including the empty set and the set itself).'''

Input = [1, 2, 3]
#Output:[(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
from itertools import combinations

def get_power_set(s):
    # Convert input to list to ensure we can index it
    elements = list(s)
    power_set = []
    
    for r in range(len(elements) + 1):
        # Generate all combinations of length r
        for combo in combinations(elements, r):
            power_set.append(combo)
            
    return power_set

# Usage
my_set = {1, 2, 3}
print(f"Power Set: {get_power_set(my_set)}")
'''combinations(elements, r): This built-in function generates all possible ways to pick r items from the list without repetition and regardless of order'''


'''Practice Problem: Create a function that asks for a user’s birthdate (YYYY-MM-DD) and calculates their exact age today in years, months, and days.'''
from datetime import datetime
from dateutil.relativedelta import relativedelta

def calculate_exact_age(birthdate_str):
    try:
        # Parse the input string
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
        today = datetime.now().date()
        
        # Calculate the difference
        diff = relativedelta(today, birthdate)
        
        return f"{diff.years} years, {diff.months} months, {diff.days} days"
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."

# Usage
# Note: You may need to install python-dateutil via pip
user_age = calculate_exact_age("1982-01-20")
print(f"Exact Age: {user_age}")

'''Practice Problem: Write a function that calculates the exact number of days, hours, and minutes remaining until the upcoming New Year’s Day.'''

from datetime import datetime

def countdown_to_new_year():
    now = datetime.now()
    print(now)
    # Target: Jan 1 of the next year
    next_year = now.year + 1
    print(next_year)
    target = datetime(next_year, 1, 1) #datetime(next_year, 1, 1): This creates a fixed point in the future to compare against.
    print(target)
    diff = target - now
    
    days = diff.days
    # Convert remaining seconds into hours and minutes
    hours, remainder = divmod(diff.seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    
    return f"{days} days, {hours} hours, {minutes} minutes"

print(f"Time remaining: {countdown_to_new_year()} until New Year!")

'''Given a list of tuples representing employees (Name, Age, Salary), sort the list primarily by Salary in descending order.'''
employees = [
    ("Alice", 30, 50000),
    ("Bob", 25, 75000),
    ("Charlie", 35, 60000)
]

# Sort by salary (index 2) in descending order
sorted_employees = sorted(employees, key=lambda emp: emp[2], reverse=True)

print("Employees sorted by Salary (High to Low):")
for emp in sorted_employees:
    print(emp)

'''Given a list of numbers, use map() and filter() together to create a list of the squares of only the even numbers.'''
nums = [1, 2, 3, 4, 5, 6]

# 1. Filter even numbers
# 2. Map those numbers to their squares
result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums)))

print(f"Original: {nums}")
print(f"Squares of evens: {result}")

'''Write a decorator function named @timer that prints how many seconds a function takes to execute. Apply it to a function that simulates a heavy computation using time.sleep().'''
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter() # High-precision start
        result = func(*args, **kwargs)# Run the actualfunction
        end_time = time.perf_counter()   # High-precision end
        
        duration = end_time - start_time
        print(f"Function '{func.__name__}' took {duration:.4f} seconds.")
        return result
    return wrapper

@timer
def waste_time():
    time.sleep(3)

waste_time()

'''Create a generator function that yields Fibonacci numbers up to N. Instead of returning a full list, it should yield values one by one.'''
'''A Generator uses the yield keyword to return one value at a time and “pauses” its execution state. '''
def fibonacci_gen(limit):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

# Using the generator
fib = fibonacci_gen(8)

print("First 8 Fibonacci numbers:")
for num in fib:
    print(num, end=" ")
    
'''Create a “Logger” function that accepts a mandatory message string, followed by an unknown number of positional arguments (*args), and an unknown number of keyword arguments (**kwargs). The function should print the message, then list the extra arguments and metadata.'''
'''Exercise Purpose: Intermediate Pythonistas must write functions that are flexible. *args (tuples) and **kwargs (dictionaries) allow your functions to handle dynamic inputs. This is how major libraries like Django or Flask allow for highly customizable function calls.'''
def log_event(message, *args, **kwargs):
    print(f"Event: {message}")
    
    if args:
        print(f"Details: {args}")
    
    if kwargs:
        print(f"Metadata: {kwargs}")

# Usage
log_event("User Login", "admin", "dashboard", timestamp="10:00 AM", status="Success")

''' You have two separate lists: one of student names and one of their exam scores. Use zip() to combine them into a dictionary, then use enumerate() to print a ranked list (1st, 2nd, 3rd…).'''
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

# Merge lists into a dictionary
score_map = dict(zip(names, scores))
print(score_map)
# Sort by score (value) descending
ranked_scores = sorted(score_map.items(), key=lambda item: item[1], reverse=True)
print(ranked_scores)
# Enumerate for ranking
for i, (name, score) in enumerate(ranked_scores, start=1):
    print(f"Rank {i}: {name} scored {score}")
    
'''
input:
trial = [1, 2, 3, 4, 5]
paid = [4, 5, 6, 7, 8]
output:
Upgraded (Both): {4, 5}
Leads (Trial only): {1, 2, 3}
Unique Status (Not both): {1, 2, 3, 6, 7, 8}'''

trial = {1, 2, 3, 4, 5} # Converted to sets
paid = {4, 5, 6, 7, 8}

upgraded = trial & paid
leads = trial - paid
unique = trial ^ paid

print(f"Upgraded (Both): {upgraded}")
print(f"Leads (Trial only): {leads}")
print(f"Unique Status (Not both): {unique}")

'''Problem: Create a base class Vehicle with an attribute called brand and a method fuel_type(). Then, create a subclass ElectricCar that inherits from Vehicle and overrides the fuel_type() method to return “Electricity.”'''
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def fuel_type(self):
        return "Petrol/Diesel"

class ElectricCar(Vehicle):
    # Override the fuel_type method
    def fuel_type(self):
        return "Electricity"

# Usage
my_tesla = ElectricCar("Tesla")
print(f"Brand: {my_tesla.brand}")
print(f"Fuel Type: {my_tesla.fuel_type()}")

'''Problem: Create a BankAccount class where the balance is a private attribute (cannot be accessed directly from outside the class). Provide deposit and withdraw methods to modify the balance safely.'''
class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New Balance: {self.__balance}")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New Balance: {self.__balance}")
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self.__balance

# Usage
acc = BankAccount(100)
acc.deposit(50)
acc.withdraw(200)
print(f"Final Balance: {acc.get_balance()}")

'''
Property Decorators (@property)
Practice Problem: Create a Student class with a name and a score. Use the @property decorator to create a getter for the score, and a @score.setter to ensure that any score assigned is between 0 and 100.'''
class Student:
    def __init__(self, name):
        self.name = name
        self._score = 0 # Internal storage

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if 0 <= value <= 100:
            self._score = value
        else:
            raise ValueError("Score must be between 0 and 100.")

# Usage
s = Student("Kevin")
try:
    s.score = 95  # Looks like attribute assignment, but calls the setter
    print(f"{s.name}'s score: {s.score}")
    s.score = 105 # This will fail
except ValueError as e:
    print(f"Error: {e}")
    
'''@property: This turns the score() method into a “getter.” You access it via s.score instead of s.score().
@score.setter: This method is triggered when you try to use the = operator. It allows for “invisible” data validation.'''
'''Class Methods vs. Static Methods:
Problem: Create a class Pizza that has a price attribute. Implement a @classmethod called margherita() that returns a pre-configured Pizza object and a @staticmethod called validate_topping() that checks if a topping is “healthy.”
'''
class Pizza:
    def __init__(self, name, toppings):
        self.name = name
        self.toppings = toppings

    @classmethod
    def margherita(cls):
        # Returns a new instance of the class (factory pattern)
        return cls("Margherita", ["cheese", "tomato"])

    @staticmethod
    def validate_topping(topping):
        # Independent utility logic
        prohibited = ["plastic", "metal"]
        return topping not in prohibited

# Usage
order = Pizza.margherita()
print(f"Pizza ordered: {order.name}")
print(f"Is 'mushrooms' valid? {Pizza.validate_topping('mushrooms')}")

'''Magic Methods (__str__ and __add__)
Practice Problem: Create a Point class that represents (x, y) coordinates. Implement __str__ so that printing the object looks like (x, y) and implement __add__ so that p1 + p2 adds the coordinates together.'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Controls how the object is printed
    def __str__(self):
        return f"({self.x}, {self.y})"

    # Overloads the '+' operator
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Point(new_x, new_y)

# Usage
p1 = Point(1, 2)
p2 = Point(3, 4)
combined = p1 + p2

print(f"Point 1: {p1}")
print(f"Point 2: {p2}")
print(f"Combined Result: {combined}")
