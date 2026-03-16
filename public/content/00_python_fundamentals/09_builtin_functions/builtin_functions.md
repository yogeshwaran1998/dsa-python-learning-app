# Built-in Functions - Theory Guide

## Table of Contents
1. [Map](#map)
2. [Filter](#filter)
3. [Reduce](#reduce)
4. [Enumerate](#enumerate)
5. [Zip](#zip)
6. [All and Any](#all-and-any)
7. [Min and Max with Key](#min-and-max-with-key)
8. [Interview Tips](#interview-tips)

---

## Map

### What is map()?
The `map()` function applies a function to every item in an iterable and returns a map object (iterator).

### Syntax
```python
map(function, iterable, ...)
# Returns iterator, not list
```

### Key Points
- Returns a lazy iterator (Python 3)
- Can handle multiple iterables
- Function must accept same number of arguments as iterables

### Examples

**Basic usage:**
```python
# Square all numbers
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
# [1, 4, 9, 16, 25]
```

**With multiple iterables:**
```python
a = [1, 2, 3]
b = [4, 5, 6]
result = list(map(lambda x, y: x + y, a, b))
# [5, 7, 9]
```

**Performance:**
- Slightly slower than list comprehension in most cases
- But can be cleaner for complex transformations

---

## Filter

### What is filter()?
The `filter()` function filters elements based on a condition (function that returns True/False).

### Syntax
```python
filter(function, iterable)
# Returns iterator with elements where function returns True
```

### Key Points
- Returns elements where function returns True
- Function should return boolean
- Can use None as function (keeps truthy values)

### Examples

**Basic usage:**
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4, 6, 8, 10]
```

**With None:**
```python
# Keep non-empty, non-zero values
values = [0, 1, '', 'hello', None, 5]
filtered = list(filter(None, values))
# [1, 'hello', 5]
```

**Common pattern - filtering objects:**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

people = [Person('Alice', 30), Person('Bob', 17), Person('Charlie', 25)]
adults = list(filter(lambda p: p.age >= 18, people))
```

---

## Reduce

### What is reduce()?
The `reduce()` function from functools reduces an iterable to a single value by applying a function cumulatively.

### Syntax
```python
from functools import reduce
reduce(function, iterable, initial)
```

### Key Points
- Function takes two arguments: accumulator and current value
- Processes: acc = f(acc, item) for each item
- Can provide initial value

### Examples

**Sum all numbers:**
```python
from functools import reduce
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda acc, x: acc + x, numbers)
# 15
```

**Find maximum:**
```python
numbers = [5, 2, 8, 1, 9]
max_val = reduce(lambda acc, x: x if x > acc else acc, numbers)
# 9
```

**Flatten nested list:**
```python
nested = [[1, 2], [3, 4], [5, 6]]
flat = reduce(lambda acc, x: acc + x, nested)
# [1, 2, 3, 4, 5, 6]
```

---

## Enumerate

### What is enumerate()?
The `enumerate()` function adds a counter to an iterable and returns it as an enumerate object.

### Syntax
```python
enumerate(iterable, start=0)
# Returns (index, value) tuples
```

### Examples

**Basic usage:**
```python
fruits = ['apple', 'banana', 'cherry']
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
# 0: apple
# 1: banana
# 2: cherry
```

**With start parameter:**
```python
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}: {fruit}")
# 1: apple
# 2: banana
# 3: cherry
```

**Common pattern - create dictionary with index:**
```python
fruits = ['apple', 'banana', 'cherry']
indexed = {i: fruit for i, fruit in enumerate(fruits)}
# {0: 'apple', 1: 'banana', 2: 'cherry'}
```

---

## Zip

### What is zip()?
The `zip()` function combines multiple iterables element-wise into tuples.

### Syntax
```python
zip(*iterables, strict=False)
# Returns iterator of tuples
```

### Key Points
- Stops at shortest iterable (unless strict=True in Python 3.10+)
- Use `*zip()` to unzip

### Examples

**Combine two lists:**
```python
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
combined = list(zip(names, ages))
# [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
```

**Unzip:**
```python
combined = [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
names, ages = zip(*combined)
# names = ('Alice', 'Bob', 'Charlie')
# ages = (25, 30, 35)
```

**Create dictionary:**
```python
keys = ['a', 'b', 'c']
values = [1, 2, 3]
d = dict(zip(keys, values))
# {'a': 1, 'b': 2, 'c': 3}
```

**Iterate over multiple lists:**
```python
for name, age, city in zip(names, ages, cities):
    print(f"{name}, {age}, {city}")
```

---

## All and Any

### What are all() and any()?
- `all()`: Returns True if ALL elements are truthy
- `any()`: Returns True if ANY element is truthy

### Syntax
```python
all(iterable)
any(iterable)
```

### Examples

**Check if all elements satisfy condition:**
```python
numbers = [2, 4, 6, 8, 10]
all_even = all(x % 2 == 0 for x in numbers)
# True
```

**Check if any element satisfies condition:**
```python
numbers = [1, 3, 5, 6, 7]
has_even = any(x % 2 == 0 for x in numbers)
# True
```

**Validate input:**
```python
# Check if all required fields are present
required_fields = ['name', 'email', 'phone']
data = {'name': 'John', 'email': 'john@example.com'}
has_all = all(field in data for field in required_fields)
# False
```

**Empty iterable behavior:**
```python
all([])  # True (vacuous truth)
any([])  # False
```

---

## Min and Max with Key

### What is the key parameter?
The `key` parameter specifies a function of one argument to use as the comparison key.

### Syntax
```python
min(iterable, key=function)
max(iterable, key=function)
```

### Examples

**Find longest string:**
```python
words = ['apple', 'banana', 'cherry', 'date']
longest = max(words, key=len)
# 'banana'
```

**Find shortest string:**
```python
shortest = min(words, key=len)
# 'date'
```

**Find number with maximum absolute value:**
```python
numbers = [-10, 2, -5, 8]
max_abs = max(numbers, key=abs)
# -10 (has highest absolute value)
```

**Find most common character:**
```python
from collections import Counter
text = "hello world"
most_common = max(text, key=text.count)
# 'l' (appears 3 times)
```

**Find object with attribute:**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

people = [Person('Alice', 30), Person('Bob', 25), Person('Charlie', 35)]
oldest = max(people, key=lambda p: p.age)
# Person with Charlie (age 35)
```

**Find index of min/max:**
```python
numbers = [5, 2, 8, 1, 9]
min_index = numbers.index(min(numbers))
# 3 (index of value 1)
```

---

## Combined Patterns

### Map + Filter + Reduce
```python
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Sum of squares of even numbers
result = reduce(
    lambda acc, x: acc + x,
    map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers))
)
# 220
```

### Using Enumerate + Zip
```python
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 78]

# Create list of tuples with index
indexed = [(i, name, score) for i, (name, score) in enumerate(zip(names, scores))]
# [(0, 'Alice', 85), (1, 'Bob', 90), (2, 'Charlie', 78)]
```

---

## Interview Tips

### When to Use Each Function
- **map()**: When transforming every element
- **filter()**: When selecting subset of elements
- **reduce()**: When computing single value from sequence
- **enumerate()**: When you need indices
- **zip()**: When combining multiple iterables
- **all/any**: When checking conditions across elements
- **min/max with key**: When finding extremum by custom criteria

### Common Mistakes
1. Forgetting to convert map/filter to list (Python 3 returns iterator)
2. Using reduce when simpler alternatives exist
3. Confusing zip behavior with unequal length iterables

### Performance Considerations
- List comprehensions often faster than map()
- Generator expressions save memory
- Built-in functions are implemented in C (fast)

### Follow-up Questions
- "Can you do this without reduce?"
- "How would you handle empty input?"
- "What's the time/space complexity?"

---

## Summary

| Function | Purpose | Returns |
|----------|---------|---------|
| map() | Transform each element | Iterator |
| filter() | Select elements | Iterator |
| reduce() | Reduce to single value | Single value |
| enumerate() | Add counter | Iterator |
| zip() | Combine iterables | Iterator |
| all() | All truthy | Boolean |
| any() | Any truthy | Boolean |
| min/max | Find extremum | Single element |

---

## Practice Problems

### Easy
- [x] Square all numbers in a list using map
- [x] Filter positive numbers
- [x] Find sum using reduce
- [x] Enumerate a list with indices

### Medium
- [x] Find longest word using max with key
- [x] Combine two lists into dictionary using zip
- [x] Check if string has all unique characters
- [x] Find element with max attribute

### Hard
- [x] Group by using reduce
- [x] Implement your own version of map/filter
- [x] Chain multiple built-in functions
- [x] Handle edge cases (empty, None)
