# Python Idioms - Theory Guide

## Table of Contents
1. [Introduction](#introduction)
2. [Walrus Operator (:=)](#walrus-operator-)
3. [Chained Comparisons](#chained-comparisons)
4. [Variable Swapping](#variable-swapping)
5. [Multiple Assignment (Tuple Unpacking)](#multiple-assignment-tuple-unpacking)
6. [Conditional Expressions (Ternary)](#conditional-expressions-ternary)
7. [Enumerate and Zip](#enumerate-and-zip)
8. [List/Dict/Set Comprehensions](#listdictset-comprehensions)
9. [Useful One-Liners](#useful-one-liners)
10. [Best Practices](#best-practices)

---

## Introduction

Python idioms are conventional ways of writing Python code that are considered elegant, efficient, and Pythonic. Understanding these idioms helps you write cleaner, more readable, and more efficient code.

---

## Walrus Operator (:=)

The walrus operator (`:=`) assigns and returns a value in a single expression. Introduced in Python 3.8.

### Syntax
```python
# variable := expression
```

### Use Cases

#### 1. In While Loops
```python
# Without walrus - read file line by line
line = f.readline()
while line:
    process(line)
    line = f.readline()

# With walrus - more concise
while line := f.readline():
    process(line)
```

#### 2. In List Comprehensions
```python
# Without walrus - calculate twice
results = [x for x in data if expensive(x) > threshold]

# With walrus - calculate once
results = [y for x in data if (y := expensive(x)) > threshold]

# Another example
data = [1, 2, 3, 4, 5]
# Without walrus
squares = [x**2 for x in data if x**2 > 10]
# With walrus - more efficient
squares = [sq for x in data if (sq := x**2) > 10]
```

#### 3. In Conditional Expressions
```python
# Without walrus
match = pattern.search(text)
if match:
    process(match.group())

# With walrus - assignment in condition
if (match := pattern.search(text)):
    process(match.group())
```

#### 4. Avoiding Repeated Function Calls
```python
# Without walrus - function called twice
if calculate_expensive_value() > threshold:
    do_something(calculate_expensive_value())

# With walrus - function called once
if (val := calculate_expensive_value()) > threshold:
    do_something(val)
```

---

## Chained Comparisons

Python allows chaining comparison operators. This is both readable and efficient.

### Syntax
```python
# a < b < c is equivalent to (a < b) and (b < c)
```

### Examples

#### 1. Range Checks
```python
# Traditional way
if x > 0 and x < 10:
    pass

# Chained comparison - cleaner
if 0 < x < 10:
    pass
```

#### 2. Multiple Conditions
```python
# Check if x is between a and b (exclusive)
if a < x < b:
    pass

# Check if x is at least a and at most b
if a <= x <= b:
    pass
```

#### 3. Common Patterns
```python
# Check if all equal
if a == b == c:
    pass

# Check if in ascending order
if a < b < c < d:
    pass

# With different operators
if a < b <= c:
    pass  # equivalent to (a < b) and (b <= c)
```

### Efficiency Note
Chained comparisons are more efficient than using `and` because each comparison is only evaluated once.

---

## Variable Swapping

Python makes swapping variables elegant and efficient.

### Traditional Way (Requires Temp Variable)
```python
temp = a
a = b
b = temp
```

### Pythonic Way (Direct Swap)
```python
# Single statement - no temp variable needed
a, b = b, a
```

### With Multiple Variables
```python
# Swap three variables
a, b, c = c, a, b
```

### Application in Algorithms
```python
# In-place sorting with swaps
arr = [3, 1, 2]
arr[0], arr[1] = arr[1], arr[0]  # Swap first two elements

# Two pointers
left, right = 0, len(arr) - 1
while left < right:
    # Process
    left += 1
    right -= 1
```

---

## Multiple Assignment (Tuple Unpacking)

Python excels at unpacking iterables into multiple variables.

### Basic Unpacking
```python
# Tuple
a, b, c = (1, 2, 3)

# List
a, b, c = [1, 2, 3]

# String
a, b, c = "123"
```

### Extended Unpacking (*)
```python
# First and rest
first, *rest = [1, 2, 3, 4, 5]
# first = 1, rest = [2, 3, 4, 5]

# First, middle, last
first, *middle, last = [1, 2, 3, 4, 5]
# first = 1, middle = [2, 3, 4], last = 5

# Ignore values
a, _, c = [1, 2, 3]  # a = 1, c = 3

# Pack remaining
*prefix, last = [1, 2, 3, 4]
# prefix = [1, 2, 3], last = 4
```

### Swapping via Unpacking
```python
a, b = b, a  # Classic swap
```

### Swap with Condition (Ternary)
```python
# Conditional swap
a, b = b, a if a > b else a, b

# More readable
if a > b:
    a, b = b, a
```

---

## Conditional Expressions (Ternary)

Python's ternary operator is clean and readable.

### Syntax
```python
result = value_if_true if condition else value_if_false
```

### Examples
```python
# Basic
age = 20
status = "adult" if age >= 18 else "minor"

# In assignments
max_val = a if a > b else b

# Nested
grade = "A" if score >= 90 else "B" if score >= 80 else "C"

# With None default
value = user_input or "default"

# Combining with walrus (Python 3.8+)
if (result := compute()) is not None:
    process(result)
```

---

## Enumerate and Zip

### Enumerate
Adds index to iteration.

```python
# Without enumerate - manual counter
i = 0
for item in items:
    print(i, item)
    i += 1

# With enumerate - cleaner
for i, item in enumerate(items):
    print(i, item)

# Start from specific index
for i, item in enumerate(items, start=1):
    print(i, item)
```

### Zip
Iterate over multiple sequences in parallel.

```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

# Without zip - index based
for i in range(len(names)):
    print(names[i], ages[i])

# With zip - cleaner
for name, age in zip(names, ages):
    print(name, age)

# Unequal lengths - stops at shortest
for name, age in zip(names, ages):
    pass  # Stops at 3

# Iterate over dictionary with enumerate
for i, (key, value) in enumerate(d.items()):
    print(i, key, value)
```

---

## List/Dict/Set Comprehensions

Comprehensions are Python's elegant way to create collections.

### List Comprehensions
```python
# Basic
squares = [x**2 for x in range(10)]

# With condition
evens = [x for x in range(10) if x % 2 == 0]

# Nested
matrix = [[i*j for j in range(3)] for i in range(3)]

# With function
processed = [func(x) for x in items]
```

### Dict Comprehensions
```python
# Basic
squares = {x: x**2 for x in range(5)}

# From two lists
dict(zip(keys, values))

# Filter existing
{k: v for k, v in d.items() if v > 0}
```

### Set Comprehensions
```python
# Basic
unique = {x for x in items}

# With condition
evens = {x for x in range(10) if x % 2 == 0}
```

---

## Useful One-Liners

### Swap Without Temporary
```python
a, b = b, a
```

### Reverse String
```python
s[::-1]
```

### Flatten List
```python
# From nested lists
flat = [x for sublist in nested for x in sublist]

# Using itertools
from itertools import chain
flat = list(chain.from_iterable(nested))
```

### Count Occurrences
```python
from collections import Counter
counts = Counter(items)

# Without imports
counts = {k: items.count(k) for k in set(items)}
```

### Get First/Last
```python
first = items[0]
last = items[-1]
first = next(iter(items))  # For sets/dicts
```

### Merge Dictionaries
```python
# Python 3.9+
merged = d1 | d2

# Python 3.5+
merged = {**d1, **d2}

# Update
d1.update(d2)
```

### Check All/Any
```python
all_positive = all(x > 0 for x in items)
any_negative = any(x < 0 for x in items)
```

---

## Best Practices

### 1. Use Walrus Wisely
- Only use when it improves readability
- Avoid overuse that makes code harder to read

### 2. Chain Comparisons When Appropriate
- Use for range checks: `0 <= x < n`
- Avoid confusing chains: don't mix operators without clear meaning

### 3. Prefer Pythonic Swapping
- Always use `a, b = b, a` instead of temp variables

### 4. Use Extended Unpacking
- Makes code clearer than index-based access
- Be careful with mixed types

### 5. Comprehensions Over Loops
- Use comprehensions for simple transformations
- Use regular loops for complex logic

---

## Interview Tips

### Common Idioms to Know
1. `a, b = b, a` - Swap
2. `a < b < c` - Chained comparison
3. `[x for x in items]` - List comprehension
4. `{k: v for k, v in items}` - Dict comprehension
5. `enumerate(items)` - With indices
6. `zip(a, b)` - Parallel iteration
7. `:=` - Walrus operator

### Code Review Points
- Are comprehensions used where appropriate?
- Is there repeated computation that could use walrus?
- Are comparisons chained or verbose?
- Is swapping done efficiently?

---

## Summary

| Idiom | Syntax | Example |
|-------|--------|---------|
| Walrus | `:=` | `if (x := func()) > 0:` |
| Chained comparison | `a < b < c` | `0 <= x < 10` |
| Swap | `a, b = b, a` | `a, b = b, a` |
| Extended unpacking | `a, *b, c` | `first, *rest = items` |
| Ternary | `a if cond else b` | `"yes" if x > 0 else "no"` |
| Comprehension | `[x for x in items]` | `[x**2 for x in range(10)]` |

---

## Practice Problems

- [x] Use walrus to optimize repeated function calls
- [x] Write range check with chained comparison
- [x] Swap variables without temp
- [x] Use extended unpacking to get first, middle, last
- [x] Flatten nested list with comprehension
