# Comprehensions - Theory Guide

## Table of Contents
1. [List Comprehensions](#list-comprehensions)
2. [Dictionary Comprehensions](#dictionary-comprehensions)
3. [Set Comprehensions](#set-comprehensions)
4. [Generator Expressions](#generator-expressions)
5. [Yield and Generators](#yield-and-generators)
6. [Interview Tips](#interview-tips)

---

## List Comprehensions

### What is a List Comprehension?
A list comprehension is a concise way to create lists in Python. It consists of an expression followed by a for clause, then zero or more for or if clauses.

### Basic Syntax
```python
[expression for item in iterable]
[expression for item in iterable if condition]
[expression for item in iterable for other_item in other_iterable]
```

### Why Use List Comprehensions?
- More concise and readable than traditional loops
- Often faster than equivalent for loops (optimized in CPython)
- Functional programming style preferred in interviews

### Examples

**Basic transformation:**
```python
# Square all numbers
squares = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

**With condition:**
```python
# Even numbers only
evens = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]
```

**Nested comprehension:**
```python
# Flatten a matrix
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
# [1, 2, 3, 4, 5, 6]
```

**With conditional expression:**
```python
# FizzBuzz style
result = ['Fizz' if x % 3 == 0 else x for x in range(5)]
# [0, 1, 2, 'Fizz', 4]
```

### Time Complexity
- O(n) for basic comprehension
- O(n*m) for nested comprehensions where n and m are the sizes

---

## Dictionary Comprehensions

### What is a Dictionary Comprehension?
Similar to list comprehensions, but creates dictionaries instead.

### Basic Syntax
```python
{key: value for item in iterable}
{key: value for item in iterable if condition}
```

### Examples

**Create dictionary from lists:**
```python
keys = ['a', 'b', 'c']
values = [1, 2, 3]
d = {k: v for k, v in zip(keys, values)}
# {'a': 1, 'b': 2, 'c': 3}
```

**Swap keys and values:**
```python
original = {'a': 1, 'b': 2, 'c': 3}
swapped = {v: k for k, v in original.items()}
# {1: 'a', 2: 'b', 3: 'c'}
```

**Filter dictionary:**
```python
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
filtered = {k: v for k, v in d.items() if v > 2}
# {'c': 3, 'd': 4}
```

**Count characters:**
```python
from collections import Counter
text = "hello world"
char_count = {char: text.count(char) for char in set(text)}
# {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
```

---

## Set Comprehensions

### What is a Set Comprehension?
Creates sets (unique elements) using comprehension syntax.

### Basic Syntax
```python
{expression for item in iterable}
{expression for item in iterable if condition}
```

### Examples

**Unique squares:**
```python
squares = {x**2 for x in range(-3, 4)}
# {0, 1, 4, 9}
```

**Unique vowels in text:**
```python
text = "hello world"
vowels = {char for char in text if char in 'aeiou'}
# {'e', 'o'}
```

**Common elements between lists:**
```python
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common = {x for x in list1 if x in list2}
# {3, 4, 5}
```

---

## Generator Expressions

### What is a Generator Expression?
A generator expression is like a list comprehension, but it returns a generator object instead of a list. It yields values on-demand (lazy evaluation).

### Syntax
```python
(expression for item in iterable)
(expression for item in iterable if condition)
```

### List Comprehension vs Generator Expression

```python
# List comprehension - evaluates immediately, stores all in memory
squares_list = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Generator expression - lazy evaluation
squares_gen = (x**2 for x in range(10))
# <generator object <genexpr> at 0x...>
```

### Why Use Generators?
1. **Memory Efficiency**: Don't store all values in memory at once
2. **Lazy Evaluation**: Compute values on-demand
3. **Infinite Sequences**: Can represent infinite sequences

### When to Use
- Large datasets that don't fit in memory
- Processing streams of data
- When you only need to iterate once

### Examples

```python
# Sum of first 1000 squares
sum_squares = sum(x**2 for x in range(1000))
# 332833500

# Find first 5 even squares
gen = (x**2 for x in range(100) if x % 2 == 0)
first_five = [next(gen) for _ in range(5)]
# [0, 4, 16, 36, 64]
```

---

## Yield and Generators

### What is Yield?
The `yield` keyword is used in generator functions to produce a value without destroying the function's local state.

### Generator Functions vs Regular Functions
- Regular function: executes completely, returns once
- Generator function: can pause and resume, yielding multiple values

### Basic Example
```python
def count_up_to(n):
    """Generator that yields numbers from 1 to n."""
    i = 1
    while i <= n:
        yield i
        i += 1

# Usage
for num in count_up_to(5):
    print(num)  # 1, 2, 3, 4, 5
```

### Infinite Generator
```python
def fibonacci():
    """Infinite Fibonacci sequence generator."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Usage - be careful to limit iteration!
fib = fibonacci()
for _ in range(10):
    print(next(fib))  # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
```

### Generator with Send
```python
def counter():
    """Generator that can receive values."""
    count = 0
    while True:
        increment = yield count
        if increment is None:
            count += 1
        else:
            count += increment

c = counter()
print(next(c))  # 0
print(c.send(5))  # 5
print(next(c))  # 6
```

### Performance Considerations
- Generators are memory-efficient for large sequences
- They are iterable only once (cannot reuse)
- Slightly slower than list comprehensions for small data

---

## Common Interview Patterns

### 1. Filter and Transform
```python
# Find squares of even numbers
result = [x**2 for x in numbers if x % 2 == 0]
```

### 2. Group By
```python
from collections import defaultdict

# Group words by first letter
words = ['apple', 'banana', 'cherry', 'apricot']
grouped = defaultdict(list)
for word in words:
    grouped[word[0]].append(word)
# {'a': ['apple', 'apricot'], 'b': ['banana'], 'c': ['cherry']}
```

### 3. Dictionary from Two Lists
```python
keys = ['a', 'b', 'c']
values = [1, 2, 3]
d = dict(zip(keys, values))
# {'a': 1, 'b': 2, 'c': 3}
```

### 4. Matrix Transposition
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
```

### 5. Unique Elements with Count
```python
from collections import Counter

text = "hello world"
counts = Counter(text)
# Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
```

---

## Interview Tips

### When to Use Comprehensions
- Prefer comprehensions for simple transformations
- Use regular loops for complex logic (multiple conditions, complex mutations)
- Generators for large datasets

### Common Mistakes to Avoid
1. **Forgetting the brackets**: `[x for x in range(5)]` vs `(x for x in range(5))`
2. **Memory issues**: Don't use list comprehension for huge data
3. **Nested comprehensions**: Can become hard to read - consider separate loops

### Performance Tips
- List comprehensions are generally faster than for loops
- Use generators for memory efficiency
- `sum()`, `min()`, `max()` with generator expressions are efficient

### Follow-up Questions
- "Can you optimize this for memory?"
- "What if the data doesn't fit in memory?"
- "How would you make this lazy?"

---

## Summary

| Type | Syntax | Use Case |
|------|--------|----------|
| List Comprehension | `[x for x in list]` | Create lists |
| Dict Comprehension | `{k: v for k, v in items}` | Create dictionaries |
| Set Comprehension | `{x for x in list}` | Unique elements |
| Generator | `(x for x in list)` | Lazy evaluation |

---

## Practice Problems

### Easy
- [x] Create list of squares for numbers 1-10
- [x] Filter even numbers from a list
- [x] Create dictionary from two lists

### Medium
- [x] Flatten a nested list
- [x] Find all prime numbers up to n using generator
- [x] Group words by length

### Hard
- [x] Create lazy Fibonacci generator
- [x] Implement pipeline with multiple generators
- [x] Memory-efficient processing of large files
