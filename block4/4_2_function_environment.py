"""
Task: Use positional vs keyword arguments, default parameters, and the global keyword.
"""

count = 0

def greet(name, message="Hello", greeting_type="Standard"):
    global count
    count += 1
    print(f"{greeting_type}: {message}, {name}!")

# Positional arguments
greet("Bob", "Good morning")

# Keyword arguments
greet(name="Alice", greeting_type="VIP", message="Welcome")

# Default parameter
greet("Charlie")

print(f"Greet function called {count} times.")
