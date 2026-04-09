# task3_conditionals.py
# Name: Shanta Sarker (可欣）
# Student ID: 301202424031221
# Lab 02 – Task 3: Conditional Practice – Simple Text Decisions

print("=" * 45)
print("Task 3 – Conditional Statements")
print("=" * 45)

# --- 1. Grade checker ---
score = int(input("Enter your score (0-100): "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}  →  Grade: {grade}")

# --- 2. String length decision ---
word = input("\nEnter a word: ").strip()

if len(word) == 0:
    print("You entered nothing.")
elif len(word) <= 3:
    print(f"'{word}' is a short word.")
elif len(word) <= 7:
    print(f"'{word}' is a medium word.")
else:
    print(f"'{word}' is a long word.")

# --- 3. Vowel or consonant check ---
letter = input("\nEnter a single letter: ").strip().lower()

if len(letter) != 1 or not letter.isalpha():
    print("Please enter a single letter.")
elif letter in "aeiou":
    print(f"'{letter}' is a vowel.")
else:
    print(f"'{letter}' is a consonant.")
