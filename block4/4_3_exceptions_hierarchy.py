"""
Task: Write code that triggers IndexError, KeyError, and ValueError.
"""

# IndexError
try:
    my_list = [1, 2]
    print(my_list[5])
except IndexError as e:
    print(f"Caught: {e}")

# KeyError
try:
    my_dict = {"a": 1}
    print(my_dict["b"])
except KeyError as e:
    print(f"Caught: KeyError: {e}")

# ValueError
try:
    int("abc")
except ValueError as e:
    print(f"Caught: {e}")
