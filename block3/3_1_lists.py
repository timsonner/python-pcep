"""
Task: Perform indexing, slicing, append(), insert(), and list comprehension. Create a multi-dimensional list.
"""

my_list = [10, 20, 30, 40, 50]
print(f"Indexing: {my_list[0]}, Slicing: {my_list[1:3]}")

my_list.append(60)
my_list.insert(0, 5)
print(f"Updated list: {my_list}")

# List comprehension
squares = [x**2 for x in range(5)]
print(f"Squares: {squares}")

# Multi-dimensional list
matrix = [[1, 2], [3, 4]]
print(f"Matrix value at [1][0]: {matrix[1][0]}")
