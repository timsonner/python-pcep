"""
Task: Use if, elif, else with nested conditions.
"""

score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
    if score >= 85:
        print("B+ grade earned.")
    else:
        print("B- grade earned.")
else:
    print("Grade below B")
