# task1_strings.py
# Name: Shanta Sarker (可欣）
# Student ID: 301202424031221
# Lab 02 – Task 1: String Basics – Inspect and Slice Text

text = "Software Engineering"

print("=" * 45)
print("Task 1 – String Basics")
print("=" * 45)

# Length
print(f"String       : '{text}'")
print(f"Length       : {len(text)}")

# Indexing
print(f"First char   : {text[0]}")
print(f"Last char    : {text[-1]}")
print(f"Index 9      : {text[9]}")

# Slicing
print(f"First 8 chars: {text[:8]}")
print(f"Last 11 chars: {text[9:]}")
print(f"Slice [0:8]  : {text[0:8]}")
print(f"Every 2nd    : {text[::2]}")
print(f"Reversed     : {text[::-1]}")

# Concatenation & repetition
greeting = "Hello, " + "Shanta!"
print(f"\nConcatenation: {greeting}")
print(f"Repetition   : {'Hi! ' * 3}")

# Membership
print(f"\n'Engineer' in text : {'Engineer' in text}")
print(f"'Math' in text     : {'Math' in text}")
