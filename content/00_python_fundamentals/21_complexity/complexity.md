# Time and Space Complexity of Python Operations - Theory Guide

## Table of Contents
1. [Introduction](#introduction)
2. [List Complexity](#list-complexity)
3. [Dictionary (dict) Complexity](#dictionary-dict-complexity)
4. [Set Complexity](#set-complexity)
5. [String Complexity](#string-complexity)
6. [Tuple Complexity](#tuple-complexity)
7. [Heap Operations](#heap-operations)
8. [Common Operations Comparison](#common-operations-comparison)
9. [Interview Tips](#interview-tips)

---

## Introduction

Understanding the time and space complexity of Python's built-in data structures is crucial for writing efficient code and performing well in technical interviews. This guide covers the complexity of operations on Lists, Dictionaries, Sets, Strings, and Tuples.

### Big O Notation Reminder
- **O(1)**: Constant time - independent of input size
- **O(log n)**: Logarithmic time - halves problem each step
- **O(n)**: Linear time - proportional to input size
- **O(n log n)**: Linearithmic time - common in sorting
- **O(n^2)**: Quadratic time - nested loops
- **O(2^n)**: Exponential time - recursive with exponential growth

---

## List Complexity

Python's list is a dynamic array (not a linked list). Understanding this helps predict performance.

### Time Complexity

| Operation | Average Case | Worst Case | Notes |
|-----------|-------------|------------|-------|
| `list[i]` | O(1) | O(1) | Direct index access |
| `list.append(x)` | O(1) | O(n)* | *Amortized O(1), occasional resize |
| `list.insert(i, x)` | O(n) | O(n) | Shifts elements |
| `list.pop()` | O(1) | O(1) | Pop from end |
| `list.pop(0)` | O(n) | O(n) | Pop from beginning - shifts all |
| `list.remove(x)` | O(n) | O(n) | Searches, then shifts |
| `list.index(x)` | O(n) | O(n) | Linear search |
| `x in list` | O(n) | O(n) | Linear search |
| `list.sort()` | O(n log n) | O(n log n) | Timsort |
| `sorted(list)` | O(n log n) | O(n log n) | Returns new list |
| `list.reverse()` | O(n) | O(n) | In-place reverse |
| `list.count(x)` | O(n) | O(n) | Counts occurrences |
| `list.extend(iter)` | O(k) | O(k) | k = length of iter |
| `list.copy()` | O(n) | O(n) | Shallow copy |

### Space Complexity
- **List creation**: O(n)
- **Append**: O(1) amortized

### Important Notes
1. Python lists are dynamic arrays with occasional resize (usually 1.125x growth factor)
2. Amortized analysis shows append is O(1) average
3. Insert at beginning is O(n) because all elements shift
4. Use collections.deque for O(1) insert/delete at both ends

---

## Dictionary (dict) Complexity

Python dict uses a hash table implementation with open addressing.

### Time Complexity

| Operation | Average Case | Worst Case | Notes |
|-----------|-------------|------------|-------|
| `d[key]` | O(1) | O(n) | Key access |
| `d[key] = value` | O(1) | O(n) | Insert/update |
| `d.get(key)` | O(1) | O(n) | Safe access |
| `key in d` | O(1) | O(n) | Membership test |
| `d.keys()` | O(1) | O(1) | View (iterator) |
| `d.values()` | O(1) | O(1) | View (iterator) |
| `d.items()` | O(1) | O(1) | View (iterator) |
| `d.pop(key)` | O(1) | O(n) | Remove key |
| `d.popitem()` | O(1) | O(1) | Remove arbitrary item |
| `d.update(other)` | O(k) | O(n) | k = len(other) |
| `d.clear()` | O(n) | O(n) | Clear all |

### Worst Case Details
Worst case O(n) occurs when there are hash collisions, causing the hash table to degrade to linear search. This is extremely rare in practice.

### Space Complexity
- **Dict creation**: O(n)
- **Per entry overhead**: ~72 bytes per entry (varies)

### Important Notes
1. Dictionary keys must be hashable (immutable)
2. Starting from Python 3.7, dict maintains insertion order
3. Use defaultdict for automatic missing key handling

---

## Set Complexity

Sets are implemented as hash tables (like dict, but only storing keys).

### Time Complexity

| Operation | Average Case | Worst Case | Notes |
|-----------|-------------|------------|-------|
| `x in s` | O(1) | O(n) | Membership test |
| `s.add(x)` | O(1) | O(n) | Add element |
| `s.remove(x)` | O(1) | O(n) | Remove (raises if missing) |
| `s.discard(x)` | O(1) | O(n) | Remove (no error if missing) |
| `s.pop()` | O(1) | O(1) | Remove arbitrary element |
| `s.union(t)` | O(len(s) + len(t)) | O(n + m) | Union |
| `s.intersection(t)` | O(min(len(s), len(t))) | O(n * m) | Intersection |
| `s.difference(t)` | O(len(s)) | O(n) | Set difference |
| `s.copy()` | O(n) | O(n) | Shallow copy |

### Space Complexity
- **Set creation**: O(n)
- **Similar to dict**: ~72 bytes per element

### Important Notes
1. Sets do not allow duplicate elements
2. Sets are unordered (before Python 3.7)
3. Use sets for membership testing, deduplication
4. frozenset is immutable and hashable

---

## String Complexity

Strings in Python are immutable sequences of characters.

### Time Complexity

| Operation | Average Case | Worst Case | Notes |
|-----------|-------------|------------|-------|
| `s[i]` | O(1) | O(1) | Character access |
| `s[i:j]` | O(k) | O(k) | Slice, k = j-i |
| `s + t` | O(n + m) | O(n + m) | Concatenation |
| `s * n` | O(n * len(s)) | O(n * len(s)) | Repetition |
| `s.find(sub)` | O(n * m) | O(n * m) | Find substring |
| `s.index(sub)` | O(n * m) | O(n * m) | Like find but raises |
| `s.replace(old, new)` | O(n * m) | O(n * m) | Replace |
| `s.split()` | O(n) | O(n) | Split on whitespace |
| `s.split(sep)` | O(n) | O(n) | Split on separator |
| `sep.join(list)` | O(n) | O(n) | Join strings |
| `s.strip()` | O(n) | O(n) | Remove whitespace |
| `s.upper()` / `s.lower()` | O(n) | O(n) | Case conversion |
| `s.startswith(sub)` | O(m) | O(m) | m = len(sub) |
| `s in t` | O(n * m) | O(n * m) | Substring check |

### Space Complexity
- **String creation**: O(n)
- **Each operation creates new string**: O(n) due to immutability

### Important Notes
1. Strings are immutable - every operation creates a new string
2. Use list + join for efficient string building
3. For pattern matching, use regex or specialized algorithms

---

## Tuple Complexity

Tuples are immutable sequences, similar to lists but optimized for small memory footprint.

### Time Complexity

| Operation | Average Case | Worst Case | Notes |
|-----------|-------------|------------|-------|
| `t[i]` | O(1) | O(1) | Index access |
| `t[i:j]` | O(k) | O(k) | Slice |
| `x in t` | O(n) | O(n) | Membership (linear) |
| `t.count(x)` | O(n) | O(n) | Count occurrences |
| `t.index(x)` | O(n) | O(n) | Find index |

### Space Complexity
- **Tuple creation**: O(n)
- **Less overhead than list**: ~48 bytes vs ~64 bytes for list

### Important Notes
1. Tuples are immutable - can be used as dict keys
2. Tuple unpacking is efficient and idiomatic
3. Namedtuples for lightweight objects
4. Can be used with *args and **kwargs

---

## Heap Operations

Python's heapq module provides heap operations on lists.

### Time Complexity

| Operation | Complexity | Notes |
|-----------|------------|-------|
| `heapify(list)` | O(n) | Build heap from list |
| `heappush(heap, x)` | O(log n) | Add element |
| `heappop(heap)` | O(log n) | Remove smallest |
| `heappushpop(heap, x)` | O(log n) | Push then pop |
| `heapreplace(heap, x)` | O(log n) | Pop then push |
| `heapq.nlargest(k, heap)` | O(n log k) | k largest elements |
| `heapq.nsmallest(k, heap)` | O(n log k) | k smallest elements |

### Space Complexity
- O(n) for heap storage

---

## Common Operations Comparison

### Membership Testing
```python
# List: O(n) - linear search
if x in my_list: pass

# Set: O(1) - hash table
if x in my_set: pass

# Dict: O(1) - hash table (checks keys)
if x in my_dict: pass

# String: O(n * m) - substring search
if sub in string: pass
```

### Finding Index
```python
# List: O(n)
idx = my_list.index(x)  # Raises if not found

# String: O(n * m)
idx = string.find(sub)  # Returns -1 if not found
```

### Deduplication
```python
# Using set - O(n), loses order
unique = list(set(items))

# Using dict - O(n), preserves order (Python 3.7+)
unique = list(dict.fromkeys(items))

# Using list comprehension - O(n^2), preserves order
unique = []
[unique.append(x) for x in items if x not in unique]
```

### Sorting
```python
# List sort: O(n log n), in-place
my_list.sort()

# Sorted: O(n log n), returns new list
sorted_list = sorted(my_list)

# Reverse sorted: O(n log n)
sorted_list = sorted(my_list, reverse=True)

# Custom key: O(n log n)
sorted_list = sorted(my_list, key=lambda x: x['name'])
```

---

## Interview Tips

### 1. Choose the Right Data Structure

| Need | Best Choice | Why |
|------|-------------|-----|
| Fast lookup by key | dict | O(1) average |
| Fast membership test | set | O(1) average |
| Ordered unique elements | dict or set | O(1) insertion |
| Frequent insert/delete at ends | collections.deque | O(1) |
| Sorted stream of elements | heapq | O(log n) insertion |
| Immutable sequence | tuple | Hashable, lighter |

### 2. Common Performance Mistakes

1. **Using list for membership testing**: Use set instead
   ```python
   # Slow: O(n)
   if item in large_list:

   # Fast: O(1)
   if item in large_set:
   ```

2. **String concatenation in loop**: Use list + join
   ```python
   # Slow: O(n^2)
   result = ""
   for s in strings:
       result += s

   # Fast: O(n)
   result = "".join(strings)
   ```

3. **Using list for stack operations at front**: Use deque
   ```python
   # Slow: O(n)
   my_list.insert(0, item)
   my_list.pop(0)

   # Fast: O(1)
   from collections import deque
   my_deque.appendleft(item)
   my_deque.popleft()
   ```

### 3. Complexity in Built-in Functions

| Function | Complexity | Notes |
|----------|-------------|-------|
| `len(collection)` | O(1) | - |
| `min(collection)` | O(n) | - |
| `max(collection)` | O(n) | - |
| `sum(collection)` | O(n) | - |
| `enumerate(collection)` | O(1)* | *Creation, iteration is O(n) |
| `zip(a, b)` | O(min(len(a), len(b))) | - |
| `reversed(collection)` | O(1)* | *Creation, iteration is O(n) |

### 4. When to Optimize

1. **Profile first**: Don't guess, measure
2. **Focus on bottlenecks**: Optimize the loops that run most
3. **Consider input size**: O(n) might be fine for small n
4. **Trade-offs**: Sometimes readability beats micro-optimization

---

## Summary

| Data Structure | Access | Search | Insert | Delete | Space |
|---------------|--------|--------|--------|--------|-------|
| List | O(1) | O(n) | O(1)* | O(n) | O(n) |
| Dict | O(1) | O(1)** | O(1)** | O(1)** | O(n) |
| Set | N/A | O(1)** | O(1)** | O(1)** | O(n) |
| String | O(1) | O(n*m) | N/A | N/A | O(n) |
| Tuple | O(1) | O(n) | N/A | N/A | O(n) |
| Heap | N/A | O(1)*** | O(log n) | O(log n) | O(n) |

*Amortized
**Average case
***Peek only (min/max)

---

## Practice Problems

- [x] Implement LRU cache with O(1) operations
- [x] Find most frequent element using different methods
- [x] Compare performance of list vs set for membership
- [x] Implement word frequency counter efficiently
- [x] Find kth smallest element using heap
