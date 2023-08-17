# Mini Syllabus for Learning Functions in Python:

import math
from functools import lru_cache

# 1. Introduction to Functions

# What are functions?
# Why use functions?
# Syntax of defining a function.
# Calling a function.
# Return values and return statement.

# 2. Function Parameters and Arguments

# Defining functions with parameters.
# Positional and keyword arguments.
# Default parameter values.
# Variable-length argument lists (*args and **kwargs). Such as:

def my_function(arg1, arg2, *args, **kwargs):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("additional positional args:", args)
    print("additional keyword args:", kwargs)

my_function(1, 2, 3, 4, name="Alice", age=30)
# Prints:
# arg1: 1
# arg2: 2
# additional positional args: (3, 4)
# additional keyword args: {'name': 'Alice', 'age': 30}

# 3. Scope and Lifetime of Variables

# Local vs. global variables.
# Understanding variable scope.
# Modifying global variables from within a function (using global keyword).

# 4. Function Recursion

# Practical use of recursive function in software:

import os

def list_files_in_directory(directory):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item) # returns to original folder
        if os.path.isfile(item_path):
            print(item_path)
        elif os.path.isdir(item_path):
            list_files_in_directory(item_path)

# Start traversal from a specific directory
start_directory = "/path/to/start/directory"
list_files_in_directory(start_directory)

# This function lists all of the files in a directory, 
# We benefit from the recursive use-case (line 59) as it can open a subfolder and then list the items of that subfolder

# Base cases and recursive cases.
# Pros and cons of recursion.

# 5. Built-in Functions and Modules

# Exploring Python's built-in functions (e.g., print, len, max).
# Introduction to Python modules and importing functions.

# 6. Practical Applications of Functions

# Structuring code for better organization.
# Code reusability and maintainability.
# Solving complex problems by breaking them into smaller functions.
# Function Applications in Programming:

# Functions are blocks of reusable code that perform a specific task. They allow you to organize your code, improve readability, and make your program more modular. Here are some key places where functions are relevant and useful:

# Code Reusability: Instead of writing the same code multiple times, you can define a function and call it whenever needed. This saves time and reduces code duplication.

# Modularity: Functions help break down complex problems into smaller, manageable parts. Each function focuses on a specific task, making it easier to understand and maintain the code.

# Abstraction: Functions abstract away the implementation details, allowing you to use a function without needing to know how it's internally implemented.

# Testing and Debugging: Debugging is simpler when functions are used because you can isolate and fix issues within specific functions.

# Collaboration: Functions enable teams to work on different parts of a program simultaneously and integrate their work seamlessly.

# Readability: Well-named functions with clear purposes make your code easier to read and understand.

# 10 Exercises to Practice:

# Here are 10 exercises to help you practice using functions in Python:

# 1. Write a function to calculate the factorial of a given number.

def factorial_simple(n):
    return math.factorial(n) # this is basically pointless as it already exists

def factorial_recursive(n):
    if n == 0:
        return 1 # Base case: factorial of 0 is 1
    else:
        return n * factorial_recursive(n - 1) # Recursive case: n! = n * (n-1)!

# 2. Create a function that checks if a number is prime.

