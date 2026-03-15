"""
Task: Use while, for, range(), break, continue, and the loop-else clause.
"""

# For loop with range
print("For loop with range:")
for i in range(1, 10):
    if i == 5:
        continue  # skip 5
    if i == 8:
        break     # end at 8
    print(i, end=" ")
print()

# While loop with else clause
counter = 0
while counter < 3:
    print(f"Counter: {counter}")
    counter += 1
else:
    print("Loop finished without a break.")
