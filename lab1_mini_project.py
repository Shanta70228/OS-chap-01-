# lab1_mini_project.py
# Name: Shanta Sarker (可欣）
# Student ID: 301202424031221
# Major: Software Engineering
# Lab 1 Mini-Project: Personal Info & Simple Calculator

import math
import random

# ─────────────────────────────────────────
# PART A: Environment Check
# (Run this script; output proves Python works)
# ─────────────────────────────────────────
import sys
print("=" * 50)
print("PART A – Environment Check")
print("=" * 50)
print(f"Python version: {sys.version}")
print(f"math module available: True  (e.g. math.pi = {math.pi:.5f})")
print(f"random module available: True (e.g. random.randint(1,10) = {random.randint(1, 10)})")

# ─────────────────────────────────────────
# PART B: Types & Expressions
# ─────────────────────────────────────────
print("\n" + "=" * 50)
print("PART B – Types & Expressions")
print("=" * 50)

# int
x = 42
print(f"x = {x}  |  type: {type(x)}")          # <class 'int'>

# float
gpa = 3.85
print(f"gpa = {gpa}  |  type: {type(gpa)}")      # <class 'float'>

# bool
is_student = True
print(f"is_student = {is_student}  |  type: {type(is_student)}")  # <class 'bool'>

# str
name = "Shanta Sarker"
print(f"name = '{name}'  |  type: {type(name)}")  # <class 'str'>

# Expressions
print("\n--- Expressions ---")
print(f"7 + 3   = {7 + 3}")          # 10
print(f"7 - 3   = {7 - 3}")          # 4
print(f"7 * 3   = {7 * 3}")          # 21
print(f"7 / 3   = {7 / 3:.4f}")      # 2.3333  (float division)
print(f"7 // 3  = {7 // 3}")         # 2       (floor division)
print(f"7 % 3   = {7 % 3}")          # 1       (modulus)
print(f"2 ** 8  = {2 ** 8}")         # 256     (exponent)

# Operator precedence example
result = 2 + 3 * 4 - (10 / 2)
print(f"\n2 + 3 * 4 - (10 / 2) = {result}")   # 9.0

# ─────────────────────────────────────────
# PART C: Tracing Variables
# ─────────────────────────────────────────
print("\n" + "=" * 50)
print("PART C – Variable Tracing (right-to-left evaluation)")
print("=" * 50)

a = 10
b = 20
print(f"Initial:  a = {a},  b = {b}")

# Swap without temp variable
a, b = b, a
print(f"After swap (a, b = b, a):  a = {a},  b = {b}")

# Chain assignment
c = d = 100
print(f"c = d = 100  →  c = {c},  d = {d}")

# Augmented assignment
total = 0
for i in range(1, 6):        # 1 + 2 + 3 + 4 + 5
    total += i
print(f"Sum 1→5 using += :  total = {total}")

# ─────────────────────────────────────────
# PART D: Modules & Function Calls
# ─────────────────────────────────────────
print("\n" + "=" * 50)
print("PART D – Modules & Function Calls")
print("=" * 50)

angle_deg = 45
angle_rad = math.radians(angle_deg)
print(f"math.radians({angle_deg}) = {angle_rad:.5f}")
print(f"math.sin({angle_deg}°)    = {math.sin(angle_rad):.5f}")
print(f"math.cos({angle_deg}°)    = {math.cos(angle_rad):.5f}")
print(f"math.sqrt(144)            = {math.sqrt(144)}")
print(f"math.floor(3.9)           = {math.floor(3.9)}")
print(f"math.ceil(3.1)            = {math.ceil(3.1)}")
print(f"math.log(math.e)          = {math.log(math.e)}")

print(f"\nrandom.random()           = {random.random():.5f}   (0.0–1.0)")
print(f"random.randint(1, 100)    = {random.randint(1, 100)}")

# ─────────────────────────────────────────
# PART E: Mini-Project – Personal Info + Calculator
# ─────────────────────────────────────────
print("\n" + "=" * 50)
print("PART E – Mini-Project: Personal Info & Calculator")
print("=" * 50)

# --- Personal info (hard-coded for demo; would use input() interactively) ---
student_name  = "Shanta Sarker (可欣）"
student_id    = "301202424031221"
major         = "Software Engineering"
year          = 1                       # int
gpa           = 3.85                    # float
on_campus     = True                    # bool

print("\n── Student Profile ──")
print(f"  Name      : {student_name}")
print(f"  ID        : {student_id}")
print(f"  Major     : {major}")
print(f"  Year      : {year}  ({type(year).__name__})")
print(f"  GPA       : {gpa}  ({type(gpa).__name__})")
print(f"  On campus : {on_campus}  ({type(on_campus).__name__})")

# --- Simple Calculator (uses input() with type conversion) ---
print("\n── Simple Calculator ──")
print("Enter two numbers to perform basic operations.")

try:
    num1 = float(input("  Enter first number  : "))
    num2 = float(input("  Enter second number : "))

    print(f"\n  {num1} + {num2}  = {num1 + num2}")
    print(f"  {num1} - {num2}  = {num1 - num2}")
    print(f"  {num1} * {num2}  = {num1 * num2}")

    if num2 != 0:
        print(f"  {num1} / {num2}  = {num1 / num2:.4f}")
        print(f"  {num1} // {num2} = {num1 // num2}")
        print(f"  {num1} % {num2}  = {num1 % num2}")
    else:
        print("  Division by zero is undefined – skipping /, //, %")

    # Bonus: use math module
    if num1 >= 0:
        print(f"\n  math.sqrt({num1})   = {math.sqrt(num1):.4f}")

    print(f"  math.pow({num1}, 2) = {math.pow(num1, 2)}")

except ValueError:
    print("  [!] Please enter valid numeric values.")

print("\n" + "=" * 50)
print("Lab 1 complete – Shanta Sarker | ID: 301202424031221")
print("=" * 50)
