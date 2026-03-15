"""
Task: Demonstrate numeric (** // %), bitwise (~ & ^ | << >>), and relational (== != > <) operators.
"""

# Numeric operators
print(f"Exponent: 2 ** 3 = {2 ** 3}")
print(f"Floor Division: 10 // 3 = {10 // 3}")
print(f"Modulo: 10 % 3 = {10 % 3}")

# Bitwise operators
a = 5  # 0101
b = 3  # 0011
print(f"AND: {a & b}, OR: {a | b}, XOR: {a ^ b}, NOT: {~a}")
print(f"Left shift: {a << 1}, Right shift: {a >> 1}")

# Relational operators
print(f"Equal: 5 == 5 is {5 == 5}")
print(f"Not Equal: 5 != 3 is {5 != 3}")
print(f"Greater: 10 > 2 is {10 > 2}")
print(f"Less: 1 < 4 is {1 < 4}")
