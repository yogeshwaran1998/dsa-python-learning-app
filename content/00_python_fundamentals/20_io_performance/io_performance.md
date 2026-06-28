# I/O Performance - Theory Guide

## Table of Contents
1. [Introduction](#introduction)
2. [Standard Input Methods](#standard-input-methods)
3. [Fast Input Techniques](#fast-input-techniques)
4. [Output Formatting](#output-formatting)
5. [Competitive Programming I/O Patterns](#competitive-programming-io-patterns)
6. [File I/O](#file-io)
7. [Common Pitfalls](#common-pitfalls)
8. [Best Practices](#best-practices)

---

## Introduction

In competitive programming and large-scale data processing, I/O (Input/Output) performance is often the bottleneck. Python's default input functions can be slow for large inputs due to:
- Buffer management overhead
- Line-by-line processing
- Type conversion overhead

Understanding and optimizing I/O can make the difference between TLE (Time Limit Exceeded) and accepted solutions.

---

## Standard Input Methods

### 1. input() Function

```python
# Simple but slow for large inputs
line = input()           # Read single line
name = input("Enter: ")  # With prompt
```

**Time Complexity**: O(n) where n is line length
**Typical Speed**: ~10,000 lines/second

### 2. sys.stdin.readline()

```python
import sys
line = sys.stdin.readline()  # Faster than input()
```

**Time Complexity**: O(n)
**Typical Speed**: ~100,000 lines/second

### 3. sys.stdin.buffer.read()

```python
import sys
data = sys.stdin.buffer.read()  # Read entire input at once
```

**Time Complexity**: O(n) total
**Typical Speed**: ~1,000,000+ lines/second

---

## Fast Input Techniques

### 1. Reading All Input at Once

```python
import sys

# Read entire input as bytes
data = sys.stdin.buffer.read()

# Convert to string
text = data.decode()

# Split into lines
lines = text.split()

# Parse integers
numbers = list(map(int, lines))
```

### 2. Using map() with Iterator

```python
import sys

# Read all integers efficiently
data = sys.stdin.buffer.read().split()
numbers = list(map(int, data))
```

### 3. Generator-based Input

```python
import sys

def ints():
    """Generator that yields integers one at a time."""
    for num in sys.stdin.buffer.read().split():
        yield int(num)

# Usage
it = ints()
n = next(it)
arr = [next(it) for _ in range(n)]
```

### 4. Using iter() with Callback

```python
import sys

data = sys.stdin.buffer.read().split()
it = iter(data)

n = int(next(it))
arr = [int(next(it)) for _ in range(n)]
```

---

## Output Formatting

### 1. Building Output String

```python
# Slow: Multiple print calls
for i in range(1000):
    print(i)

# Fast: Build string and print once
output = '\n'.join(str(i) for i in range(1000))
print(output)
```

### 2. Using String Formatting

```python
# f-strings (Python 3.6+) - Fast
name = "Alice"
age = 30
print(f"{name} is {age} years old")

# format() - Slightly slower
print("{} is {} years old".format(name, age))

# % formatting - Old style
print("%s is %d years old" % (name, age))
```

### 3. Using sys.stdout.write()

```python
import sys

# Faster than print() - no newline, no flush
sys.stdout.write("Hello\n")
sys.stdout.write(str(value) + "\n")
```

### 4. Collecting Output with list join

```python
# Build output as list of strings
output_lines = []
for i in range(1000):
    output_lines.append(f"Line {i}: {i * 2}")

# Join and print once
print('\n'.join(output_lines))
```

---

## Competitive Programming I/O Patterns

### Pattern 1: Single Integer

```python
import sys

n = int(sys.stdin.readline())
```

### Pattern 2: Multiple Integers on One Line

```python
import sys

a, b, c = map(int, sys.stdin.readline().split())
```

### Pattern 3: Unknown Number of Integers

```python
import sys

arr = list(map(int, sys.stdin.read().split()))
```

### Pattern 4: Multiple Lines, Unknown Count

```python
import sys

# Read all, process line by line
data = sys.stdin.read().splitlines()
for line in data:
    # Process each line
    pass
```

### Pattern 5: Grid/Matrix Input

```python
import sys

def read_grid(rows """Read a, cols):
    grid of characters."""
    grid = []
    for _ in range(rows):
        line = sys.stdin.readline().strip()
        grid.append(list(line))
    return grid

def read_int_matrix(rows):
    """Read matrix of integers."""
    return [list(map(int, sys.stdin.readline().split())) for _ in range(rows)]
```

### Pattern 6: Space-separated Without Newlines

```python
import sys

# All input is space-separated
data = sys.stdin.buffer.read().split()
# data = [b'1', b'2', b'3', ...]
numbers = [int(x) for x in data]
```

### Pattern 7: Interactive Problems

```python
import sys

def query(x, y):
    """Send query and read response."""
    sys.stdout.write(f"? {x} {y}\n")
    sys.stdout.flush()
    return int(sys.stdin.readline())
```

---

## File I/O

### 1. Reading Files

```python
# Basic file reading
with open('input.txt', 'r') as f:
    content = f.read()

# Line by line
with open('input.txt', 'r') as f:
    for line in f:
        print(line, end='')

# With context manager - recommended
with open('file.txt', 'r') as f:
    data = f.read()
```

### 2. Writing Files

```python
# Write string
with open('output.txt', 'w') as f:
    f.write("Hello\n")

# Write multiple lines
lines = ["line1", "line2", "line3"]
with open('output.txt', 'w') as f:
    f.write('\n'.join(lines))

# Append to file
with open('log.txt', 'a') as f:
    f.write("new entry\n")
```

### 3. Binary Files

```python
# Read binary
with open('data.bin', 'rb') as f:
    data = f.read()

# Write binary
with open('data.bin', 'wb') as f:
    f.write(b'\x00\x01\x02')
```

### 4. Buffered I/O

```python
# Using buffered reader for large files
import io

# Create buffer
buffer = io.BufferedReader(sys.stdin.buffer)

# Read through buffer
data = buffer.read(1024)  # Read 1024 bytes
```

---

## Common Pitfalls

### 1. Forgetting to Strip Newlines

```python
# Wrong
line = sys.stdin.readline()
if line == "":  # Never true, line is "\n"

# Correct
line = sys.stdin.readline().strip()
```

### 2. Mixing sys.stdin and sys.stdin.buffer

```python
# Use consistently - either text or buffer
# sys.stdin - text mode (decoded)
# sys.stdin.buffer - binary mode (faster for integers)
```

### 3. Not Converting Types Early

```python
# Wrong - converts in loop
for _ in range(n):
    x = int(sys.stdin.readline())  # Slow

# Correct - batch convert
arr = list(map(int, sys.stdin.read().split()))
```

### 4. Using print() in Tight Loops

```python
# Wrong - many I/O calls
for i in range(100000):
    print(i)

# Correct - single output
output = '\n'.join(map(str, range(100000)))
print(output)
```

---

## Best Practices

### 1. For Competitive Programming

```python
import sys

def solve():
    # Use buffer for input
    data = sys.stdin.buffer.read().split()

    # Parse efficiently
    it = iter(data)
    n = int(next(it))
    arr = [int(next(it)) for _ in range(n)]

    # Process...

    # Use join for output
    output = '\n'.join(map(str, result))
    sys.stdout.write(output)

solve()
```

### 2. For Large File Processing

```python
import sys

def process_large_file(filepath):
    with open(filepath, 'r') as f:
        # Process line by line to avoid memory issues
        for line in f:
            # Process line
            pass
```

### 3. Using functools.lru_cache for I/O

```python
from functools import lru_cache
import sys

@lru_cache(maxsize=None)
def expensive_io_operation(x):
    # Expensive operation with I/O
    return compute(x)
```

---

## Performance Comparison

| Method | Speed (ops/sec) | Best For |
|--------|-----------------|----------|
| `input()` | ~10,000 | Small inputs |
| `sys.stdin.readline()` | ~100,000 | Medium inputs |
| `sys.stdin.buffer.read()` | ~1,000,000+ | Large inputs |

### Output Methods Comparison

| Method | Speed | Best For |
|--------|-------|----------|
| `print()` | Medium | Debugging |
| `sys.stdout.write()` | Fast | Competitive |
| `'\n'.join()` + single print | Fastest | Batch output |

---

## Summary

| Technique | Speed Improvement | Use Case |
|-----------|------------------|----------|
| `sys.stdin.buffer.read()` | 10-100x | Large inputs |
| Batch parsing with split() | 5-10x | Integer arrays |
| Collect + join output | 5-10x | Large outputs |
| Avoid `input()` in loops | Variable | Always |
| Use `.strip()` correctly | Variable | Always |

---

## Practice Problems

- [x] Read 10^6 integers and compute sum
- [x] Read grid of N x M characters
- [x] Process log file with 10^7 lines
- [x] Handle mixed integer and string input
- [x] Implement fast output for sorted results
