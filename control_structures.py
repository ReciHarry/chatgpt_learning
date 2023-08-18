import numpy as np

# Control Structures Mini Syllabus:

# 1. Introduction to Control Structures:

# Explanation of what control structures are.
# Overview of the three main types: sequential, conditional, and repetitive.

# 2. Conditional Control Structures (Decision Making):

# if statement: Using a single condition.
# if-else statement: Adding an alternative path.
# if-elif-else statement: Handling multiple conditions.
# nested if statements: Conditions within conditions.
# Application: Creating dynamic responses based on user input or data conditions.

# 3. Repetitive Control Structures (Loops):

# while loop: Repeating code while a condition is true.
# for loop: Iterating over a sequence (e.g., a list or a range).
# break and continue statements: Controlling loop execution.
# Nested loops: Using loops within loops.
# Application: Automating repetitive tasks, processing data, and creating patterns.

# Exercises:
# Here are 10 exercises to help you practice and understand the applications of control structures. Each exercise has a unique purpose to reinforce your learning:

# Exercise 1:
# Print all even numbers from 1 to 20 using a loop.

for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# Exercise 2:
# Create a program that asks the user for their age and determines if they are eligible to vote (18 years or older).

user_age = input("What is your age?")
if int(user_age) >= 18:
    print("You can vote")
else:
    print("You can't vote")

# Exercise 3:
# Write a program to calculate the factorial of a given number using a loop.

fact_num = 8
fact_result = 1

for f in range(1, fact_num + 1):
    fact_result *= f

print(fact_result)

# Exercise 4:
# Create a simple guessing game where the computer generates a random number and the player has to guess it.

while True:
    random_int = np.random.randint(1, 11)
    print(random_int)
    
    while True:
        player_input = int(input("What number am I thinking of between 1 and 10? "))
        
        if player_input != random_int:
            print("Try again.")
        else:
            play_again = input("Correct! Would you like to play again? (yes/no): ")
            if play_again.lower() == "no":
                print("Thanks for playing!")
                break  
            elif play_again.lower() == "yes":
                break  # Restart the inner loop with a new random number
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
    
    if play_again.lower() == "no":
        break  

# Exercise 5:
# Print the Fibonacci sequence up to the 10th term.

fibo_list = []
a = 0
b = 1

for _ in range(10):
    fibo_list.append(a)
    temp = a
    a = b
    b = temp + b

print(fibo_list)

# another way
fibonacci_sequence = [0, 1]

for _ in range(8):
    next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
    fibonacci_sequence.append(next_term)

print(fibonacci_sequence)

# Exercise 6:
# Write a program that prints the multiplication table of a given number.

multi_table = []
multi_by = int(input("Choose a number to multiply: "))

for x in range(1, 13):
    print(f"{multi_by} x {x} = {multi_by * x}")
    multi_table.append(x * multi_by)

print(multi_table)

# Exercise 7:
# Create a program that checks if a given word is a palindrome (reads the same forwards and backwards).

word = "raddfsar"
palin = True

if palin:
    palin = (word == word[::-1])

if palin:
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")

# Exercise 8:
# Implement a basic calculator that performs addition, subtraction, multiplication, or division based on user input.

while True:
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    
    choice = input("Enter choice (1/2/3/4/5): ")
    
    if choice == '5':
        print("Exiting the calculator.")
        break
    
    if choice not in ('1', '2', '3', '4'):
        print("Invalid choice. Please enter a valid option.")
        continue
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if choice == '1':
        print(f"Result: {num1} + {num2} = {num1 + num2}")
    elif choice == '2':
        print(f"Result: {num1} - {num2} = {num1 - num2}")
    elif choice == '3':
        print(f"Result: {num1} * {num2} = {num1 * num2}")
    elif choice == '4':
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            print(f"Result: {num1} / {num2} = {num1 / num2}")

# Exercise 9:
# Generate a list of prime numbers within a given range.

start_range = int(input("Enter the starting range: "))
end_range = int(input("Enter the ending range: "))

prime_numbers = []

for num in range(max(2, start_range), end_range + 1):
    is_prime = True
    
    for divisor in range(2, int(num**0.5) + 1):
        if num % divisor == 0:
            is_prime = False
            break
    
    if is_prime:
        prime_numbers.append(num)

print("Prime numbers within the range:", prime_numbers)

# Exercise 10:
# Write a program that simulates a simple ATM, allowing users to deposit, withdraw, and check their balance.

while True:
    if balance == 0:
        balance = int(np.random.normal(2900, 500))
    
    print("Select Service:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = input("Enter choice (1/2/3/4: ")
    
    if choice == '4':
        print("Thank you for using Harry's Bank.")
        print("Take care and have a great day.")
        break
    
    if choice not in ('1', '2', '3'):
        print("Invalid choice. Please enter a valid option.")
        continue
        
    if choice == '1':
        print(f"Your Balance: {balance}")
    elif choice == '2':
        num = int(input("Select the amount you wish to deposit (Pounds only): "))
        balance += num
        print(f"Balance is now: {balance}")
        continue
    elif choice == '3':
        num = int(input("Select the amount you wish to withdraw (Pounds only): "))
        balance -= num
        print(f"Balance is now: {balance}")
        continue