# Itertools - Theory Guide

## Table of Contents
1. [Introduction](#introduction)
2. [Infinite Iterators](#infinite-iterators)
3. [Combinatoric Iterators](#combinatoric-iterators)
4. [Iterator Slicing](#iterator-slicing)
5. [Chain and Chain.from_iterable](#chain-and-chainfrom_iterable)
6. [Product](#product)
7. [Common Patterns](#common-patterns)
8. [Performance Tips](#performance-tips)

---

## Introduction

The `itertools` module provides a collection of fast, memory-efficient tools for working with iterables. These are essential for competitive programming and efficient Python code.

### Why Use Itertools?
- **Memory efficient**: Most return iterators, not lists
- **Fast**: Implemented in C
- **Composable**: Can be chained together
- **Idiomatic**: Pythonic way to handle iterables

---

## Infinite Iterators

These iterators generate infinite sequences. Use with caution!

### 1. count(start=0, step=1)
Creates an infinite counter.

```python
from itertools import count

# Infinite counter starting at 0
for i in count():
    if i > 10:
        break
    print(i)  # 0, 1, 2, ...

# Start from 5, step by 2
for i in count(5, 2):
    if i > 15:
        break
    print(i)  # 5, 7, 9, 11, 13, 15
```

### 2. cycle(iterable)
Cycles through an iterable indefinitely.

```python
from itertools import cycle

# Infinite loop through [1, 2, 3]
counter = 0
for item in cycle([1, 2, 3]):
    print(item)  # 1, 2, 3, 1, 2, 3, ...
    counter += 1
    if counter > 7:
        break
```

### 3. repeat(elem, n=None)
Repeats an element n times or infinitely.

```python
from itertools import repeat

# Repeat 5 three times
for item in repeat(5, 3):
    print(item)  # 5, 5, 5

# Infinite repeat
for i, item in enumerate(repeat('x')):
    if i > 3:
        break
    print(item)  # x, x, x, x
```

---

## Combinatoric Iterators

These generate combinations and permutations.

### 1. permutations(iterable, r=None)
Generates all permutations (order matters).

```python
from itertools import permutations

# All permutations of length 2
for p in permutations('ABC', 2):
    print(p)  # ('A','B'), ('A','C'), ('B','A'), ...

# All permutations of entire iterable
for p in permutations('ABC'):
    print(p)  # ('A','B','C'), ('A','C','B'), ...
```

### 2. combinations(iterable, r)
Generates all combinations (order doesn't matter).

```python
from itertools import combinations

# All combinations of 2
for c in combinations('ABC', 2):
    print(c)  # ('A','B'), ('A','C'), ('B','C')

# Notice: ('B','A') is NOT included (order doesn't matter)
```

### 3. combinations_with_replacement(iterable, r)
Allows repeated elements in combinations.

```python
from itertools import combinations_with_replacement

# Combinations with replacement
for c in combinations_with_replacement('AB', 2):
    print(c)  # ('A','A'), ('A','B'), ('B','B')
```

### 4. product(*iterables, repeat=1)
Cartesian product of input iterables.

```python
from itertools import product

# Cartesian product of two sets
for p in product([1, 2], ['a', 'b']):
    print(p)  # (1,'a'), (1,'b'), (2,'a'), (2,'b')

# For dice rolls (two dice)
for roll in product(range(1, 7), range(1, 7)):
    print(roll)

# Repeat parameter for multiple iterations
for p in product('AB', repeat=3):
    print(p)  # All 3-length strings from 'A','B'
```

---

## Iterator Slicing

### islice(iterable, start, stop, step)
Slices an iterator without creating the full sequence.

```python
from itertools import islice

# First 5 elements
for item in islice(range(100), 5):
    print(item)  # 0, 1, 2, 3, 4

# Elements from index 5 to 10
for item in islice(range(100), 5, 10):
    print(item)  # 5, 6, 7, 8, 9

# Every other element
for item in islice(range(100), 0, 100, 2):
    print(item)  # 0, 2, 4, 6, ...
```

---

## Chain and Chain.from_iterable

### chain(*iterables)
Chains multiple iterables together.

```python
from itertools import chain

# Chain multiple iterables
for item in chain([1, 2], [3, 4], [5]):
    print(item)  # 1, 2, 3, 4, 5

# Flatten using chain
matrix = [[1, 2], [3, 4]]
flat = list(chain.from_iterable(matrix))
print(flat)  # [1, 2, 3, 4]
```

### chain.from_iterable(iterable)
Chains an iterable of iterables.

```python
from itertools import chain

# Nested structure
nested = [[1, 2], [3, 4], [5]]
flat = list(chain.from_iterable(nested))
print(flat)  # [1, 2, 3, 4, 5]

# Equivalent to:
flat = [x for sublist in nested for x in sublist]
```

---

## Common Patterns

### 1. Filter with Multiple Conditions

```python
from itertools import filterfalse

# Filter false (opposite of filter)
for item in filterfalse(lambda x: x > 5, range(10)):
    print(item)  # 0, 1, 2, 3, 4, 5
```

### 2. Group Adjacent Elements

```python
from itertools import groupby

# Group by first letter
data = ['apple', 'apricot', 'banana', 'blueberry']
for key, group in groupby(data, lambda x: x[0]):
    print(f"{key}: {list(group)}")
# a: ['apple', 'apricot']
# b: ['banana', 'blueberry']
```

### 3. Accumulate (Running Sum)

```python
from itertools import accumulate

# Running sum
for total in accumulate([1, 2, 3, 4, 5]):
    print(total)  # 1, 3, 6, 10, 15

# With custom function (multiply)
for product in accumulate([1, 2, 3, 4], lambda x, y: x * y):
    print(product)  # 1, 2, 6, 24
```

### 4. Drop/Take

```python
from itertools import dropwhile, takewhile

# Take while condition is true
for item in takewhile(lambda x: x < 5, range(10)):
    print(item)  # 0, 1, 2, 3, 4

# Drop while condition is true
for item in dropwhile(lambda x: x < 5, range(10)):
    print(item)  # 5, 6, 7, 8, 9
```

### 5. Pairwise

```python
from itertools import pairwise  # Python 3.10+

# Consecutive pairs
for a, b in pairwise('ABCDE'):
    print(f"{a}-{b}")  # A-B, B-C, C-D, D-E
```

---

## Performance Tips

### 1. Lazy Evaluation
All itertools functions return iterators, not lists. They don't evaluate until needed.

```python
# This doesn't create a list
count(1, 2)  # Just returns an iterator object

# Only evaluates when iterated
for i in count(1, 2):
    if i > 10:
        break
    print(i)
```

### 2. Memory Efficiency
Use `islice` to limit memory usage.

```python
# BAD: Creates full list
result = [x**2 for x in range(10**8)]

# GOOD: Only computes what's needed
result = islice((x**2 for x in range(10**8)), 100)
```

### 3. Combining with List Comprehensions

```python
# Get first 10 permutations as list
result = list(islice(permutations('ABC'), 10))

# Filter and take
result = list(takewhile(lambda x: sum(x) < 10, combinations(range(5), 3)))
```

---

## Interview Tips

### Common Problems Solved with Itertools

1. **Generate all subsets**: Use `product` with repeat
2. **Generate all combinations**: Use `combinations`
3. **Generate all permutations**: Use `permutations`
4. **Iterate with index**: Use `islice` with `enumerate`
5. **Sliding window**: Use `zip` with `islice`

### Example: Subsets Using Product

```python
# Generate all subsets of [1, 2, 3]
# Each element can be either in or out (0 or 1)
from itertools import product

def subsets(nums):
    result = []
    for choices in product([0, 1], repeat=len(nums)):
        subset = [nums[i] for i in range(len(nums)) if choices[i]]
        result.append(subset)
    return result
```

### Example: Sliding Window

```python
from itertools import islice

def sliding_window(seq, n):
    """Generate sliding windows of size n."""
    it = iter(seq)
    window = tuple(islice(it, n))
    if len(window) == n:
        yield window
    for item in it:
        window = window[1:] + (item,)
        yield window
```

---

## Summary

| Function | Purpose | Example |
|----------|---------|---------|
| `count()` | Infinite counter | `count(1, 2)` |
| `cycle()` | Infinite loop | `cycle([1,2,3])` |
| `repeat()` | Repeat element | `repeat(5, 3)` |
| `permutations()` | All orderings | `permutations('ABC', 2)` |
| `combinations()` | Selections (no order) | `combinations('ABC', 2)` |
| `combinations_with_replacement()` | With replacement | `combinations_with_replacement('A', 2)` |
| `product()` | Cartesian product | `product([1,2], [3,4])` |
| `islice()` | Slice iterator | `islice(it, 5, 10)` |
| `chain()` | Chain iterables | `chain(a, b, c)` |
| `chain.from_iterable()` | Flatten | `chain.from_iterable(nested)` |

---

## Practice Problems

- [x] Generate all valid parentheses combinations
- [x] Find all subsets of an array
- [x] Generate all combinations of coins to make amount
- [x] Implement sliding window using itertools
- [x] Flatten deeply nested list
