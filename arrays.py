# Mini Syllabus: Introduction to Arrays

# 1. What are Arrays?

# Definition of arrays.
# How arrays are used to store multiple elements of the same data type.
# Basic terminology: index, element, length.

# 2. Creating and Initializing Arrays

# Declaring an array in Python.
# Initializing arrays with values.
# Accessing array elements using indices.

# 3. Array Operations

# Modifying array elements.
# Adding and removing elements.
# Slicing arrays to extract sub-arrays.
# Looping through arrays using for loops.

# 4. Multidimensional Arrays

# Creating and working with 2D arrays.
# Accessing elements in a 2D array.
# Applications of multidimensional arrays.

# 5. Common Array Methods

# Finding the length of an array.
# Finding maximum and minimum values.
# Sorting and reversing arrays.
# Searching for elements.

# 6. Practical Applications

# Use cases of arrays in programming.
# Examples from fields like data analysis, graphics, and game development.

# Exercises:

import numpy as np
import time
import math

# 1. Create an Array:
# Declare an array containing your favorite colors. Print the second color in the array.

colour_array = ["blue", "green", "purple", "yellow", "pink"]
print(colour_array[1])

# 2. Modify Array Elements:
# Create an array of numbers. Change the third element to 10. Print the updated array.

numbers = [54, 23, 99, 40, 33, 20, 21]
numbers[2] = 10

print(numbers)
for num in numbers:
    print(num)

# 3. Slice and Dice:
# Create an array of characters representing a word. Print only the middle characters using slicing.

sliceword = "charcoals"
length = len(sliceword)
middle = length // 2 # integer division

if length % 2 == 1:
    odd_character = sliceword[middle]
    print("Middle: ", odd_character)
else:
    even_characters = sliceword[middle - 1:middle + 1]
    print("Middle: ", even_characters)

# 4. Concatenation:
# Create two arrays of names: male and female names. Concatenate them into a single array and print it.

male = ['david', 'stian', 'tom', 'andrew']
female = ['claire', 'christina', 'jill', 'zoe']
unisex = male + female
print(unisex)

unisex_in_order = []
for i in range(len(female)):
    unisex_in_order.append(male[i])
    unisex_in_order.append(female[i])

print(unisex_in_order)

# 5. 2D Array Initialization:
# Create a 3x3 matrix with integer values. Print the value in the second row, third column.

# creating the 3x3 matrix
matrix = [
    [5, 6, 4],
    [4, 5, 6],
    [3, 9, 8]
]
print(matrix[1][2])

# generate a 3x3 matrix with random numbers between 0 and 1
random_matrix = np.random.rand(3, 3)
print(random_matrix)
print(random_matrix[1][2])

# generate a 3x3 matrix with random integers between 1 and 10
random_int_matrix = np.random.randint(1, 11, size=(3, 3))
print(random_int_matrix)
print(random_int_matrix[1][2])

# 6. Array Manipulation:
# Given an array, double the value of each element. Print the modified array.

unmodified = [55, 84, 32, 92, 54]
manipulated = []
for i in range(len(unmodified)):
    manipulated.append(unmodified[i] * 2)

print(manipulated)

# using numpy as random generator
start_time = time.time()

numpy_unmod = np.random.randint(1, 151, size=(1000000))
numpy_manip = []

for i in range(len(numpy_unmod)):
    numpy_manip.append(numpy_unmod[i] * 2)

print(numpy_manip)

end_time = time.time()
elapsed_time = end_time - start_time
print(f'time:{elapsed_time:.2f}')

# lambda
start_time = time.time()

numpy_unmod = np.random.randint(1, 151, size=(100))
lambdarray = list(map(lambda x: 2 * x, numpy_unmod))
print(lambdarray)

end_time = time.time()
elapsed_time = end_time - start_time
print(f'time:{elapsed_time:.2f}')

# list comprehension version
# this is the fastest way to do this
start_time = time.time()

numpy_unmod = np.random.randint(1, 151, size=(100))
[n * 2 for n in numpy_unmod]

end_time = time.time()
elapsed_time = end_time - start_time
print(f'time:{elapsed_time:.2f}')

# 7. Array Searching:
# Create an array of numbers. Check if a specific number is present in the array or not.

library = [55, 94, 32, 54, 23]

searching_for = 33
if searching_for not in library:
    print(f"{searching_for} is not present in the list.")
else:
    print(f"{searching_for} is present in the list.")

# 8. Finding Extremes:
# Create an array of temperatures. Find the highest and lowest temperatures in the array.

temperatures = np.random.randint(0, 50, size=(25))
coldest = 50
hottest = 0
for i in temperatures:
    if coldest >= i:
        coldest = i
    elif hottest <= i:
        hottest = i

print(temperatures)
print(coldest)
print(hottest)

# 9. Sorting Array:
# Create an array of random numbers. Sort the array in ascending order and print the result.

sorting = np.random.randint(0, 100, size=(50))
print(sorting)
sorting.sort()#(reverse=True) for descending
print(sorting)

# 10. Array Summation:
# Create an array of integers. Calculate and print the sum of all the elements in the array.

summation = np.random.randint(0, 50, size=(5))
print(summation)
sum(n for n in summation)

# These exercises cover a range of array-related concepts and practical scenarios. 
# They'll help reinforce your understanding and give you hands-on experience with array manipulation in Python. 
# Remember, practice is key to mastering arrays and programming in general. 
# Good luck, and feel free to ask if you have any questions!

# In addition: playing around with palindromes

testing_cases = ['hello', 'there', 'am', 'testing']
[n.upper() for n in testing_cases]

words = ["level", "python", "radar", "programming"]
[word for word in words if word == word[::-1]]

# [::-1]: This specifies slicing with a step of -1, which means it will iterate through the string in reverse order.
# So, when you use word[::-1], you're essentially creating a new string by starting at 
# the end of the original string and moving towards the beginning with a step of -1. This effectively reverses the string.

for i in range(len(words)):
    print(words[i][::-1])

# Bonus question: 
# Find all the numbers that are divisible by 43 up to 10000 that start and end with the same number.

mirrors = []
for n in range(10001):
    if n % 43 == 0:
        mirrors.append(n)

for i in range(len(mirrors)):
    index = str(mirrors[i])
    if index[0] == index[len(index)-1]:
        print(index)

# list comprehension version:

divides_true = [i*43 for i in range(math.floor(10000 / 43))]
[n for n in divides_true if str(n)[0] == str(n)[-1]] 
# remember that -1 counts as the final index

# another version:

mirrors = []
for i in range(233):
    index = str(i*43)
    if index[0] == index[-1]:
        mirrors.append(index)

print(mirrors)