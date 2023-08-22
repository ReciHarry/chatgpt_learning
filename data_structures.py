import numpy as np
import math

# Mini Syllabus: Data Structures and Their Applications

# 1. Lists

# Definition: An ordered collection of elements.
# Application: Used for storing and manipulating sequences of data, like a list of items, records, or values.

# 2. Tuples

# Definition: Similar to lists, but immutable (cannot be modified after creation).
# Application: Used to store data that should not be changed, like coordinates or elements in a dictionary.

# 3. Sets

# Definition: An unordered collection of unique elements.
# Application: Useful for eliminating duplicates and performing set operations like union, intersection, and difference.

# 4. Dictionaries

# Definition: Stores key-value pairs, allowing fast access to values using keys.
# Application: Efficient for mapping data relationships, such as storing user data, configurations, or word frequency counts.

# 5. Stacks

# Definition: A linear data structure that follows the Last-In-First-Out (LIFO) principle.
# Application: Used for managing function calls, undo operations, and implementing algorithms like depth-first search.

# 6. Queues

# Definition: A linear data structure that follows the First-In-First-Out (FIFO) principle.
# Application: Useful for managing tasks in the order they were added, like print job scheduling and breadth-first search.

# 7. Linked Lists

# Definition: A linear data structure consisting of nodes, where each node points to the next node in the sequence.
# Application: Great for dynamic memory allocation and implementing advanced data structures like stacks, queues, and graphs.

# 8. Trees

# Definition: A hierarchical data structure with a root node and child nodes.
# Application: Used in hierarchical data representation, file systems, binary search trees, and more.

# 9. Hash Tables

# Definition: Data structure that stores key-value pairs and uses a hash function to map keys to indexes.
# Application: Enables fast data retrieval and is used in dictionaries, caches, and database indexing.

# 10. Graphs

# Definition: A collection of nodes (vertices) and edges that connect pairs of nodes.
# Application: Essential for modeling relationships between objects, social networks, network routing, and more.

# Exercises:
# Now, here are 10 exercises to help you practice and reinforce your understanding of these data structures:

# Create a function to reverse a list without using built-in reverse methods.

def reverse_list(list):
    return list[::-1]

int_array = np.random.randint(0, 101, size=10)
print(int_array)
print(reverse_list(int_array))

# Implement a tuple that stores the dimensions of a rectangle and calculate its area.

rectuple = (4, 10)
width, length = rectuple
print(width * length)
print(rectuple[0] * rectuple[1])

# Remove duplicates from a list using a set.

duplicate_list = [44, 44, 23, 23, 99, 99, 55, 55, 35, 35]
unique_set = set()
for value in duplicate_list:
    if value not in unique_set:
        unique_set.add(value)

print(unique_set)        

# Build a dictionary to store the names and ages of a group of people.

names = ['Tony', 'Joy', 'Claire', 'Fran']
ages = 12, 15, 13, 13

student_dict = {}

for person, age in zip(names, ages):
    student_dict[person] = age

for person, age in student_dict.items():
    print(f"{person}, {age}")

# Implement a stack and evaluate a simple arithmetic expression (e.g., "3 + 4 * 2").

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Tokenization: Break down the arithmetic expression into tokens, which can be numbers, operators, or parentheses. 
# Splitting the expression into tokens makes it easier to evaluate.    
expression = "3 + 4 * 2"
tokens = expression.split()  # Split by whitespace
print(tokens)  # Output: ['3', '+', '4', '*', '2']

# Operator Precedence: Define the precedence of operators. 
# Multiplication has higher precedence than addition. 
# We can use a dictionary to represent operator precedence.
precedence = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2
}

# Evaluate the Expression:
# Create an empty stack to hold operators.
# Iterate through the tokens.
# If the token is a number, push it onto the stack.
# If the token is an operator, pop operators from the stack and apply them based on precedence until a lower-precedence operator is encountered or the stack is empty.
# Push the current operator onto the stack.
# Finally, pop any remaining operators from the stack and apply them.
def evaluate_expression(expression):
    stack = Stack()
    output = []
    
    for token in tokens:
        if token.isnumeric():
            output.append(int(token))
        elif token in precedence:
            while (not stack.is_empty() and
                   stack.peek() in precedence and
                   precedence[stack.peek()] >= precedence[token]):
                output.append(stack.pop())
            stack.push(token)
    
    while not stack.is_empty():
        output.append(stack.pop())
    
    return output

