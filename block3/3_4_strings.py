"""
Task: Demonstrate string indexing, slicing, escaping characters (\), and multi-line strings.
"""

text = "Hello, Python!"
print(f"Indexing: {text[7]}, Slicing: {text[0:5]}")

# Escaping characters
escaped = "This is a line break\nAnd a tab\t!"
print(escaped)

# Multi-line string
multi_line = """
This is a 
multi-line string.
Useful for documentation.
"""
print(multi_line)
