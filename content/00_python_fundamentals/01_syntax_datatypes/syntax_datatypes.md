# Variables, Primitive Types, and Strings - Theory Guide

## Table of Contents
1. [Variables](#variables)
2. [Primitive Types](#primitive-types)
3. [Type Conversion](#type-conversion)
4. [None Type](#none-type)
5. [String Operations](#string-operations)
6. [Interview Tips](#interview-tips)

---

## Variables

### What is a Variable?
A variable is a named storage location in memory that holds a value. In Python, variables are created when you assign a value and do not need explicit declaration.

### Key Concepts
- **Dynamic Typing**: Python determines variable type at runtime
- **No Type Declaration**: Just assign a value to create a variable
- **Case Sensitive**: `myVar` and `myvar` are different variables
- **Meaningful Names**: Use descriptive names (e.g., `max_value` not `m`)

### Variable Naming Rules
- Must start with a letter or underscore
- Can contain letters, numbers, and underscores
- Cannot be a Python keyword
- Snake case is convention: `max_value`, `user_name`

### Memory Model
```python
x = 10          # Creates integer object, binds x to it
y = x           # Creates another reference to the same object
y = 20          # Creates new integer object, y now points to it
                # x still points to 10
```

---

## Primitive Types

### 1. Integer (int)
Whole numbers, no limit on size (arbitrary precision).

```python
age = 25
count = -100
population = 7_000_000_000  # Underscores for readability
```

### 2. Float (float)
Decimal numbers, represented as double-precision.

```python
price = 19.99
temperature = -273.15
scientific = 1.5e10  # 1.5 * 10^10
```

### 3. Boolean (bool)
True or False values.

```python
is_active = True
has_permission = False
```

### 4. String (str)
Sequence of Unicode characters.

```python
name = "Alice"
message = 'Hello, World!'
multiline = """This is a
multi-line string"""
```

### Type Checking
```python
x = 10
print(type(x))       # <class 'int'>
print(isinstance(x, int))  # True
```

---

## Type Conversion

### Explicit Conversion (Casting)
Convert between types explicitly using constructor functions.

```python
# String to Integer
num = int("42")           # 42
num = int("1010", 2)      # Binary 1010 = 10

# Integer to String
s = str(42)               # "42"

# Integer to Float
f = float(42)             # 42.0

# Float to Integer (truncates)
i = int(3.7)              # 3 (not rounded!)

# String to Float
f = float("3.14")         # 3.14

# To Boolean
bool(1)          # True
bool(0)          # False
bool("")         # False (empty string)
bool("hello")    # True
bool([])         # False (empty list)
```

### Implicit Conversion
Python automatically converts in mixed expressions.

```python
# Integer + Float = Float
result = 10 + 3.14        # 13.14 (int promoted to float)

# Boolean + Integer = Integer
result = True + 5         # 6 (True = 1)
result = False + 5        # 5 (False = 0)
```

---

## None Type

### What is None?
`None` represents the absence of a value or null value. It's a singleton object (only one instance exists).

```python
# Assigning None
result = None
data = None

# Checking for None
if result is None:
    print("No result")

# Common patterns
def find_item(items, target):
    for item in items:
        if item == target:
            return item
    return None  # Explicitly return None if not found
```

### None vs False vs Empty
| Value | Boolean | Use Case |
|-------|---------|----------|
| None | False | Absence of value |
| False | False | Boolean false |
| "" | False | Empty string |
| [] | False | Empty list |
| 0 | False | Zero number |

---

## String Operations

### 1. String Slicing
Extract portions of a string using indices.

```python
s = "Hello, World!"

# Basic slicing
s[0:5]        # "Hello" (start:stop, exclusive)
s[:5]         # "Hello" (from beginning)
s[7:]         # "World!" (to end)
s[:]          # "Hello, World!" (copy)

# With step
s[::2]        # "Hlo ol!" (every 2nd character)
s[::-1]       # "!dlroW ,olleH" (reverse)
s[6:1:-1]     # ",olle" (negative step)

# Index mapping
#  H  e  l  l  o  ,     W  o  r  l  d  !
#  0  1  2  3  4  5  6  7  8  9 10 11 12
#-13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
```

### 2. F-Strings (Formatted String Literals)
Modern way to embed values in strings (Python 3.6+).

```python
name = "Alice"
age = 30
score = 95.5

# Basic usage
f"Hello, {name}!"                    # "Hello, Alice!"
f"{name} is {age} years old"         # "Alice is 30 years old"

# Formatting
f"{score:.2f}"                       # "95.50" (2 decimal places)
f"{age:05d}"                         # "00030" (zero-padded)
f"{age:,}"                           # "1,000,000" (thousands separator)

# Expressions inside f-strings
f"{name.upper()}"                    # "ALICE"
f"{age * 2}"                         # "60"
f"{name} is {'adult' if age >= 18 else 'minor'}"  # "Alice is adult"
```

### 3. split() Method
Split string into list of substrings.

```python
text = "apple,banana,cherry"

# Split by delimiter
text.split(",")           # ["apple", "banana", "cherry"]

# Split by whitespace (default)
"hello world".split()    # ["hello", "world"]

# Split with maxsplit
"a,b,c,d".split(",", 2)   # ["a", "b", "c,d"]

# Common use case: parsing input
line = "john,25,NYC"
name, age, city = line.split(",")
```

### 4. join() Method
Join list of strings into a single string.

```python
words = ["apple", "banana", "cherry"]

# Join with delimiter
",".join(words)           # "apple,banana,cherry"
" ".join(words)          # "apple banana cherry"
"-".join(words)          # "apple-banana-cherry"

# Common pattern: building strings efficiently
# WRONG: string concatenation in loop
result = ""
for word in words:
    result += word        # Creates new string each iteration - O(n²)

# RIGHT: use join
result = "".join(words)  # O(n)
```

### 5. Other Common String Methods

```python
s = "  Hello, World!  "

# Case conversion
s.upper()                 # "  HELLO, WORLD!  "
s.lower()                 # "  hello, world!  "
s.title()                 # "  Hello, World!  "
s.capitalize()            # "  hello, world!  "

# Whitespace
s.strip()                 # "Hello, World!" (removes both ends)
s.lstrip()                # "Hello, World!  "
s.rstrip()                # "  Hello, World!"

# Search and replace
s.find("World")           # 9 (index of first occurrence, -1 if not found)
s.index("World")          # 9 (raises ValueError if not found)
s.count("l")              # 3 (count occurrences)
s.replace("World", "Python")  # "  Hello, Python!  "

# Check methods
s.startswith("  Hello")   # True
s.endswith("!  ")        # True
s.isdigit()               # False
s.isalpha()               # False (has comma and space)
"123".isdigit()           # True

# Split and partition
"hello world".split()     # ["hello", "world"]
"hello world".partition(" ")  # ("hello", " ", "world") - returns 3-tuple
```

### String Immutability
Strings are immutable - they cannot be changed after creation.

```python
s = "hello"
# s[0] = "H"     # TypeError! Cannot modify in place

# To "modify", create new string
s = "H" + s[1:]   # "Hello" - new string created
```

---

## Interview Tips

### Common Pitfalls
1. **Off-by-one errors**: Remember slicing is exclusive on the end
2. **Integer division**: Use `//` for integer division, `/` returns float
3. **None vs empty**: Always check for both when validating input
4. **String concatenation in loops**: Use join() instead
5. **Mutable default arguments**: Never use mutable defaults in functions

### Time Complexity for String Operations
| Operation | Time |
|-----------|------|
| Index access | O(1) |
| Length | O(1) |
| Slice | O(k) where k is slice length |
| Concatenation | O(n) |
| join() | O(n) |
| split() | O(n) |
| find() | O(n) |

### Key Takeaways
- Understand string slicing with step
- Use f-strings for readable formatting
- Remember strings are immutable
- Use join() for efficient string building
- Be careful with None vs empty values
