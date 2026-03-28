# Task: Demonstrate numeric (** // %), bitwise (~ & ^ | << >>), and relational (== != > <) operators.

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
