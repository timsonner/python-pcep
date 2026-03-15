"""
Task: Use try-except-else-finally blocks with specific exception types.
"""

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except TypeError:
        print("Error: Please provide numbers!")
    else:
        print(f"Result is {result}")
    finally:
        print("Division attempt complete.")

divide(10, 2)
divide(10, 0)
divide(10, "2")
