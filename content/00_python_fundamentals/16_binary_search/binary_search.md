# Binary Search - Theory Guide

## Table of Contents
1. [Introduction](#introduction)
2. [Standard Binary Search](#standard-binary-search)
3. [Lower and Upper Bounds](#lower-and-upper-bounds)
4. [Bisect Module](#bisect-module)
5. [Search in Rotated Array](#search-in-rotated-array)
6. [Common Problems](#common-problems)
7. [Time and Space Complexity](#time-and-space-complexity)
8. [Interview Tips](#interview-tips)
9. [Practice Problems](#practice-problems)

---

## Introduction

Binary Search is an efficient algorithm for finding an element in a sorted array. It works by repeatedly dividing the search interval in half, achieving O(log n) time complexity.

### Why Use Binary Search?
- O(log n) time complexity vs O(n) for linear search
- Essential for large datasets
- Foundation for many advanced algorithms
- Common in FAANG interviews

### Prerequisites
- Data must be sorted (or have some monotonic property)
- Random access to elements (array)

---

## Standard Binary Search

### Algorithm
1. Set left = 0, right = n - 1
2. While left <= right:
   - Calculate mid = left + (right - left) // 2 (avoid overflow)
   - If arr[mid] == target: return mid
   - If arr[mid] < target: left = mid + 1
   - Else: right = mid - 1
3. Return -1 (not found)

### Key Points
- Use `left + (right - left) // 2` to avoid integer overflow
- Decide on left <= right vs left < right based on problem
- Handle edge cases properly

---

## Lower and Upper Bounds

### Lower Bound
Find first index where arr[i] >= target (or arr[i] > target).

**Algorithm:**
- Binary search continues even after finding target
- Move right when arr[mid] >= target

### Upper Bound
Find first index where arr[i] > target.

**Algorithm:**
- Similar to lower bound
- Move right when arr[mid] > target

### Use Cases
- Lower bound: First occurrence
- Upper bound: Last occurrence + 1

---

## Bisect Module

Python's `bisect` module provides binary search functions.

```python
import bisect

# bisect_left(a, x) - leftmost position
# bisect_right(a, x) - rightmost position + 1
```

### Functions
- `bisect_left(a, x)`: Insert x in sorted array a, maintaining order
- `bisect_right(a, x)`: Same but for rightmost insertion
- `bisect(a, x)`: Alias for bisect_right

---

## Search in Rotated Array

### Problem
Array is rotated at pivot point. Find target.

### Approach
Modified binary search that checks which half is sorted.

### Algorithm
1. Find mid point
2. Check if left half is sorted:
   - If target in range [left, mid): search left
   - Else: search right
3. Same logic for right half

### Key Insight
At least one half of the array is always sorted.

---

## Common Problems

### Problem 1: Search in Rotated Array
Search in sorted but rotated array.

**Example:**
```text
Input: [4,5,6,7,0,1,2], target = 0
Output: 4 (index of 0)
```

### Problem 2: Find Minimum in Rotated Array
Find minimum element in rotated sorted array.

**Example:**
```text
Input: [4,5,6,7,0,1,2]
Output: 0
```

### Problem 3: Find Peak Element
Find a peak element (greater than neighbors).

**Example:**
```text
Input: [1,2,3,1]
Output: 2 (index of 3)
```

### Problem 4: Find First and Last Position
Find first and last position of target.

**Example:**
```text
Input: [5,7,7,8,8,10], target = 8
Output: [3, 4]
```

---

## Time and Space Complexity

| Operation | Time | Space |
|-----------|------|-------|
| Standard Binary Search | O(log n) | O(1) |
| Lower/Upper Bound | O(log n) | O(1) |
| Search Rotated Array | O(log n) | O(1) |
| Find Minimum in Rotated | O(log n) | O(1) |

---

## Interview Tips

### Key Questions to Ask
1. Is the array sorted?
2. Are there duplicates?
3. Should we return index or -1 if not found?
4. What if array is empty?

### Common Edge Cases
- Empty array
- Single element
- Target at edges
- All elements same
- No rotation (normal sorted array)

### Binary Search Checklist
- [ ] Use `left + (right - left) // 2` to avoid overflow
- [ ] Choose correct termination condition (<= or <)
- [ ] Update pointers correctly (mid + 1 or mid - 1)
- [ ] Handle duplicates properly

### Follow-up Questions
- "How to handle duplicates?"
- "What if array is rotated k times?"
- "Can you do it recursively?"

---

## Summary

Binary Search is essential for:
- Finding elements in sorted arrays
- Monotonic function problems
- Finding boundaries
- Search in rotated arrays

**Key Insight:** Binary search reduces search space by half each iteration. O(log n) is extremely fast - can search 1 billion elements in just 30 comparisons.

---

## Practice Problems

### Easy
- Binary Search
- First Bad Version
- Search Insert Position
- Squares of Sorted Array

### Medium
- Search in Rotated Array
- Find First and Last Position
- Search in Rotated Array II
- Find Minimum in Rotated Array

### Hard
- Median of Two Sorted Arrays
- Find Minimum in Rotated Array II
- Search in Rotated Array II
- Count of Range Sum
