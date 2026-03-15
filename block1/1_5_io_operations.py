"""
Task: Use print() with sep= and end= parameters. Get user input and cast to int/float.
"""

# Using sep and end in print
print("Python", "PCEP", "Certification", sep="-", end="!!!\n")

# Getting and casting input
user_age_str = input("Enter your age (integer): ")
user_age = int(user_age_str)

user_gpa_str = input("Enter your GPA (float): ")
user_gpa = float(user_gpa_str)

print(f"Age: {user_age}, GPA: {user_gpa}")
