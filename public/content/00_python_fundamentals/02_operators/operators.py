"""
Operators - Implementation Guide
=================================
Comprehensive Python implementations covering arithmetic, comparison,
logical, bitwise, and ternary operators with interview-focused examples.
"""

from typing import List


# =============================================================================
# SECTION 1: ARITHMETIC OPERATORS
# =============================================================================

# Basic arithmetic operations
a, b = 10, 3

# Addition - returns int if both are int, float otherwise
add_result = a + b              # 13

# Subtraction
sub_result = a - b              # 7

# Multiplication
mul_result = a * b             # 30

# Division - ALWAYS returns float in Python 3
div_result = a / b             # 3.333... (float)
div_result_exact = 10 / 2      # 2.0 (still float!)

# Floor division - rounds DOWN toward negative infinity
floor_div = a // b             # 3
floor_div_negative = -10 // 3  # -4 (not -3!)

# Modulus - remainder after division
mod_result = a % b             # 1 (10 = 3*3 + 1)
mod_negative = -10 % 3          # 2 (because -10 = (-4) * 3 + 2)

# Exponentiation - right associative
power_result = 2 ** 3          # 8
power_chained = 2 ** 3 ** 2    # 2 ** 9 = 512 (right associative)

# Combined operations
combined = (a + b) * (a - b)   # 13 * 7 = 91

# Practical examples
def is_even(n: int) -> bool:
    """Check if number is even using modulus."""
    return n % 2 == 0

def get_last_digit(n: int) -> int:
    """Get the last digit of a number."""
    return abs(n) % 10

def cycle_index(index: int, total: int) -> int:
    """Cycle index using modulus (useful for circular arrays)."""
    return index % total

def sum_of_digits(n: int) -> int:
    """Calculate sum of digits using modulus."""
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


# =============================================================================
# SECTION 2: COMPARISON OPERATORS - == vs is
# =============================================================================

# == compares VALUE equality
# is compares IDENTITY (same object in memory)

# Integer comparisons
print(10 == 10)               # True - same value
print(10 == 10.0)             # True - int equals float value

# String comparisons
print("hello" == "hello")     # True - same content
print("hello" == "world")     # False

# List comparisons - checks content
list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = list_a

print(list_a == list_b)       # True - same content
print(list_a is list_b)       # False - different objects in memory
print(list_a is list_c)       # True - same object

# CRITICAL: Use 'is' for None comparison
my_var = None

if my_var is None:            # CORRECT - identity check
    print("Variable is None")

# WRONG way (though often works due to Python interning)
# if my_var == None:          # Not recommended

# Integer interning - small integers are cached
small_int_a = 256
small_int_b = 256
print(small_int_a is small_int_b)  # True (cached)

# But not for larger integers!
large_int_a = 1000
large_int_b = 1000
print(large_int_a is large_int_b)  # May be False

# String interning - some strings are interned
str_a = "hello"
str_b = "hello"
print(str_a is str_b)          # True (likely interned)

# Chained comparisons - Python feature
x = 5
result = 1 < x < 10            # True - equivalent to (1 < x) and (x < 10)
result2 = 1 < x < 5           # False - (1 < 5) and (5 < 5) = True and False

# Practical use of chained comparisons
age = 25
is_working_age = 18 <= age <= 65  # True


# =============================================================================
# SECTION 3: LOGICAL OPERATORS
# =============================================================================

# and - returns first falsy value or last value
result = 0 and 1               # 0 (0 is falsy)
result = 1 and 2              # 2 (both truthy, returns last)
result = "hello" and ""       # "" (first falsy)
result = "hello" and "world" # "world" (both truthy)

# or - returns first truthy value or last value
result = 0 or 1               # 1 (0 is falsy)
result = 1 or 2               # 1 (first truthy, short-circuits)
result = "" or "default"      # "default"
result = 0 or "" or "fallback"  # "fallback"

# not - returns boolean
result = not True             # False
result = not False            # True
result = not 0                # True (0 is falsy)
result = not 1                # False (1 is truthy)

# Short-circuit evaluation for default values
def get_user_name(user_dict):
    """Safely get username with default."""
    return user_dict.get("name") or "Anonymous"

