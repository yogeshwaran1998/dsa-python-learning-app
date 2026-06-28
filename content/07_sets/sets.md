# Sets - Theory Guide

## Table of Contents
1. [What is a Set?](#what-is-a-set)
2. [Time Complexity](#time-complexity)
3. [Python Set Operations](#python-set-operations)
4. [Common Patterns](#common-patterns)
5. [Interview Tips](#interview-tips)

---

## What is a Set?

A set is an unordered collection of unique elements. Unlike lists, sets don't allow duplicates.

### Key Properties
- **Unordered**: No guaranteed order of elements
- **Unique**: No duplicate elements
- **Mutable**: Can add/remove elements
- **Hashable elements**: Elements must be hashable (immutable)

---

## Time Complexity

| Operation | Average | Worst Case |
|-----------|---------|------------|
| Add | O(1) | O(n) |
| Remove | O(1) | O(n) |
| Contains | O(1) | O(n) |
| Union | O(n + m) | O(n + m) |
| Intersection | O(min(n,m)) | O(n*m) |
| Difference | O(n) | O(n*m) |

---

## Python Set Operations

### Basic Operations
- `add(x)` - Add element
- `remove(x)` - Remove element (raises error if missing)
- `discard(x)` - Remove element (doesn't raise error)
- `clear()` - Remove all elements
- `x in set` - Membership check
- `len(set)` - Get size

### Set Operations
- `set1 | set2` or `set1.union(set2)` - Union
- `set1 & set2` or `set1.intersection(set2)` - Intersection
- `set1 - set2` or `set1.difference(set2)` - Difference
- `set1 ^ set2` or `set1.symmetric_difference(set2)` - Symmetric difference

---

## Common Patterns

### 1. Deduplication
Quickly remove duplicates.

### 2. Membership Checking
O(1) lookup.

### 3. Set Intersection
Find common elements.

### 4. Two Pointers with Sets
Find pairs/sums.

---

## Interview Tips

### FAANG Expectations
1. **Know all operations**
2. **Understand when to use set vs dict**
3. **Space complexity awareness**

### Common Mistakes
1. Using mutable elements (lists as set elements)
2. Assuming order (sets are unordered)
3. Not handling missing elements properly

---

## Practice Problems

### Easy
- [x] Contains Duplicate
- [x] Single Number
- [x] Intersection of Two Arrays

### Medium
- [x] Intersection of Multiple Arrays
- [x] Find Common Elements in Rows
