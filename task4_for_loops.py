# task4_for_loops.py
# Name: Shanta Sarker (可欣）
# Student ID: 301202424031221
# Lab 02 – Task 4: For Loop Practice – Count Letters and Characters

print("=" * 45)
print("Task 4 – For Loops")
print("=" * 45)

text = "Shanta Sarker Software Engineering"
print(f"Text: '{text}'\n")

# --- 1. Print each character ---
print("Characters in text:")
for ch in text:
    print(ch, end=" ")
print()

# --- 2. Count vowels and consonants ---
vowels = 0
consonants = 0
spaces = 0

for ch in text.lower():
    if ch == " ":
        spaces += 1
    elif ch in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1

print(f"\nVowels    : {vowels}")
print(f"Consonants: {consonants}")
print(f"Spaces    : {spaces}")

# --- 3. Find and print positions of a letter ---
target = "a"
print(f"\nPositions of '{target}' in text:")
for i, ch in enumerate(text):
    if ch.lower() == target:
        print(f"  index {i} → '{ch}'")

# --- 4. Build a new string (only uppercase letters) ---
upper_only = ""
for ch in text:
    if ch.isupper():
        upper_only += ch
print(f"\nUppercase letters only: '{upper_only}'")