# Practical: validate before using
def divide_safe(a, b):
    """Divide with short-circuit evaluation."""
    if b == 0:
        return None
    return a / b

# Another practical use: conditional function calls
condition = True
result = condition and expensive_function()  # Only calls if True

# Logical operator precedence: not < and < or
result = not True or False        # (not True) or False = False or False = False
result = not (True or False)     # not True = False
result = True and False or True  # (True and False) or True = False or True = True


# =============================================================================
# SECTION 4: BITWISE OPERATORS
# =============================================================================

# Binary representations:
# 5 = 0b101
# 3 = 0b011

# Bitwise AND - 1 only if both bits are 1
and_result = 5 & 3             # 1 (0b001)

# Bitwise OR - 1 if either bit is 1
or_result = 5 | 3             # 7 (0b111)

# Bitwise XOR - 1 if bits are different
xor_result = 5 ^ 3             # 6 (0b110)

# Bitwise NOT - invert all bits + 1 (two's complement)
not_result = ~5                # -6

# Left shift - multiply by 2^n
left_shift = 5 << 1            # 10 (0b1010 = 5 * 2)
left_shift2 = 5 << 2          # 20 (0b10100 = 5 * 4)

# Right shift - divide by 2^n (floor)
right_shift = 5 >> 1          # 2 (0b10 = 5 // 2)
right_shift2 = 5 >> 2         # 1 (0b1 = 5 // 4)


# =============================================================================
# SECTION 5: PRACTICAL BITWISE TRICKS
# =============================================================================

def is_even_bitwise(n: int) -> bool:
    """Check if number is even using bitwise AND."""
    return (n & 1) == 0


def is_power_of_2(n: int) -> bool:
    """
    Check if n is a power of 2.
    Key insight: n & (n-1) clears the lowest set bit.
    For powers of 2, this results in 0.
    """
    return n > 0 and (n & (n - 1)) == 0


def get_bit(num: int, pos: int) -> int:
    """Get the bit at position pos (0-indexed from right)."""
    return (num >> pos) & 1


def set_bit(num: int, pos: int) -> int:
    """Set the bit at position pos to 1."""
    return num | (1 << pos)


def clear_bit(num: int, pos: int) -> int:
    """Clear the bit at position pos to 0."""
    return num & ~(1 << pos)


def toggle_bit(num: int, pos: int) -> int:
    """Toggle the bit at position pos."""
    return num ^ (1 << pos)


def count_set_bits(n: int) -> int:
    """
    Count number of 1s in binary representation.
    Uses Brian Kernighan's algorithm.
    """
    count = 0
    while n:
        n &= (n - 1)  # Clear lowest set bit
        count += 1
    return count


def reverse_bits(n: int, bits: int = 32) -> int:
    """Reverse bits of a number."""
    result = 0
    for i in range(bits):
        if (n >> i) & 1:
            result |= (1 << (bits - 1 - i))
    return result


def swap_bits(a: int, i: int, j: int) -> int:
    """Swap bits at positions i and j."""
    if ((a >> i) & 1) != ((a >> j) & 1):
        mask = (1 << i) | (1 << j)
        a ^= mask
    return a


# =============================================================================
# SECTION 6: TERNARY/CONDITIONAL OPERATOR
# =============================================================================

# Basic ternary syntax: value_if_true if condition else value_if_false

age = 20

# Simple conditional assignment
status = "adult" if age >= 18 else "minor"

# In assignment expressions
a, b = 10, 20
max_val = a if a > b else b
min_val = a if a < b else b

# With None checks
name = user_input or "Anonymous"

# Chained ternary (use sparingly - can be hard to read)
x = 10
result = "a" if x > 10 else "b" if x > 5 else "c"
# Equivalent to:
# if x > 10: "a"
# elif x > 5: "b"
# else: "c"

# Practical example: categorize number
def categorize(n: int) -> str:
    """Categorize number as negative, zero, or positive."""
    return "negative" if n < 0 else "zero" if n == 0 else "positive"


# =============================================================================
# SECTION 7: OPERATOR PRECEDENCE
# =============================================================================

