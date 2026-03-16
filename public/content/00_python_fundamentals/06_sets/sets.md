# Sets - Theory Guide

## Table of Contents
1. [Set Creation](#set-creation)
2. [Set Operations](#set-operations)
3. [Membership Testing](#membership-testing)
4. [frozenset](#frozenset)
5. [Interview Tips](#interview-tips)

---

## Set Creation

### Basic Creation
```python
# Empty set (note: {} creates dict, not set)
empty = set()

# With elements
fruits = {"apple", "banana", "cherry"}

# From iterable
from_list = set([1, 2, 3, 2])    # {1, 2, 3} - removes duplicates
from_string = set("hello")        # {'h', 'e', 'l', 'o'}
from_range = set(range(5))        # {0, 1, 2, 3, 4}

# Set comprehension
squares = {x**2 for x in range(5)}  # {0, 1, 4, 9, 16}
```

### Properties
- Unordered (no index access)
- No duplicates
- Elements must be hashable (immutable)

---

## Set Operations

### Union (| or union())
All elements from both sets.
```python
a = {1, 2, 3}
b = {3, 4, 5}

# Using | operator
result = a | b           # {1, 2, 3, 4, 5}

# Using method
result = a.union(b)      # {1, 2, 3, 4, 5}

# Union with multiple sets
result = a | b | {6, 7}
```

### Intersection (& or intersection())
Common elements.
```python
a = {1, 2, 3}
b = {3, 4, 5}

# Using & operator
result = a & b           # {3}

# Using method
result = a.intersection(b)  # {3}
```

### Difference (- or difference())
Elements in first set but not in second.
```python
a = {1, 2, 3}
b = {3, 4, 5}

# Using - operator
result = a - b           # {1, 2}

# Using method
result = a.difference(b)  # {1, 2}
```

### Symmetric Difference (^ or symmetric_difference())
Elements in either set but not both.
```python
a = {1, 2, 3}
b = {3, 4, 5}

# Using ^ operator
result = a ^ b           # {1, 2, 4, 5}

# Using method
result = a.symmetric_difference(b)  # {1, 2, 4, 5}
```

### Operation Summary Table

| Operation | Method | Description |
|-----------|--------|-------------|
| \| | union() | All elements |
| & | intersection() | Common elements |
| - | difference() | In a not in b |
| ^ | symmetric_difference() | Not in both |

### Modifying Sets

```python
s = {1, 2, 3}

s.add(4)           # Add one element: {1, 2, 3, 4}
s.update([4, 5, 6])  # Add multiple: {1, 2, 3, 4, 5, 6}

s.remove(3)        # Remove element (raises KeyError if not found)
s.discard(3)       # Remove (no error if not found)

s.pop()            # Remove and return arbitrary element

s.clear()          # Remove all elements
```

---

## Membership Testing

### Key Property: O(1) Lookup
Sets are optimized for membership testing.

```python
fruits = {"apple", "banana", "cherry"}

# Check membership - O(1) time
"apple" in fruits       # True
"orange" in fruits      # False

# Using not in
"orange" not in fruits  # True
```

### Practical Use Cases

```python
# Remove duplicates while preserving order
def unique_elements(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result

# Check for duplicates
def has_duplicates(items):
    return len(items) != len(set(items))

# Common interview pattern: two-sum with set
def has_pair_sum(nums, target):
    seen = set()
    for num in nums:
        if target - num in seen:
            return True
        seen.add(num)
    return False
```

---

## frozenset

### What is frozenset?
An immutable version of set - cannot be modified after creation.

### Why Use frozenset?
- Can be used as dictionary keys
- Can be elements of other sets
- Thread-safe (immutable)

### Creation
```python
# Create frozenset
fs = frozenset([1, 2, 3])
fs2 = frozenset("hello")

# From regular set
s = {1, 2, 3}
fs = frozenset(s)
```

### Operations
Most set operations work, but no modifying operations.

```python
fs1 = frozenset([1, 2, 3])
fs2 = frozenset([3, 4, 5])

# These work (return new frozenset)
union = fs1 | fs2          # frozenset({1, 2, 3, 4, 5})
intersection = fs1 & fs2   # frozenset({3})
difference = fs1 - fs2     # frozenset({1, 2})

# These DON'T work (would modify)
# fs1.add(4)    # AttributeError
# fs1.remove(1)  # AttributeError
```

### Use as Dictionary Key
```python
# Valid: frozenset as key
d = {frozenset([1, 2]): "pair", frozenset([3, 4]): "another"}

# Invalid: regular set as key
# d = {{1, 2}: "pair"}  # TypeError: unhashable type
```

---

## Interview Tips

### Time Complexity

| Operation | Average | Worst |
|-----------|---------|-------|
| Add | O(1) | O(n) |
| Remove | O(1) | O(n) |
| Membership (in) | O(1) | O(n) |
| Union | O(n + m) | - |
| Intersection | O(min(n,m)) | O(n*m) |

### Common Patterns

1. **Remove Duplicates**
```python
unique = list(set(items))  # Order not preserved!
```

2. **Find Common Elements**
```python
common = set1 & set2
```

3. **Check for Intersection**
```python
if set1 & set2:  # Non-empty intersection
    # Do something
```

4. **Two Sum Optimization**
```python
def has_pair_sum(nums, target):
    seen = set()
    for num in nums:
        if target - num in seen:
            return True
        seen.add(num)
    return False
```

### Key Takeaways
- Use sets for O(1) membership testing
- Remember sets are unordered
- Use frozenset when immutability needed
- Many operations available (union, intersection, difference)
- Great for finding duplicates and commonalities
