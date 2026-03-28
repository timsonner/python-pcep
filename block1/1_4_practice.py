# Task: Demonstrate numeric (** // %), bitwise (~ & ^ | << >>), and relational (== != > <) operators.

"""
program to demonstrate the use of numeric, bitwise, and relational operators in Python.

example output:
Integer: 20, Float: 1337000.000, Binary: 00010100, Octal: 024, Hexadecimal: 00000014
Integer: 65, Float: 1337000.000, Binary: 01000001, Octal: 0101, Hexadecimal: 00000041
NOT: ~
00010100
11101011
01000001
10111110
AND: &
00010100
01000001
00000000
XOR: ^
00010100
01000001
01000001
OR: |
00010100
01000001
01010101
Shift right offset: 2
00010100
00000101
01000001
00010000
Shift left offset: 2
00010100
01010000
01000001
00000100
20 == 65
False
20 != 65
True
20 < 65
True
20 > 65
False
20 ** 65
36893488147419103232
20 // 65
0
20 % 65
20
"""

num_1 = 20
num_2 = 65

def print_nums():
    print(f"{num_1:08b}\n{num_2:08b}")
print_nums()

def print_shift(direction, offset):
    if direction == ">>":
        print(f"{num_1:08b}\n{num_1 >> offset:08b}")
        print(f"{num_2:08b}\n{num_2 >> offset:08b}")
    elif direction == "<<":
        print(f"{num_1:08b}\n{num_1 << offset:08b}")
        print(f"{num_2:08b}\n{num_2 << offset:08b}")
    else:
        print("Invalid argument passed to print_shift()")

def print_mafs(symbol):
    if symbol == "==":
        print(f"{num_1} == {num_2}\n {num_1 == num_2}")
    elif symbol == "!=":
        print(f"{num_1} != {num_2}\n {num_1 != num_2}")
    elif symbol == "<":
        print(f"{num_1} < {num_2}\n {num_1 < num_2}")
    elif symbol == ">":
        print(f"{num_1} > {num_2}\n {num_1 > num_2}")
    elif symbol == "**":
        print(f"{num_1} ** {num_2}\n {num_1 ** num_2}")
    elif symbol == "//":
        print(f"{num_1} // {num_2}\n {num_1 // num_2}")
    elif symbol == "%":
        print(f"{num_1} % {num_2}\n {num_1 % num_2}")
    else:
        print("Invalid argument passed to print_mafs()")

choice = input("Choose: numeric (** // %), bitwise (~ & ^ | << >>), relational (== != > <) operators.")

if choice == "~":
    print("NOT:", choice)
    print(f"{num_1:08b}\n{~num_1:08b}")
    print(f"{num_2:08b}\n{~num_2:08b}")
elif choice == "&":
    print("AND:", choice)
    print_nums()
    print(f"{(num_1 & num_2):08b}")
elif choice == "^":
    print("XOR:", choice)
    print_nums()
    print(f"{num_1 ^ num_2:08b}")
elif choice == "|":
    print("OR:", choice)
    print_nums()
    print(f"{num_1 | num_2:08b}")
elif choice == ">>":
    offset = int(input("Shift right offset: "))
    print_shift(choice, offset)
elif choice == "<<":
    offset = int(input("Shift left offset: "))
    print_shift(choice, offset)
elif choice == "==":
    print_mafs(choice)
elif choice == "!=":
    print_mafs(choice)
elif choice == "<":
    print_mafs(choice)
elif choice == ">":
    print_mafs(choice)
elif choice == "**":
    print_mafs(choice)
elif choice == "//":
    print_mafs(choice)
elif choice == "%":
    print_mafs(choice)
else:
    print("Invalid argument passed to var choice")