# Highest to lowest precedence:
# 1. ** (exponentiation)
# 2. -x (unary negation)
# 3. * / // % (multiplicative)
# 4. + - (additive)
# 5. << >> (bit shifts)
# 6. & (bitwise AND)
# 7. ^ (bitwise XOR)
# 8. | (bitwise OR)
# 9. == != < > <= >= is is not in not in (comparisons)
# 10. not (logical NOT)
# 11. and (logical AND)
# 12. or (logical OR)

# Examples showing precedence
result1 = 2 + 3 * 4           # 14, not 20 (multiplication before addition)
result2 = (2 + 3) * 4         # 20 (parentheses override)

result3 = 2 ** 3 ** 2         # 512 (right associative: 2 ** 9)
result4 = (2 ** 3) ** 2       # 64 (left associative)

result5 = not True or False  # False (not has higher precedence than or)
result6 = not (True or False) # False

result7 = 2 + 3 < 4 + 5       # True (comparisons after additions)


# =============================================================================
# SECTION 8: SPECIAL OPERATORS - IN AND NOT IN
# =============================================================================

# Membership operators - for sequences

# in - checks if value is in sequence
fruits = ["apple", "banana", "cherry"]
result = "apple" in fruits           # True
result = "orange" in fruits         # False

# in with strings
text = "hello world"
result = "hello" in text            # True
result = "world" in text            # True

# not in - opposite of in
result = "orange" not in fruits     # True

# Practical use in conditional
def find_element(arr: List[int], target: int) -> str:
    """Find if target exists in array."""
    if target in arr:
        return f"Found {target}"
    return f"{target} not found"


# =============================================================================
# SECTION 9: IDENTITY OPERATORS - IS AND IS NOT
# =============================================================================

# is - checks if two variables point to same object
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)              # True - same object
print(a is c)              # False - different objects (same content)
print(a is not c)          # True

# Use cases for is:
# 1. Comparing with None
if my_var is None:
    print("No value")

# 2. Checking singleton objects
if result is True:         # Compare with True
    print("Success")
if result is False:
    print("Failure")

# 3. Checking object identity
def check_singleton():
    """Check if we're using the same object."""
    pass


# =============================================================================
# SECTION 10: COMBINED PRACTICAL EXAMPLES
# =============================================================================

def solve_interview_problem(arr: List[int], target: int) -> dict:
    """
    Solve a common interview problem showing multiple operators.
    Find pairs that sum to target and return their indices.
    """
    seen = {}  # value -> index

    for i, num in enumerate(arr):
        complement = target - num

        # Use 'in' for membership check
        if complement in seen:
            return {
                "found": True,
                "indices": (seen[complement], i),
                "values": (complement, num)
            }

        # Use 'or' for default
        seen[num] = i

    return {"found": False}


def bit_manipulation_example(n: int) -> dict:
    """Demonstrate bit manipulation concepts."""
    return {
        "original": n,
        "is_even": (n & 1) == 0,
        "is_power_of_2": n > 0 and (n & (n - 1)) == 0,
        "bit_count": bin(n).count("1"),
        "left_shift_1": n << 1,
        "right_shift_1": n >> 1,
    }


# =============================================================================
# SECTION 11: DEMONSTRATION
# =============================================================================

if __name__ == "__main__":
    # Demonstrate arithmetic
    print("=== Arithmetic ===")
    print(f"10 / 3 = {10 / 3}")      # 3.333...
    print(f"10 // 3 = {10 // 3}")    # 3
    print(f"-10 // 3 = {-10 // 3}")  # -4

    # Demonstrate comparison
    print("\n=== Comparison ===")
    print(f"[1,2,3] == [1,2,3]: {[1,2,3] == [1,2,3]}")
    print(f"[1,2,3] is [1,2,3]: {[1,2,3] is [1,2,3]}")

    # Demonstrate logical
    print("\n=== Logical ===")
    print(f"0 and 1 = {0 and 1}")
    print(f"1 or 2 = {1 or 2}")
    print(f"not True = {not True}")

    # Demonstrate bitwise
    print("\n=== Bitwise ===")
    print(f"5 & 3 = {5 & 3}")  # 1
    print(f"5 | 3 = {5 | 3}")  # 7
    print(f"5 ^ 3 = {5 ^ 3}")  # 6

    # Demonstrate ternary
    print("\n=== Ternary ===")
    print(f"'adult' if 20 >= 18 else 'minor': {'adult' if 20 >= 18 else 'minor'}")
