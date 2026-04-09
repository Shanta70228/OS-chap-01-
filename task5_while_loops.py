# task5_while_loops.py
# Name: Shanta Sarker (可欣）
# Student ID: 301202424031221
# Lab 02 – Task 5: While Loop Practice – Repeated Input Check

print("=" * 45)
print("Task 5 – While Loops")
print("=" * 45)

# --- 1. Keep asking until valid input ---
print("\nPart 1: Enter a non-empty word (keeps asking if blank).")
word = ""
while word == "":
    word = input("Enter a word: ").strip()
    if word == "":
        print("  Empty input – please try again.")
print(f"You entered: '{word}'")

# --- 2. Password-style check (max 3 tries) ---
print("\nPart 2: Secret word game (3 attempts).")
secret = "python"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    guess = input(f"  Guess the secret word (attempt {attempts + 1}/{max_attempts}): ").strip().lower()
    attempts += 1
    if guess == secret:
        print(f"  Correct! You got it in {attempts} attempt(s).")
        break
    else:
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"  Wrong. {remaining} attempt(s) left.")
else:
    print(f"  Out of attempts. The secret word was '{secret}'.")

# --- 3. Countdown while loop ---
print("\nPart 3: Countdown.")
count = 5
while count > 0:
    print(f"  {count}...")
    count -= 1
print("  Go!")
