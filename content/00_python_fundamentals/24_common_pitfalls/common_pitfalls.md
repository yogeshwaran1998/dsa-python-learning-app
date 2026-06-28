# Common Python Pitfalls - Theory Guide

## Table of Contents
1. [Introduction](#introduction)
2. [Mutable Default Arguments](#mutable-default-arguments)
3. [Shallow vs Deep Copy](#shallow-vs-deep-copy)
4. [Generator Exhaustion](#generator-exhaustion)
5. [Integer Caching](#integer-caching)
6. [Late Binding in Closures](#late-binding-in-closures)
7. [Other Common Pitfalls](#other-common-pitfalls)

---

## Introduction

Python has many features that can trip up developers, especially those coming from other languages. Understanding these common pitfalls is essential for writing correct code and passing interviews.

---

## Mutable Default Arguments

### The Problem

Using mutable objects (list, dict) as default arguments can lead to unexpected behavior.

```python
# WRONG - Mutable default argument
def append_to(element, to=[]):  # Empty list created ONCE at definition!
    to.append(element)
    return to

# Usage
append_to(1)  # Returns [1]
append_to(2)  # Returns [1, 2] - NOT [2]!
append_to(3)  # Returns [1, 2, 3]
```

### Why This Happens

The default argument is evaluated once when the function is defined, not each time it's called. The same list object is shared across all calls.

### Correct Solutions

```python
# Solution 1: Use None as default
def append_to(element, to=None):
    if to is None:
        to = []  # Create new list each call
    to.append(element)
    return to

# Solution 2: Use mutable checking
def append_to(element, to=[]):
    to = to or []  # Creates new list if to is falsy
    to.append(element)
    return to
```

### Real-world Examples

```python
# WRONG
def add_item(item, items=[]):
    items.append(item)
    return items

# CORRECT
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

---

## Shallow vs Deep Copy

### The Problem

Understanding the difference between shallow and deep copying is crucial for nested data structures.

### Shallow Copy

Creates a new object but doesn't recursively copy nested objects.

```python
import copy

# Shallow copy - top level is new, nested are same
original = [[1, 2], [3, 4]]
shallow = copy.copy(original)  # or original[:] or list(original)

# Modify top level
shallow.append([5, 6])
print(original)  # [[1, 2], [3, 4]] - unchanged
print(shallow)   # [[1, 2], [3, 4], [5, 6]]

# Modify NESTED element
shallow[0][0] = 999
print(original)  # [[999, 2], [3, 4]] - CHANGED!
print(shallow)   # [[999, 2], [3, 4]]
```

### Deep Copy

Recursively copies all nested objects.

```python
import copy

original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)

# Modify nested
deep[0][0] = 999

print(original)  # [[1, 2], [3, 4]] - unchanged!
print(deep)       # [[999, 2], [3, 4]]
```

### Copy Methods Summary

| Method | Top Level | Nested | Speed |
|--------|-----------|--------|-------|
| `copy.copy()` | New | Same reference | Fast |
| `copy.deepcopy()` | New | New (recursive) | Slow |
| `list()` / `list[:]` | New | Same reference | Fast |
| `dict()` / `dict.copy()` | New | Same reference | Fast |
| `.copy()` on dict | New | Same reference | Fast |

### When to Use Each

```python
import copy

# For simple lists (no nesting)
new_list = old_list[:]  # Shallow is fine

# For nested lists
new_list = copy.deepcopy(old_list)

# For lists of objects
new_list = [obj.copy() for obj in old_list]

# For dicts
new_dict = old_dict.copy()  # Shallow
new_dict = copy.deepcopy(old_dict)  # Deep
```

---

## Generator Exhaustion

### The Problem

Generators can only be iterated once. After exhaustion, they return nothing.

```python
# Create generator
gen = (x for x in range(3))

# First iteration
print(list(gen))  # [0, 1, 2]

# Second iteration - exhausted!
print(list(gen))  # [] - Empty!
```

### Solutions

```python
# Solution 1: Convert to list if needed multiple times
gen = (x for x in range(3))
gen_list = list(gen)  # Materialize
print(list(gen_list))  # [0, 1, 2]
print(list(gen_list))  # [0, 1, 2] - Works!

# Solution 2: Create new generator
def my_generator():
    for x in range(3):
        yield x

gen1 = my_generator()
gen2 = my_generator()  # Fresh generator

# Solution 3: Use itertools.tee (careful with memory)
from itertools import tee
gen1, gen2 = tee(x for x in range(3))
```

### Common Mistake with Functions

```python
# WRONG - Generator exhausted after first use
def get_squares(n):
    return (x**2 for x in range(n))

squares = get_squares(5)
print(list(squares))  # [0, 1, 4, 9, 16]
print(list(squares))  # [] - Empty!

# CORRECT - Return list or make function reusable
def get_squares_list(n):
    return [x**2 for x in range(n)]
```

---

## Integer Caching

### The Problem

Python caches small integers (-5 to 256) for performance. This can cause unexpected behavior in certain situations.

```python
# Integer caching
a = 256
b = 256
print(a is b)  # True - Same object!

a = 257
b = 257
print(a is b)  # False - Different objects!

# This affects comparisons
a = 256
b = 256
print(a == b)  # True (value)
print(a is b)  # True (identity) - because cached!

# But for larger integers
a = 257
b = 257
print(a == b)  # True (value)
print(a is b)  # False (identity) - not cached!
```

### When This Matters

```python
# Using 'is' for comparison - WRONG
if user_id is 1:  # WRONG!
    pass

# Should use ==
if user_id == 1:  # Correct!
    pass

# In sets/dicts with integers - BE CAREFUL
s = set()
s.add(256)
s.add(256)
print(len(s))  # 1 - Same value

s.add(257)
s.add(257)
print(len(s))  # 2 - Different objects but same value

# Dict keys
d = {}
d[256] = "value1"
d[256] = "value2"
print(len(d))  # 1 - Overwrites (same key)

d[257] = "value1"
d[257] = "value2"
print(len(d))  # 1 - Overwrites (same key)
```

### Why Caching Exists

- Performance: Small integers are used frequently
- Memory: Reusing objects saves memory
- This is an implementation detail, not guaranteed!

---

## Late Binding in Closures

### The Problem

In closures, variables are captured by reference, not by value. The value is looked up when the function is called, not when it's defined.

```python
# WRONG - All functions refer to same 'i'
def create_functions():
    return [lambda: i for i in range(3)]

funcs = create_functions()
for f in funcs():
    print(f())  # All print 2! (last value of i)
```

### Solutions

```python
# Solution 1: Default argument (captures value)
def create_functions():
    return [lambda x=i: x for i in range(3)]

# Solution 2: Use closure with parameter
def create_functions():
    return [make_function(i) for i in range(3)]

def make_function(i):
    return lambda: i

# Solution 3: Use enumerate
def create_functions():
    return [(lambda x=i: x) for i in range(3)]
```

---

## Other Common Pitfalls

### 1. Modifying List While Iterating

```python
# WRONG
for item in my_list:
    if should_remove(item):
        my_list.remove(item)

# CORRECT
# Option 1: Create new list
new_list = [item for item in my_list if not should_remove(item)]

# Option 2: Iterate over copy
for item in my_list[:]:  # Slice creates copy
    if should_remove(item):
        my_list.remove(item)
```

### 2. Using mutable objects as dict keys

```python
# WRONG - List is not hashable
d = {[1, 2]: "value"}  # TypeError!

# CORRECT - Use tuple
d = {(1, 2): "value"}
```

### 3. Floating point comparison

```python
# WRONG
0.1 + 0.2 == 0.3  # False!

# CORRECT - Use math.isclose
import math
math.isclose(0.1 + 0.2, 0.3)  # True
```

### 4. Default mutable in class

```python
# WRONG
class Foo:
    def __init__(self, items=[]):
        self.items = items

# CORRECT
class Foo:
    def __init__(self, items=None):
        self.items = items if items is not None else []
```

### 5. Forgetting to return in recursion

```python
# WRONG
def sum_list(lst):
    if not lst:
        return 0  # But what about the recursive case?
    return sum_list(lst[1:])  # Missing return!

# CORRECT
def sum_list(lst):
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])
```

---

## Summary Table

| Pitfall | Symptom | Solution |
|---------|---------|----------|
| Mutable default | Same list across calls | Use None |
| Shallow copy | Nested changes affect original | Use deepcopy |
| Generator exhaustion | Empty after first use | Convert to list |
| Integer caching | Unexpected is comparison | Use == |
| Late binding | Closure captures wrong value | Use default arg |
| Modify while iterating | Skip elements | Use copy or comprehension |

---

## Interview Tips

### Questions to Expect
1. "What is the output of this code?"
2. "How would you fix this bug?"
3. "What is the difference between shallow and deep copy?"
4. "Why does this generator only work once?"

### Always Check
1. Are default arguments mutable?
2. Are you modifying while iterating?
3. Are you using generators correctly?
4. Are you using 'is' vs '==' correctly?

---

## Practice Problems

- [x] Fix the mutable default argument bug
- [x] Deep copy a nested dictionary
- [x] Fix the closure late binding issue
- [x] Copy a list with nested lists correctly
- [x] Create reusable generator function
