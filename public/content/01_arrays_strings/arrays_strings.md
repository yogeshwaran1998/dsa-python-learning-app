# Arrays and Strings - Theory Guide

## Table of Contents
1. [Arrays](#arrays)
2. [Strings](#strings)
3. [Common Patterns](#common-patterns)
4. [Interview Tips](#interview-tips)

---

## Arrays

### What is an Array?
An array is a contiguous memory data structure that stores elements of the same type at sequential memory locations. It provides O(1) random access by index.

### Key Properties
- **Contiguous Memory**: Elements stored in adjacent memory locations
- **Fixed Size** (in most languages): Size must be known at compile time
- **Zero-Indexed**: First element at index 0
- **Homogeneous**: All elements are of the same type

### Time Complexity

| Operation | Average Case | Worst Case |
|-----------|--------------|-------------|
| Access by index | O(1) | O(1) |
| Search (linear) | O(n) | O(n) |
| Search (binary) | O(log n) | O(log n) |
| Insert at end | O(1) | O(1) |
| Insert at beginning | O(n) | O(n) |
| Delete at end | O(1) | O(1) |
| Delete at beginning | O(n) | O(n) |

### Python Specifics
- Python lists are dynamic arrays (resize automatically)
- Underlying implementation uses dynamic array (cpython list)
- Resize happens at ~0.63x and ~1.125x growth factor

### When to Use Arrays
- Need O(1) random access
- Fixed number of elements known in advance
- Need memory locality for cache efficiency
- Iterating over elements frequently

---

## Strings

### What is a String?
A string is a sequence of characters. In most languages, strings are immutable. Python strings are immutable (cannot be changed after creation).

### String Operations Complexity

| Operation | Time Complexity |
|-----------|-----------------|
| Access by index | O(1) |
| Search (linear) | O(n) |
| Concatenation | O(n) |
| Substring | O(k) where k is substring length |
| Slice | O(k) |

### String Immutability Benefits
1. **Thread Safety**: Cannot be modified by multiple threads
2. **Hashing**: Can be safely used as dictionary keys
3. **String Pooling**: Enables interning for memory optimization
4. **Security**: Cannot be modified after creation

### When to Use Strings
- Text processing and manipulation
- Pattern matching
- Building strings incrementally (use list + join for efficiency)

---

## Common Patterns

### 1. Two Pointers
Use two pointers moving in opposite or same direction.

**When to use:**
- Finding pairs that satisfy condition
- Partitioning arrays
- Removing duplicates in-place

### 2. Sliding Window
Maintain a window that slides through the data.

**When to use:**
- Subarray/substring problems
- Finding maximum/minimum sum of k consecutive elements
- String permutations

**Types:**
- Fixed window size
- Variable window size (expand/shrink based on condition)

### 3. Prefix Sum
Pre-compute cumulative sums for fast range queries.

**When to use:**
- Range sum queries
- Subarray problems with specific sum

### 4. kadane's Algorithm
Find maximum subarray sum.

**When to use:**
- Maximum sum contiguous subarray
- Problems with "maximum/minimum subarray"

### 5. Cyclic Sort
Place elements in their correct positions.

**When to use:**
- Array contains numbers from 1 to n
- Finding missing/duplicate numbers

---

## Interview Tips

### Before Writing Code
1. **Clarify the problem**: Ask about constraints, input size, edge cases
2. **Think about approaches**: Brute force → optimized
3. **Choose the right approach**: Consider time/space trade-offs

### Common Edge Cases to Check
1. Empty array/string
2. Single element
3. All same elements
4. Negative numbers
5. Very large inputs (overflow considerations)
6. Duplicates vs no duplicates

### FAANG-Specific Expectations
1. **Optimal Time Complexity**: They expect O(n) or O(log n) solutions
2. **Space Optimization**: Often expect O(1) space for array problems
3. **Edge Case Handling**: Must handle all edge cases
4. **Clean Code**: Readable variable names, proper comments
5. **Testing**: Walk through examples, edge cases

### Red Flags
- Using built-in functions without understanding complexity
- Not considering space complexity
- Missing edge cases
- Not testing the solution mentally

### Follow-up Questions
- "Can you optimize further?"
- "What if the input is sorted?"
- "How would you handle this with O(1) space?"
- "What about negative numbers?"

---

## Practice Problems

### Easy
- [x] Two Sum
- [x] Best Time to Buy and Sell Stock
- [x] Contains Duplicate
- [x] Product of Array Except Self
- [x] Maximum Subarray

### Medium
- [x] 3Sum
- [x] Container With Most Water
- [x] Longest Substring Without Repeating Characters
- [x] Minimum Window Substring
- [x] Longest Repeating Character Replacement

### Hard
- [x] First Missing Positive
- [x] Merge Intervals
- [x] Trapping Rain Water
- [x] Minimum Window Substring (Hard)

---

## Summary

| Pattern | Use Case | Time | Space |
|---------|----------|------|-------|
| Two Pointers | Pair finding | O(n) | O(1) |
| Sliding Window | Subarray/substring | O(n) | O(1) or O(k) |
| Prefix Sum | Range queries | O(n) | O(n) |
| Kadane | Max subarray | O(n) | O(1) |
| Cyclic Sort | 1 to n elements | O(n) | O(1) |
