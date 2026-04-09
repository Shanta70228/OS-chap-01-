# task2_methods.py
# Name: Shanta Sarker (可欣）
# Student ID: 301202424031221
# Lab 02 – Task 2: String Methods – Clean and Transform Input

raw = "  hello, shanta sarker!  "

print("=" * 45)
print("Task 2 – String Methods")
print("=" * 45)

print(f"Original         : '{raw}'")
print(f"strip()          : '{raw.strip()}'")
print(f"upper()          : '{raw.strip().upper()}'")
print(f"lower()          : '{raw.strip().lower()}'")
print(f"title()          : '{raw.strip().title()}'")
print(f"replace()        : '{raw.strip().replace('shanta', 'Python')}'")
print(f"count('a')       : {raw.count('a')}")
print(f"find('sarker')   : {raw.find('sarker')}")
print(f"startswith('  h'): {raw.startswith('  h')}")
print(f"endswith('!  ')  : {raw.endswith('!  ')}")

# Split and join
words = raw.strip().split(", ")
print(f"\nsplit(', ')      : {words}")
print(f"join with ' | '  : {'|'.join(words)}")

# Practical: clean user input
name_input = "  SHANTA sarker (可欣）  "
clean_name = name_input.strip().title()
print(f"\nCleaned name     : '{clean_name}'")
