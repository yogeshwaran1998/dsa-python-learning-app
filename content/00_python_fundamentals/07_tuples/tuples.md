# Tuples - Theory Guide

## Table of Contents
1. [Tuple Creation](#tuple-creation)
2. [Immutability](#immutability)
3. [Packing and Unpacking](#packing-and-unpacking)
4. [namedtuple](#namedtuple)
5. [Multiple Return Values](#multiple-return-values)
6. [Interview Tips](#interview-tips)

---

## Tuple Creation

### Basic Creation
```python
# Empty tuple
empty = ()
empty2 = tuple()

# Single element (note: comma is required!)
single = (1,)          # (1,) - tuple
not_tuple = (1)        # 1 - just an integer

# Multiple elements
point = (1, 2, 3)
person = ("Alice", 30, "NYC")

# Without parentheses (packing)
coordinates = 1, 2, 3  # Creates tuple (1, 2, 3)

# From iterable
from_list = tuple([1, 2, 3])     # (1, 2, 3)
from_string = tuple("hello")    # ('h', 'e', 'l', 'l', 'o')
from_range = tuple(range(5))    # (0, 1, 2, 3, 4)
```

### Tuple vs List
| Feature | Tuple | List |
|---------|-------|------|
| Syntax | () | [] |
| Mutable | No | Yes |
| Performance | Faster | Slower |
| Memory | Less | More |
| Hashable | Yes (if elements are) | No |

---

## Immutability

### What It Means
Tuples cannot be modified after creation.

```python
# Valid operations
t = (1, 2, 3)
print(t[0])              # Access by index - OK
print(t[1:2])            # Slice - OK
print(t + (4, 5))        # Concatenation - returns new tuple
print(t * 2)            # Repetition - returns new tuple

# Invalid - these will raise errors
t[0] = 10               # TypeError!
t.append(4)             # AttributeError!
t.remove(1)              # AttributeError!
t[1:2] = [20]           # TypeError!
```

### Why Use Tuples?
1. **Hashable** - can be used as dictionary keys
2. **Memory efficient** - less overhead than lists
3. **Intent** - signals "this won't change"
4. **Safety** - prevents accidental modification

---

## Packing and Unpacking

### Tuple Packing
Multiple values in one variable.
```python
point = 10, 20, 30      # Packing into tuple
```

### Tuple Unpacking
Extract values into variables.
```python
# Basic unpacking
point = (10, 20, 30)
x, y, z = point         # x=10, y=20, z=30

# With parentheses (optional but clearer)
x, y, z = (10, 20, 30)

# Extended unpacking (Python 3)
first, *middle, last = (1, 2, 3, 4, 5)
# first=1, middle=[2,3,4], last=5

# Swap without temp variable
a, b = 1, 2
a, b = b, a              # a=2, b=1
```

### Practical Unpacking
```python
# In loops
pairs = [(1, 2), (3, 4), (5, 6)]
for a, b in pairs:
    print(a + b)

# In function arguments
def print_coords(x, y):
    print(f"({x}, {y})")

point = (10, 20)
print_coords(*point)     # Unpacks to print_coords(10, 20)

# Multiple assignment
name, age, city = "Alice", 30, "NYC"
```

---

## namedtuple

### What is namedtuple?
A factory function for creating tuple subclasses with named fields.

### Import and Creation
```python
from collections import namedtuple

# Define namedtuple
Point = namedtuple("Point", ["x", "y"])
# Or: Point = namedtuple("Point", "x y")

# Create instance
p = Point(10, 20)

# Access by name
print(p.x)               # 10
print(p.y)               # 20

# Access by index
print(p[0])              # 10
print(p[1])              # 20

# Unpacking works
x, y = p
```

### Methods
```python
from collections import namedtuple

Point = namedtuple("Point", "x y")

# _fields - tuple of field names
print(Point._fields)     # ('x', 'y')

# _asdict() - return as OrderedDict
p = Point(10, 20)
print(p._asdict())       # OrderedDict([('x', 10), ('y', 20)])

# _replace() - create new instance with modified fields
p2 = p._replace(x=30)   # Point(x=30, y=20)

# _make() - create from iterable
p3 = Point._make([30, 40])  # Point(x=30, y=40)
```

### Use Cases
```python
# Perfect for representing records
from collections import namedtuple

Employee = namedtuple("Employee", ["name", "department", "salary"])
emp = Employee("Alice", "Engineering", 100000)

# Clean access
print(emp.name)
print(emp.department)

# Works well with data processing
from collections import namedtuple
Result = namedtuple("Result", ["success", "data", "message"])
```

---

## Multiple Return Values

### Functions Return Tuples
```python
def divide(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

result = divide(10, 3)
# result = (3, 1)

# Unpack immediately
q, r = divide(10, 3)
```

### Common Pattern: min/max with index
```python
def find_min_max(arr):
    if not arr:
        return None, None
    return min(arr), max(arr)

min_val, max_val = find_min_max([1, 2, 3])
```

### Pattern: Success/failure with data
```python
def search(items, target):
    for i, item in enumerate(items):
        if item == target:
            return True, i
    return False, -1

found, index = search([1, 2, 3], 2)
```

---

## Time Complexity

| Operation | Time |
|-----------|------|
| Access by Interview Tips

### index | O(1) |
| Search | O(n) |
| Concatenation | O(n) |
| Repetition | O(nk) |

### Key Differences: Tuple vs List

1. **Immutability**: Tuples cannot be modified
2. **Performance**: Tuples are faster
3. **Memory**: Tuples use less memory
4. **Usage**: Tuples for fixed data, lists for dynamic
5. **Hashing**: Tuples can be dict keys (if hashable)

### Common Patterns

1. **Return multiple values**
```python
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)
```

2. **Swap values**
```python
a, b = b, a
```

3. **Dictionary keys**
```python
locations = {(40.7128, -74.0060): "NYC", (51.5074, -0.1278): "London"}
```

4. **Namedtuple for records**
```python
from collections import namedtuple
Point = namedtuple("Point", "x y z")
```

### Key Takeaways
- Tuples are immutable sequences
- Use parentheses but tuple works without
- Unpacking is powerful for multiple assignments
- namedtuple provides named fields
- Great for multiple return values
- Can be used as dictionary keys