# Evaluate the Postfix Expression: Use the Shunting Yard algorithm to convert the postfix expression (output from step 4) into the final result.
def evaluate_postfix(postfix_tokens):
    stack = Stack()
    
    for token in postfix_tokens:
        if isinstance(token, int):
            stack.push(token)
        elif token in precedence:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2
            stack.push(result)
    
    return stack.pop()

# Combine all steps
tokens = expression.split()
postfix_expression = evaluate_expression(tokens)
result = evaluate_postfix(postfix_expression)
print(result)

# It should be noted that this stack solution is not a result of my work.
# I will spend an extended period of time studying stacks.

# Create a queue data structure using lists and perform enqueue and dequeue operations.

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    
my_queue = Queue()
my_queue.enqueue(5)
my_queue.enqueue(10)
my_queue.enqueue(15)

for _ in my_queue.items[:]:
    my_queue.dequeue()

print("Is queue empty?", my_queue.is_empty())
print("Queue size:", my_queue.size())

# Implement a singly linked list with methods to append, insert, and delete nodes.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert(self, value, position):
        if position == 0:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        new_node = Node(value)
        new_node.next = current.next
        current.next = new_node

    def delete(self, value):
        if self.head and self.head.value == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next
        raise ValueError(f"{value} not found in the list")

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

sll = SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.display()  

sll.insert(15, 1) # appends at index 1
sll.display()  

sll.delete(20)
sll.display() 

# Build a binary search tree and implement the "search" functionality.

from functools import reduce

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def search(root, target):
    if root is None or root.value == target:
        return root
    if target < root.value:
        return search(root.left, target)
    return search(root.right, target)

values = [10, 5, 15, 3, 7, 20]
root = reduce(insert, values, None)

target_value = 7
result_node = search(root, target_value)
if result_node:
    print(f"Value {target_value} found!")
else:
    print(f"Value {target_value} not found.")

# Create a simple hash table to store contact information (name, phone number).

from faker import Faker

class SimpleHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self.hash_function(key)
        self.table[index].append(value)

    def get(self, key):
        index = self.hash_function(key)
        return self.table[index]

faker = Faker()

random_table = SimpleHashTable(size=15)
for _ in range(15):
    name, age = faker.name(), np.random.randint(18, 56)
    random_table.put("name", name)
    random_table.put("age", age)

names, ages = random_table.get("name"), random_table.get("age")

for name, age in zip(names, ages):
    print(f"Name: {name}. Age: {age}")

# Represent a graph using an adjacency matrix and find the shortest path between two nodes.

num_nodes = 4
adjacency_matrix = np.zeros((num_nodes, num_nodes), dtype=int)

edges = [(0, 1), (1, 2), (2, 3), (0, 3)]
for edge in edges:
    i, j = edge
    adjacency_matrix[i, j] = 1
    adjacency_matrix[j, i] = 1

def print_graph(matrix):
    for row in matrix:
        row_str = " ".join(str(value) for value in row)
        print(row_str)

def dijkstra(graph, start):
    distances = [math.inf] * num_nodes
    distances[start] = 0
    visited = [False] * num_nodes

    for _ in range(num_nodes):
        min_dist = math.inf
        min_node = -1

        for node in range(num_nodes):
            if not visited[node] and distances[node] < min_dist:
                min_dist = distances[node]
                min_node = node

        if min_node == -1:
            break

        visited[min_node] = True

        for neighbor in range(num_nodes):
            if graph[min_node, neighbor] == 1:
                new_distance = distances[min_node] + 1
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance

    return distances

print_graph(adjacency_matrix)

start_node = 0
end_node = 3
shortest_distances = dijkstra(adjacency_matrix, start_node)
shortest_path_length = shortest_distances[end_node]

print(f"Shortest path length from node {start_node} to {end_node}: {shortest_path_length}")
