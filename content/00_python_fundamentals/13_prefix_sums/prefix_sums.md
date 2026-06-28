# Prefix Sums - Theory Guide

## Table of Contents
1. [Introduction](#introduction)
2. [1D Prefix Sums](#1d-prefix-sums)
3. [2D Prefix Sums](#2d-prefix-sums)
4. [Range Sum Queries](#range-sum-queries)
5. [Common Problems](#common-problems)
6. [Time and Space Complexity](#time-and-space-complexity)
7. [Interview Tips](#interview-tips)
8. [Practice Problems](#practice-problems)

---

## Introduction

Prefix Sums is a technique for pre-computing cumulative sums to answer range sum queries efficiently. By preprocessing the array into a prefix sum array, we can answer any range sum query in O(1) time.

### Why Use Prefix Sums?
- Convert O(n) per query to O(1) per query
- Useful when there are many queries
- Foundation for 2D prefix sums
- Common in FAANG interviews

### When to Use
- Multiple range sum queries
- Subarray sum problems
- 2D matrix sum queries
- Finding subarrays with specific sums

---

## 1D Prefix Sums

### Concept
Prefix sum at index i = sum of all elements from index 0 to i (inclusive).

### Construction
```text
Array:     [1, 2, 3, 4, 5]
Prefix:    [1, 3, 6, 10, 15]
           ↑  ↑  ↑   ↑   ↑
           0  1  2   3   4  (indices)
```

### Formula
```text
prefix[i] = prefix[i-1] + arr[i]
```

### Range Sum Query
```text
Sum from index l to r = prefix[r] - prefix[l-1]
                         (or prefix[r] if l=0)
```

---

## 2D Prefix Sums

### Concept
Extend prefix sums to 2D matrices. Each cell stores sum of all elements in rectangle from (0,0) to (i,j).

### Construction
```text
Matrix:
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]

Prefix Sum Matrix:
[1,  3,  6]
[5,  12, 21]
[12, 27, 45]
```

### Formula
```text
prefix[i][j] = matrix[i][j] +
               prefix[i-1][j] +
               prefix[i][j-1] -
               prefix[i-1][j-1]
```

### Rectangle Sum Query
For rectangle from (r1,c1) to (r2,c2):
```text
Sum = prefix[r2][c2] -
      prefix[r1-1][c2] -
      prefix[r2][c1-1] +
      prefix[r1-1][c1-1]
```

---

## Common Problems

### Problem 1: Range Sum Query - Immutable
Answer range sum queries on static array.

**Approach:**
- Build prefix sum array
- Answer each query in O(1)

**Example:**
```text
Input: nums = [-2, 0, 3, -5, 2, -1]
Query: sumRange(0, 2) = 1
Query: sumRange(2, 5) = -1
```

### Problem 2: Subarray Sum Equals K
Find number of subarrays with sum equal to k.

**Approach:**
- Use prefix sum and hashmap
- Store counts of prefix sums seen
- For each prefix, check if (prefix - k) exists

### Problem 3: Matrix Block Sum
Calculate sum of elements in k x k submatrices.

**Approach:**
- Build 2D prefix sum
- For each cell, calculate k-neighborhood sum

---

## Time and Space Complexity

| Operation | Time | Space |
|-----------|------|-------|
| Build 1D prefix | O(n) | O(n) |
| 1D range query | O(1) | O(1) |
| Build 2D prefix | O(m*n) | O(m*n) |
| 2D range query | O(1) | O(1) |
| Subarray sum k | O(n) | O(n) |

---

## Interview Tips

### Key Questions to Ask
1. Is the array/matrix mutable?
2. How many queries will be made?
3. Are there any constraints on indices?
4. Should we handle negative numbers?

### Common Edge Cases
- Empty array/matrix
- Single element
- Query range equals entire array
- Negative numbers in array

### Prefix Sum Checklist
- [ ] Properly initialize prefix array
- [ ] Handle 0-index vs 1-index
- [ ] Account for boundary conditions
- [ ] Use long for large sums (Python handles big integers)

### Follow-up Questions
- "How would you handle updates to the array?"
- "What if queries are offline vs online?"
- "Can you do it with O(1) space?"

---

## Summary

Prefix Sums is essential for:
- Multiple range sum queries
- Subarray problems with specific sums
- 2D matrix range queries
- Cumulative frequency problems

**Key Insight:** Precompute prefix array in O(n), answer each query in O(1). Trade-off: O(n) space for O(1) query time.

---

## Practice Problems

### Easy
- Range Sum Query - Immutable
- Running Sum of 1d Array
- Maximum Average Subarray I

### Medium
- Subarray Sum Equals K
- Number of Subarrays with Bounded Maximum
- Matrix Block Sum
- 2D Matrix Queries

### Hard
- Range Sum Query 2D - Mutable
- Count of Range Sum
- Maximum Sum Circular Subarray
