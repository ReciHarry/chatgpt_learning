# Here are 15 exercises where you'll be given a piece of code, and your task is to rewrite it using list operations like map, filter, reduce, iterable objects and list comprehensions. 
# Remember that the goal is to achieve the same functionality using these operations.

# Exercise 1:
# Original code:

numbers = [1, 2, 3, 4, 5]
squared = []
for num in numbers:
    squared.append(num ** 2)

# Convert to list comprehension or map:
numbers = [1, 2, 3, 4, 5]
squared = [num ** 2 for num in numbers]
squared = list(map(lambda num: num ** 2, numbers))

# Exercise 2:
# Original code:

words = ['hello', 'world', 'this', 'is', 'a', 'test']
lengths = []
for word in words:
    lengths.append(len(word))

# Convert to list comprehension or map:
words = ['hello', 'world', 'this', 'is', 'a', 'test']
lengths = [len(word) for word in words]
lengths = list(map(len, words))

# Exercise 3:
# Original code:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)
# Convert to list comprehension or filter:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [num for num in numbers if num % 2 == 0]
evens = list(filter(lambda num: num % 2 == 0, numbers))

# Exercise 4:
# Original code:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
product = 1
for num in numbers:
    product *= num

# Convert to reduce:

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
product = reduce(lambda x, y: x * y, numbers)

# Exercise 5:
# Original code:

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_even = []
for num in numbers:
    if num % 2 == 0:
        squared_even.append(num ** 2)

# Convert to list comprehension with conditional:
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_even = [num ** 2 for num in numbers if num % 2 == 0]

# Exercise 6:
# Original code:

words = ['apple', 'banana', 'cherry', 'date', 'elderberry']
uppercase_words = []
for word in words:
    uppercase_words.append(word.upper())

# Convert to list comprehension:
words = ['apple', 'banana', 'cherry', 'date', 'elderberry']
uppercase_words = [word.upper() for word in words]

# Exercise 7:
# Original code:

numbers = [1, 2, 3, 4, 5]
doubled = []
for num in numbers:
    doubled.append(num * 2)

# Convert to list comprehension:
numbers = [1, 2, 3, 4, 5]
doubled = [num * 2 for num in numbers]

# Exercise 8:
# Original code:

sentence = "This is a sample sentence."
words = sentence.split()
capitalized_words = []
for word in words:
    capitalized_words.append(word.capitalize())

# Convert to list comprehension:
sentence = "This is a sample sentence."
words = sentence.split()
capitalized_words = [word.capitalize() for word in words]

# Exercise 9:
# Original code:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_squares = []
for num in numbers:
    if num % 2 != 0:
        odd_squares.append(num ** 2)

# Convert to list comprehension with conditional:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_squares = [num ** 2 for num in numbers if num % 2 != 0]

# Exercise 10:
# Original code:

numbers = [10, 20, 30, 40, 50]
incremented = []
for num in numbers:
    incremented.append(num + 5)

# Convert to list comprehension:
numbers = [10, 20, 30, 40, 50]
incremented = [num + 5 for num in numbers]

# Exercise 11:
# Original code:

words = ['hello', 'world', 'python', 'list', 'comprehension']
filtered_words = []
for word in words:
    if len(word) > 5:
        filtered_words.append(word)

# Convert to list comprehension with conditional:
words = ['hello', 'world', 'python', 'list', 'comprehension']
filtered_words = [word for word in words if len(word) > 5]

# Exercise 12:
# Original code:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_of_squares = 0
for num in numbers:
    sum_of_squares += num ** 2

# Convert to reduce:
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
summed = sum(num ** 2 for num in numbers)
sum_of_squares = reduce(lambda x, y: x + y ** 2, numbers, 0)

# Exercise 13:
# Original code:

numbers = [10, 25, 30, 45, 50, 65]
even_halves = []
for num in numbers:
    if num % 2 == 0:
        even_halves.append(num // 2)

# Convert to list comprehension with conditional:
numbers = [10, 25, 30, 45, 50, 65]
even_halves = [num // 2 for num in numbers if num % 2 == 0]

# Exercise 14:
# Original code:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cubed_odd_sum = 0
for num in numbers:
    if num % 2 != 0:
        cubed_odd_sum += num ** 3

# Convert to list comprehension with conditional and sum:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cubed_odd_sum = sum(num ** 3 for num in numbers if num % 2 != 0)

# Exercise 15:
# Original code:

names = ['Alice', 'Bob', 'Charlie', 'David', 'Emily']
name_lengths = {}
for name in names:
    name_lengths[name] = len(name)

# Convert to dictionary comprehension:
names = ['Alice', 'Bob', 'Charlie', 'David', 'Emily']
name_lengths = {name: len(name) for name in names}

# Just as an extra. Messing around with dictionary iterables.

from faker import Faker
import numpy as np

faker = Faker()
testing_further = {faker.name(): np.random.randint(20, 51) for _ in range(10)}

# Extending this:

class CustomDataGenerator:
    def __init__(self, count):
        self.count = count
        self.faker = Faker()
        self.current_item = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_item < self.count:
            name = self.faker.name()
            value = np.random.randint(20, 51)
            self.current_item += 1
            return name, value
        else:
            raise StopIteration
        
    def generate_data(self):
        return [(self.faker.name(), np.random.randint(20, 51)) for _ in range(self.count)]

data_generator = CustomDataGenerator(count=20)
data = data_generator.generate_data()

for name, value in data:
    print(f"Name: {name}, Value: {value}")

for name, value in data_generator:
    print(f"Name: {name}, Value: {value}")