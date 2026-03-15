"""
Task: Demonstrate tuple immutability and indexing. Nest a tuple inside a list.
"""

my_tuple = (1, 2, 3)
print(f"Tuple indexing: {my_tuple[1]}")

# Tuple immutability demonstration
try:
    my_tuple[0] = 100
except TypeError as e:
    print(f"Caught error (tuples are immutable): {e}")

# Nested tuple in a list
data = [10, (20, 30), 40]
print(f"Nested tuple: {data[1]}")
