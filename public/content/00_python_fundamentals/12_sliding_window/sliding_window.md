# Sliding Window - Theory Guide

## Table of Contents
1. [Introduction](#introduction)
2. [Types of Sliding Windows](#types-of-sliding-windows)
3. [Deque Implementation](#deque-implementation)
4. [Common Problems](#common-problems)
5. [Time and Space Complexity](#time-and-space-complexity)
6. [Interview Tips](#interview-tips)
7. [Practice Problems](#practice-problems)

---

## Introduction

Sliding Window is a technique used to perform operations on a specific window size of an array or string. The window "slides" as we move through the data, allowing us to process elements in chunks without re-computing from scratch.

### Why Use Sliding Window?
- Reduces nested loops from O(n^2) to O(n)
- Efficient for substring/subarray problems
- Common pattern in FAANG interviews
- Works well with streaming data

### When to Use
- Finding subarrays/substrings with certain properties
- Maximum/minimum sum of k consecutive elements
- Longest substring with certain characteristics
- Average of all subarrays of size k

---

## Types of Sliding Windows

### 1. Fixed Window Size
Window size is predetermined and doesn't change.

**Algorithm:**
1. Calculate sum of first k elements
2. Slide window by removing leftmost and adding next element
3. Track maximum/minimum during slide

**Use Cases:**
- Maximum sum of k consecutive elements
- Average of k-sized subarrays

### 2. Variable Window Size
Window size expands and contracts based on conditions.

**Algorithm:**
1. Expand window by moving right pointer
2. Shrink window from left when condition violated
3. Track answer during expansion

**Use Cases:**
- Longest substring without repeating characters
- Minimum size subarray with sum >= target

### 3. Sliding Window with Deque
Use deque to maintain useful elements in window.

**Use Cases:**
- Maximum in each window
- Minimum in each window
- Monotonic decreasing/increasing queues

---

## Common Problems

### Problem 1: Longest Substring Without Repeating Characters
Find length of longest substring without repeating characters.

**Approach:**
- Use variable sliding window
- Use set/hash to track characters in window
- Shrink window when duplicate found

**Example:**
```
Input: "abcabcbb"
Output: 3 ("abc")
```

### Problem 2: Minimum Window Substring
Find minimum window containing all characters of pattern.

**Approach:**
- Expand window to include all pattern characters
- Shrink window while still valid
- Track minimum window

**Example:**
```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
```

### Problem 3: Maximum Sliding Window
Find maximum element in each sliding window.

**Approach:**
- Use monotonic decreasing deque
- Maintain elements in decreasing order
- Remove elements outside window

**Example:**
```
Input: [1,3,-1,-3,5,3,6,7], k=3
Output: [3,3,5,5,6,7]
```

---

## Deque-Based Sliding Window

### Monotonic Deque Pattern
Maintain elements in sorted order within deque.

**For Maximum:**
- Keep deque in decreasing order
- Front always has maximum
- Remove elements smaller than current (they can't be max)

**For Minimum:**
- Keep deque in increasing order
- Front always has minimum
- Remove elements larger than current (they can't be min)

### Benefits
- O(n) time instead of O(n*k) for naive approach
- Each element added/removed at most once

---

## Time and Space Complexity

| Problem | Time | Space |
|---------|------|-------|
| Max Sum Subarray (fixed k) | O(n) | O(1) |
| Longest Substring (no repeat) | O(n) | O(min(m,n)) |
| Minimum Window Substring | O(n+m) | O(m) |
| Max Sliding Window (deque) | O(n) | O(k) |
| Min Sliding Window (deque) | O(n) | O(k) |

---

## Interview Tips

### Key Questions to Ask
1. Are characters/elements unique in the input?
2. Is window size fixed or variable?
3. Should we return count or actual substring?
4. How to handle empty inputs?

### Common Edge Cases
- Empty string/array
- Window size larger than array
- All same elements
- Single character string
- Pattern not found in string

### Sliding Window Checklist
- [ ] Properly initialize window boundaries
- [ ] Handle window expansion and shrinking
- [ ] Update answer at each step
- [ ] Handle edge cases (small arrays)

### Follow-up Questions
- "Can you do it without extra space?"
- "How would you handle Unicode?"
- "What if window size is 1?"

---

## Summary

Sliding Window is essential for:
- Substring/subarray problems
- Finding patterns in sequences
- Aggregate operations on windows

**Key Insight:** Fixed window is simpler (O(n)), variable window handles more complex conditions (also O(n)). Deque gives O(n) for sliding window min/max.

---

## Practice Problems

### Easy
- Maximum Average Subarray I
- Number of Subarrays with Bounded Maximum
- Max Consecutive Ones
- Maximum Number of Vowels in a Substring

### Medium
- Longest Substring Without Repeating Characters
- Minimum Size Subarray Sum
- Fruit Into Baskets
- Longest Repeating Character Replacement

### Hard
- Minimum Window Substring
- Sliding Window Maximum
- Substring with Concatenation of All Words
- Minimum Window Subsequence
