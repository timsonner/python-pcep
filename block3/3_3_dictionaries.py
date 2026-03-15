"""
Task: Build a dictionary, iterate through keys/values, and use keys(), items(), values().
"""

student = {"name": "Alice", "age": 22, "course": "PCEP"}

print(f"Keys: {list(student.keys())}")
print(f"Values: {list(student.values())}")
print(f"Items: {list(student.items())}")

print("Iterating through dictionary:")
for key, value in student.items():
    print(f"{key}: {value}")
