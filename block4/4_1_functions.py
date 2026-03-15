"""
Task: Define a function with return and explore recursion.
"""

def add(a, b):
    return a + b

print(f"Result of add(5, 3): {add(5, 3)}")

# Recursion: Factorial
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(f"Factorial of 5: {factorial(5)}")
