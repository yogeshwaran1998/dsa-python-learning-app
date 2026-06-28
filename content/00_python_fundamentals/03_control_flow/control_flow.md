# Control Flow - Theory Guide

## Table of Contents
1. [If-Elif-Else](#if-elif-else)
2. [For Loops](#for-loops)
3. [While Loops](#while-loops)
4. [Range Function](#range-function)
5. [Break, Continue, and Else](#break-continue-and-else)
6. [Match-Case (Python 3.10+)](#match-case-python-310)
7. [Interview Tips](#interview-tips)

---

## If-Elif-Else

### Basic Syntax
```python
if condition:
    # executes if condition is True
    pass
elif other_condition:
    # executes if first condition is False and this is True
    pass
else:
    # executes if all conditions are False
    pass
```

### Key Points
- No parentheses needed around conditions
- Colon (:) required after condition
- Indentation defines the code block
- elif = "else if"

### Examples

```python
# Simple if
age = 18
if age >= 18:
    print("Adult")

# If-else
if age >= 18:
    print("Adult")
else:
    print("Minor")

# If-elif-else chain
score = 85
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
```

### Falsy Values in Conditions
These evaluate to False:
- None
- False
- Zero: 0, 0.0, 0j
- Empty sequences: "", [], {}
- Objects with __bool__() returning False

```python
# These are all "falsy"
if not None:
    print("None is falsy")
if not 0:
    print("0 is falsy")
if not "":
    print("Empty string is falsy")
if not []:
    print("Empty list is falsy")
```

---

## For Loops

### Basic Syntax
```python
for item in iterable:
    # do something with item
    pass
```

### Iterating Over Different Types

```python
# String - iterate over characters
for char in "hello":
    print(char)

# List - iterate over elements
for item in [1, 2, 3]:
    print(item)

# Dictionary - iterate over keys (default)
for key in {"a": 1, "b": 2}:
    print(key)

# Using enumerate() - get index and value
for index, value in enumerate([10, 20, 30]):
    print(f"Index: {index}, Value: {value}")

# Using zip() - iterate over multiple sequences
for name, age in zip(["Alice", "Bob"], [25, 30]):
    print(f"{name} is {age}")
```

---

## While Loops

### Basic Syntax
```python
while condition:
    # runs while condition is True
    pass
```

### Examples

```python
# Countdown
count = 5
while count > 0:
    print(count)
    count -= 1
print("Blast off!")

# Find first matching element
items = [1, 3, 5, 7, 9]
target = 5
index = 0
while index < len(items):
    if items[index] == target:
        print(f"Found at index {index}")
        break
    index += 1
```

---

## Range Function

### Syntax
```python
range(stop)                    # 0 to stop-1
range(start, stop)             # start to stop-1
range(start, stop, step)       # start to stop-1, incrementing by step
```

### Key Points
- stop is EXCLUSIVE (like slicing)
- step can be negative
- Returns a range object (lazy evaluation)

### Examples

```python
# Basic usage
list(range(5))        # [0, 1, 2, 3, 4]
list(range(2, 5))     # [2, 3, 4]
list(range(0, 10, 2)) # [0, 2, 4, 6, 8]

# Negative step (reverse)
list(range(5, 0, -1))  # [5, 4, 3, 2, 1]
list(range(5, 0, -2))   # [5, 3, 1]

# Common patterns
for i in range(10):           # 0 to 9
    print(i)

for i in range(len(arr)):     # iterate with index
    print(arr[i])

for i in range(0, 100, 10):  # 0, 10, 20, ..., 90
    print(i)
```

---

## Break, Continue, and Else

### Break
- Exits the loop immediately
- Only exits the innermost loop (if nested)

```python
for i in range(10):
    if i == 5:
        break  # Exit loop when i is 5
    print(i)
# Output: 0, 1, 2, 3, 4
```

### Continue
- Skips the rest of current iteration
- Moves to next iteration

```python
for i in range(5):
    if i == 2:
        continue  # Skip when i is 2
    print(i)
# Output: 0, 1, 3, 4 (skips 2)
```

### Else in Loops
- Executes after loop completes normally (no break)
- Does NOT execute if loop exits via break

```python
# Search example - using else with for
for i in range(10):
    if i == 7:
        print(f"Found {i}")
        break
else:
    print("Not found")  # Only runs if break not executed
```

---

## Match-Case (Python 3.10+)

### Basic Syntax
```python
match variable:
    case pattern1:
        # handle pattern1
    case pattern2:
        # handle pattern2
    case _:
        # default case (like else)
```

### Patterns

```python
# Literal values
def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Server Error"
        case _:
            return "Unknown"

# Multiple values (OR pattern)
def grade(score):
    match score:
        case 90 | 91 | 92 | 93 | 94 | 95 | 96 | 97 | 98 | 99 | 100:
            return "A"
        case 80 | 81 | 82 | 83 | 84 | 85 | 86 | 87 | 88 | 89:
            return "B"
        case _:
            return "C or below"

# Wildcard with capture
def describe(x):
    match x:
        case 0:
            return "zero"
        case _ as n if n > 0:
            return f"positive: {n}"
        case _:
            return f"negative: {n}"
```

---

## Interview Tips

### Common Patterns

1. **Iterating with index**
   ```python
   for i in range(len(arr)):
       # use arr[i]
   ```

2. **Iterating with index and value**
   ```python
   for i, val in enumerate(arr):
       # use i and val
   ```

3. **Finding elements**
   ```python
   for i, val in enumerate(arr):
       if val == target:
           return i
   return -1
   ```

4. **Using else with loop**
   - Common for search algorithms
   - Ensures you know if loop completed naturally

### Pitfalls

1. **Off-by-one errors with range**
   - Remember: range(stop) goes from 0 to stop-1

2. **Infinite loops**
   - Always ensure loop condition eventually becomes False

3. **Modifying list while iterating**
   - Creates unexpected behavior
   - Use list copy or different approach

4. **Using = instead of ==**
   - Assignment returns the assigned value (truthy if non-zero)

### Time Complexity
- for loop: O(n) iterations
- while loop: O(n) iterations (depends on condition)
- range(): O(n) to materialize

### Space Complexity
- Loop variables: O(1) typically
- Additional data structures vary
