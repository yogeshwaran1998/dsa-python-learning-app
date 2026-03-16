# Lists - Theory Guide

## Table of Contents
1. [List Creation](#list-creation)
2. [Indexing and Access](#indexing-and-access)
3. [List Slicing](#list-slicing)
4. [Mutability and Methods](#mutability-and-methods)
5. [Sorting](#sorting)
6. [List as Stack and Queue](#list-as-stack-and-queue)
7. [Interview Tips](#interview-tips)

---

## List Creation

### Basic Creation
```python
# Empty list
empty = []
empty2 = list()

# With elements
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

# Using list() constructor
from_list = list([1, 2, 3])
from_string = list("hello")      # ['h', 'e', 'l', 'l', 'o']

# List comprehension - Pythonic way to create lists
squares = [x**2 for x in range(10)]
even_numbers = [x for x in range(20) if x % 2 == 0]
```

### Common Patterns
```python
# Repeated elements
zeros = [0] * 5                # [0, 0, 0, 0, 0]
repeated = [1, 2] * 3          # [1, 2, 1, 2, 1, 2]

# Nested lists
matrix = [[1, 2], [3, 4]]      # 2D list
3d_array = [[[0] * 3 for _ in range(3)] for _ in range(3)]
```

---

## Indexing and Access

### Positive Indexing (0-based)
```python
arr = [10, 20, 30, 40, 50]
arr[0]    # 10 (first element)
arr[1]    # 20 (second element)
arr[4]    # 50 (last element)
```

### Negative Indexing
```python
arr[-1]   # 50 (last element)
arr[-2]   # 40 (second to last)
arr[-5]   # 10 (first element)
```

### Index Mapping
```
Index:    0    1    2    3    4
Value:   10   20   30   40   50
Index:   -5   -4   -3   -2   -1
```

### Out of Bounds
```python
arr = [1, 2, 3]
# arr[10]   # IndexError: list index out of range
```

---

## List Slicing

### Basic Slicing
```python
arr = [0, 1, 2, 3, 4, 5]

arr[1:4]    # [1, 2, 3] (start to stop-1)
arr[:3]     # [0, 1, 2] (beginning to stop-1)
arr[3:]     # [3, 4, 5] (start to end)
arr[:]      # [0, 1, 2, 3, 4, 5] (copy of entire list)
```

### With Step
```python
arr[::2]    # [0, 2, 4] (every 2nd element)
arr[1::2]   # [1, 3, 5] (every 2nd starting from index 1)
arr[::-1]   # [5, 4, 3, 2, 1, 0] (reverse)
arr[::-2]   # [5, 3, 1] (reverse, every 2nd)
```

### Modify via Slice
```python
arr = [0, 1, 2, 3, 4, 5]
arr[1:3] = [10, 20]  # [0, 10, 20, 3, 4, 5]
arr[:2] = []         # Remove first two: [20, 3, 4, 5]
```

---

## Mutability and Methods

### Mutability
Lists are mutable - can be changed after creation.
```python
arr = [1, 2, 3]
arr[0] = 10          # [10, 2, 3]
arr.append(4)        # [10, 2, 3, 4]
```

### Common Methods

| Method | Description | Time |
|--------|-------------|------|
| append(x) | Add to end | O(1)* |
| insert(i, x) | Insert at index | O(n) |
| remove(x) | Remove first occurrence | O(n) |
| pop(i) | Remove and return at index | O(1)* |
| clear() | Remove all elements | O(n) |
| index(x) | Return first index of x | O(n) |
| count(x) | Count occurrences | O(n) |
| sort() | Sort in-place | O(n log n) |
| reverse() | Reverse in-place | O(n) |

*Amortized O(1)

### Examples
```python
# Adding elements
arr = [1, 2]
arr.append(3)           # [1, 2, 3]
arr.insert(1, 10)       # [1, 10, 2, 3]
arr.extend([4, 5])      # [1, 10, 2, 3, 4, 5]

# Removing elements
arr.remove(10)          # [1, 2, 3, 4, 5]
arr.pop()               # Returns 5, arr = [1, 2, 3, 4]
arr.pop(0)              # Returns 1, arr = [2, 3, 4]

# Finding
arr = [1, 2, 3, 2]
arr.index(2)            # 1 (first occurrence)
arr.count(2)            # 2

# Other
arr = [3, 1, 2]
arr.sort()             # [1, 2, 3]
arr.reverse()          # [3, 2, 1]
```

---

## Sorting

### sort() vs sorted()

```python
# sort() - modifies original list (in-place)
arr = [3, 1, 2]
arr.sort()              # arr = [1, 2, 3]

# sorted() - returns new sorted list
arr = [3, 1, 2]
sorted_arr = sorted(arr)  # [1, 2, 3], arr unchanged
```

### Sorting Options
```python
# Reverse sort
arr.sort(reverse=True)
sorted(arr, reverse=True)

# Custom key function
words = ["banana", "apple", "cherry"]
arr.sort(key=len)        # Sort by length: ["apple", "banana", "cherry"]

# Case-insensitive sorting
words = ["Banana", "apple", "Cherry"]
arr.sort(key=str.lower)  # ["apple", "Banana", "Cherry"]

# Sort by multiple criteria
pairs = [(1, "a"), (2, "b"), (1, "c")]
pairs.sort(key=lambda x: (x[0], x[1]))  # Sort by first, then second
```

### Custom Objects
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

people = [Person("Alice", 30), Person("Bob", 25)]
people.sort(key=lambda p: p.age)  # Sort by age
```

---

## List as Stack and Queue

### Stack (LIFO)
```python
stack = []

# Push - add to end
stack.append(1)      # [1]
stack.append(2)      # [1, 2]
stack.append(3)      # [1, 2, 3]

# Pop - remove from end
top = stack.pop()    # Returns 3, stack = [1, 2]

# Peek
top = stack[-1]      # 2 (without removing)
```

### Queue (FIFO)
```python
from collections import deque

queue = deque()

# Enqueue - add to end
queue.append(1)      # [1]
queue.append(2)      # [1, 2]
queue.append(3)      # [1, 2, 3]

# Dequeue - remove from front
front = queue.popleft()  # Returns 1, queue = [2, 3]

# Peek
front = queue[0]     # 2 (without removing)
```

### Why Not Use list for Queue?
```python
# Using list as queue is O(n) for popleft()
queue = [1, 2, 3]
front = queue.pop(0)  # O(n) - must shift all elements

# Use deque for O(1) operations
```

---

## Interview Tips

### Time Complexity Summary

| Operation | Average | Worst |
|-----------|---------|-------|
| Access by index | O(1) | O(1) |
| Append | O(1) | O(n) |
| Pop from end | O(1) | O(1) |
| Pop from front | O(n) | O(n) |
| Insert at index | O(n) | O(n) |
| Remove at index | O(n) | O(n) |
| Search | O(n) | O(n) |
| Sort | O(n log n) | O(n log n) |

### Common Mistakes
1. **Modifying while iterating** - causes unexpected behavior
2. **Using list for queue** - use deque instead
3. **Forgetting slice copies** - arr[:] creates copy
4. **Mutating sorted copy** - check if sort() or sorted()

### Key Patterns
- Use list comprehension for creating lists
- Use deque for queue operations
- Remember negative indexing
- Use enumerate for index-value pairs
- Sort with key for custom ordering
