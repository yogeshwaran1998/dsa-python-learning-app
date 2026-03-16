# Operators - Theory Guide

## Table of Contents
1. [Arithmetic Operators](#arithmetic-operators)
2. [Comparison Operators](#comparison-operators)
3. [Logical Operators](#logical-operators)
4. [Bitwise Operators](#bitwise-operators)
5. [Ternary/Conditional Operator](#ternaryconditional-operator)
6. [Operator Precedence](#operator-precedence)
7. [Interview Tips](#interview-tips)

---

## Arithmetic Operators

### Basic Operations

| Operator | Description | Example |
|----------|-------------|---------|
| + | Addition | 10 + 5 = 15 |
| - | Subtraction | 10 - 5 = 5 |
| * | Multiplication | 10 * 5 = 50 |
| / | Division (float) | 10 / 5 = 2.0 |
| // | Floor Division | 10 // 5 = 2, 10 // 3 = 3 |
| % | Modulus (remainder) | 10 % 3 = 1 |
| ** | Exponentiation | 2 ** 3 = 8 |

### Key Differences: / vs //

- **/** (Division): Always returns float, even for exact division
- **//** (Floor Division): Returns integer, rounds down toward negative infinity

```python
# Positive numbers - both work similarly
10 / 3        # 3.333... (float)
10 // 3       # 3 (floor, integer)

# Negative numbers - DIFFERENT results!
-10 / 3       # -3.333... (float)
-10 // 3      # -4 (floors DOWN toward negative infinity)
10 // -3      # -4
-10 // -3     # 3
```

### Modulus (%) Behavior

The modulus always has the same sign as the divisor:

```python
10 % 3        # 1
-10 % 3       # 2 (because -10 = (-4) * 3 + 2)
10 % -3       # -2
-10 % -3      # -1
```

### Practical Uses

```python
# Check if even/odd
number = 7
is_even = (number % 2 == 0)       # False
is_odd = (number % 2 != 0)        # True

# Get last digit
last_digit = 12345 % 10           # 5

# Cycle through values
index = 7 % 3                     # 1 (cycles 0, 1, 2, 0, 1, 2...)

# Check divisibility
is_divisible = (20 % 5 == 0)      # True
```

---

## Comparison Operators

### Value vs Identity

| Operator | Meaning | Checks |
|----------|---------|--------|
| == | Equal to | Value equality |
| != | Not equal to | Value inequality |
| is | Identity | Same object in memory |
| is not | Not identity | Different objects in memory |

### When to Use == vs is

**Use == (equality) for:**
- Comparing values
- Comparing numbers, strings, lists (by content)

**Use is (identity) for:**
- Comparing with None, True, False (singletons)
- Checking if two variables point to the same object
- Comparing with literals when you need identity

```python
# == compares VALUES
[1, 2, 3] == [1, 2, 3]    # True - same values
"hello" == "hello"        # True - same values
10 == 10                  # True

# is compares IDENTITY (same object in memory)
# For small integers and strings, Python may intern them
a = "hello"
b = "hello"
a is b                    # True (may be interned)

# But this is NOT reliable for larger strings!
a = "hello world"
b = "hello world"
a is b                    # False - different objects

# CRITICAL: Always use 'is' for None comparison
if my_var is None:        # CORRECT
if my_var == None:        # WRONG (but works due to Python quirks)

# Lists - == checks content, is checks identity
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

list1 == list2            # True - same content
list1 is list2            # False - different objects
list1 is list3            # True - same object
```

### Chained Comparisons

Python allows chaining comparisons:

```python
# a < b < c is equivalent to (a < b) and (b < c)
x = 5
result1 < x < 10       # =  True (1 < 5 < 10)
result = 1 < x < 5        # False (1 < 5 but 5 is not < 5)

# Practical use
age = 25
is_adult = 18 <= age <= 65  # True
```

---

## Logical Operators

### and, or, not

| Operator | Description | Truth Table |
|----------|-------------|--------------|
| and | Both True | True and True = True |
| or | At least one True | False or True = True |
| not | Invert truth | not True = False |

### Short-Circuit Evaluation

Python evaluates only as much as needed:

```python
# and - returns first falsy value or last value
result = 0 and 1          # 0 (0 is falsy, short-circuits)
result = 1 and 2          # 2 (both truthy, returns last)
result = "hello" and ""    # "" (first falsy)

# or - returns first truthy value or last value
result = 0 or 1           # 1 (0 is falsy, 1 is truthy)
result = 1 or 2           # 1 (first truthy, short-circuits)
result = "" or "default"  # "default"

# Common pattern: default values
name = user_input or "Anonymous"
```

### Practical Examples

```python
# Validate multiple conditions
age = 25
income = 50000

if age >= 18 and income > 0:
    print("Eligible")

# Either/or conditions
is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
    print("No work today!")

# not for negation
if not is_empty:
    print("Has data")
```

### Operator Precedence (High to Low)

1. **not** (lowest in this group)
2. **and**
3. **or** (highest in this group)

```python
# not has lowest precedence among logical operators
not True or True          # (not True) or True = False or True = True
not (True or True)        # not True = False

# and has higher precedence than or
True or True and False    # True or (True and False) = True or False = True
(True or True) and False  # True and False = False
```

---

## Bitwise Operators

### What Are They?
Operations on individual bits of integers.

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| & | AND | 5 & 3 | 1 |
| \| | OR | 5 \| 3 | 7 |
| ^ | XOR | 5 ^ 3 | 6 |
| ~ | NOT | ~5 | -6 |
| << | Left Shift | 5 << 1 | 10 |
| >> | Right Shift | 5 >> 1 | 2 |

### Binary Representations

```python
# 5 in binary: 101
# 3 in binary: 011

5 & 3   # 001 = 1  (AND: both 1)
5 | 3   # 111 = 7  (OR: either 1)
5 ^ 3   # 110 = 6  (XOR: different)
~5      # -6       (NOT: invert + 1)

# Left shift: multiply by 2^n
5 << 1   # 1010 = 10  (5 * 2)
5 << 2   # 10100 = 20 (5 * 4)

# Right shift: divide by 2^n (floor)
5 >> 1   # 10 = 2 (5 // 2)
5 >> 2   # 1 (5 // 4)
```

### Practical Interview Uses

```python
# Check if number is even
is_even = (n & 1) == 0

# Check if number is power of 2
def is_power_of_2(n):
    return n > 0 and (n & (n - 1)) == 0

# Get nth bit
def get_bit(num, n):
    return (num >> n) & 1

# Set nth bit
def set_bit(num, n):
    return num | (1 << n)

# Clear nth bit
def clear_bit(num, n):
    return num & ~(1 << n)

# Toggle nth bit
def toggle_bit(num, n):
    return num ^ (1 << n)

# Count set bits (Brian Kernighan's algorithm)
def count_bits(n):
    count = 0
    while n:
        n &= (n - 1)
        count += 1
    return count
```

---

## Ternary/Conditional Operator

### Syntax
```python
value_if_true if condition else value_if_false
```

### Examples

```python
# Basic usage
age = 20
status = "adult" if age >= 18 else "minor"

# In assignments
max_val = a if a > b else b
min_val = a if a < b else b

# With None checks
name = user_name if user_name else "Anonymous"

# Chained ternary (avoid - can be hard to read)
result = "a" if x > 10 else "b" if x > 5 else "c"
```

### When to Use Ternary

Good for:
- Simple conditional assignments
- Inline conditionals

Avoid when:
- Complex logic (use if-else)
- Multiple conditions (use if-elif-else)

---

## Operator Precedence

### Full Precedence Table (High to Low)

1. ** (exponentiation)
2. -x (unary negation)
3. * / // % (multiplication/division)
4. + - (addition/subtraction)
5. << >> (bit shifts)
6. & (bitwise AND)
7. ^ (bitwise XOR)
8. | (bitwise OR)
9. == != < > <= >= is is not in not in (comparisons)
10. not (logical NOT)
11. and (logical AND)
12. or (logical OR)

### Examples

```python
# Multiplication before addition
2 + 3 * 4              # 14, not 20

# Use parentheses to be explicit
(2 + 3) * 4            # 20

# Exponentiation is right-associative
2 ** 3 ** 2            # 2 ** 9 = 512, not 4 ** 2 = 16
```

---

## Interview Tips

### Common Pitfalls

1. **Floor division with negatives**
   - Remember: -10 // 3 = -4 (not -3)

2. **Using == with mutable objects**
   - Use is for None, == for values

3. **Bitwise vs Logical operators**
   - & is bitwise AND
   - and is logical AND

4. **Operator precedence**
   - When in doubt, use parentheses

### Time Complexity
- All arithmetic operations: O(1) for basic types
- All comparisons: O(1)
- Bitwise operations: O(1)

### Key Takeaways
- Use // for integer division when you need integer result
- Use is for None comparisons (not ==)
- Bitwise operations are powerful for bit manipulation
- Short-circuit evaluation can be used for elegant defaults
- Always use parentheses for clarity