def prime_fastest_process(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0:
        return False

    sqrt_n = int(math.sqrt(n))
    return all(n % divisor != 0 and n % (divisor + 2) != 0 for divisor in range(5, sqrt_n + 1, 6))

def prime_simple_to_read_and_understand(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(math.sqrt(n))
    for divisor in range(5, sqrt_n + 1, 6):
        if n % divisor == 0 or n % (divisor + 2) == 0:
            return False
    return True
    
for i in range(0, 100):
    if prime_fastest_process(i):
        print(i)

primes = [i for i in range(0, 100) if prime_fastest_process(i)]
print(primes)

print([i for i in range(0, 100) if prime_fastest_process(i)]) # without variable

# 3. Implement a function that converts Celsius to Fahrenheit.

def celsius_to_fahrenheit(t):
    return f"{float(t)}°C in Fahrenheit is {((t * 9 / 5) + 32)}°F"

print(celsius_to_fahrenheit(32))

# 4. Write a function that finds the largest element in a list.

def element_largest(data):
    if isinstance(data, list) and all(isinstance(item, str) for item in data):
        largest = 0
        words = ""
        for s in data:
            if largest == len(s):
                words += ", " + s
            elif largest < len(s):
                words = s
                largest = len(s)
        return f"Largest word/s: {words}. Character count: {largest}."

    elif isinstance(data, list) and all(isinstance(item, int) for item in data): 
        largest = 0
        for i in data:
            if largest < i:
                largest = i
        return largest
    
    else:
        print("Input is of unknown data type.")    

def list_comprehension_element_largest(data):
    if all(isinstance(item, str) for item in data):
        longest_length = max(len(s) for s in data)
        longest_words = [s for s in data if len(s) == longest_length]
        return f"Largest word/s: {', '.join(longest_words)}. Character count: {longest_length}."

    elif all(isinstance(item, int) for item in data):
        return max(data, default=None)
    
    else:
        return "Input is of unknown data type."
    
list_test = [44, 32, 12, 49, 342]
string_list_test = ['nest', 'nestle', 'mould', 'fortitude', 'beacons', 'traverses']

print(list_comprehension_element_largest(list_test))
print(list_comprehension_element_largest(string_list_test))

# 5. Create a function that reverses a string.

def reverse_string(rev):
    palindrome = rev[::-1]
    return palindrome

input_string = input("Enter a string: ")
palindrome_string = reverse_string(input_string)
print("Palindrome: ", palindrome_string)

# 6. Build a function that generates Fibonacci numbers up to a given limit.

def fibonacci_sequence(limit, a=0, b=1):
    if a <= limit:
        print(a, end=" ")
        fibonacci_sequence(limit, b, a + b)

# when the recursive step is taken, the parameters change as such:
# limit = 1000, a = 1, b = 1
# limit = 1000, a = 2, b = 3
# limit = 1000, a = 3, b = 5

limit = 1000
fibonacci_sequence(limit)

def fibonacci_sequence(limit):
    a, b = 0, 1
    fib_sequence = []
    while a <= limit:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

limit = 1000
sequence = fibonacci_sequence(limit)
print(sequence)

# 7. Implement a function to calculate the area of different geometric shapes (circle, rectangle, triangle, etc.).

def rectangle_areas(length, width):
    return length * width

def triangle_areas(base, height):
    return 0.5 * base * height

def circle_areas(radius):
    return 3.14159 * radius ** 2

def calculate_shapes():
    length = 10
    width = 5
    rectangle = rectangle_areas(length, width)
    print("Rectangle area:", rectangle)

    base = 8
    height = 4
    triangle = triangle_areas(base, height)
    print("Triangle area:", triangle)

    radius = 3
    circle = circle_areas(radius)
    print("Circle area:", circle)

calculate_shapes()

length = 10
width = 5
print("Rectangle area:", rectangle_areas(length, width))

base = 8
height = 4
print("Triangle area:", triangle_areas(base, height))

radius = 3
print("Circle area:", circle_areas(radius))

# 8. Write a function that counts the occurrences of each word in a text.

def count_word_occurrences(text):
    words = text.lower().split()
    word_counts = {word: words.count(word) for word in set(words)}
    
    for word, count in word_counts.items(): 
        print(f"The word '{word}' appears {count} times in the sentence.")

count_sentence = "This is an example sentence. This sentence contains the word example multiple times."
count_word_occurrences(count_sentence)

# 9. Create a function that checks if a string is a palindrome.

def is_it_palindrome(text):
    return bool(text == text[::-1])

palindrome_sentence = "radar"
print(is_it_palindrome(palindrome_sentence))

words = ["level", "python", "radar", "programming"]
[word for word in words if word == word[::-1]]

# 10. Build a function that simulates a basic calculator with addition, subtraction, multiplication, and division operations.

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def basic_calculator(first, operation, second):
    operations = ["addition", "subtraction", "multiplication", "division"]
    operation_functions = {
        "addition": add,
        "subtraction": subtract,
        "multiplication": multiply,
        "division": divide
    }

    if operation in operations:
        return operation_functions[operation](first, second)
    else:
        return "Invalid operation."

try:
    first_input = float(input("Enter the first number: "))
    operation_input = input("Choose an operation (addition, subtraction, multiplication, division): ").lower()
    second_input = float(input("Enter the second number: "))
    
    result = basic_calculator(first_input, operation_input, second_input)
    print("Result:", result)
except ValueError:
    print("Invalid input. Please enter valid numbers.")    

# Remember, practicing these exercises will help solidify your understanding of functions and their applications in Python programming. 
# Good luck, and don't hesitate to ask if you need further assistance!