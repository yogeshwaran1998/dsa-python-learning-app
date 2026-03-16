# Two Pointers - Theory Guide

## Table of Contents
1. [Introduction](#introduction)
2. [Types of Two Pointers](#types-of-two-pointers)
3. [Common Problems](#common-problems)
4. [Time and Space Complexity](#time-and-space-complexity)
5. [Interview Tips](#interview-tips)
6. [Practice Problems](#practice-problems)

---

## Introduction

Two Pointers is a powerful algorithmic technique that uses two pointers to solve array/string problems efficiently. The pointers can move in the same direction or in opposite directions, depending on the problem requirements.

### Why Use Two Pointers?
- Reduces time complexity from O(n^2) to O(n)
- Uses O(1) extra space (in-place)
- Leverages sorted/ordered input
- Common in FAANG interviews

---

## Types of Two Pointers

### 1. Opposite Direction (Converging)
Two pointers start at opposite ends and move toward each other.

**Use Cases:**
- Finding pair with target sum in sorted array
- Checking if string is palindrome
- Finding container with most water

**Example:**
```
Array: [1, 2, 3, 4, 5], Target: 6
Left=0 (1), Right=4 (5) -> 1+5=6 -> Found!
```

### 2. Same Direction (Parallel)
Two pointers both start from the beginning, with one moving faster (fast-slow pattern).

**Use Cases:**
- Removing duplicates from sorted array
- Partitioning arrays
- Finding missing numbers

**Example:**
```
Array: [1,1,1,2,2,3]
Slow tracks position of next unique element
Fast iterates through array
```

---

## Common Problems

### Problem 1: Remove Duplicates from Sorted Array
Given a sorted array, remove duplicates in-place.

**Approach:**
- Use slow pointer to track position
- Fast pointer scans array
- When different element found, copy to slow position

**Example:**
```
Input: [1,1,2,2,2,3]
Output: elements: 3 (unique [1,2,3])
```

### Problem 2: 3Sum
Find all unique triplets that sum to zero.

**Approach:**
- Sort the array
- Fix one element, use two pointers for remaining
- Avoid duplicates by skipping equal elements

**Example:**
```
Input: [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
```

### Problem 3: Container With Most Water
Find container that holds most water between vertical lines.

**Approach:**
- Two pointers at ends
- Move smaller height pointer inward
- Track max area

**Example:**
```
Input: [1,8,6,2,5,4,8,3,7]
Output: 49 (between indices 1 and 8)
```

---

## Time and Space Complexity

| Problem | Time | Space |
|---------|------|-------|
| Remove Duplicates | O(n) | O(1) |
| 3Sum | O(n^2) | O(1) or O(n) for results |
| Container With Most Water | O(n) | O(1) |
| Valid Palindrome | O(n) | O(1) |
| Two Sum II (sorted) | O(n) | O(1) |

---

## Interview Tips

### Before Writing Code
1. Ask if array is sorted - determines approach
2. Clarify if in-place modification required
3. Check for duplicate handling requirements

### Common Edge Cases
- Empty array
- Single element
- All same elements
- Negative numbers
- Very large arrays

### Two Pointers Checklist
- [ ] Are pointers properly initialized?
- [ ] When to move each pointer?
- [ ] How to handle duplicates?
- [ ] What are termination conditions?

### Follow-up Questions
- "Can you do it in O(1) space?"
- "How would you handle duplicates?"
- "What if the array is not sorted?"

---

## Summary

Two Pointers is essential for:
- Sorted array problems
- Palindrome checking
- Pair finding with target sum
- In-place modifications

**Key Insight:** When input is sorted, two pointers from ends often gives O(n). When removing elements, slow-fast pattern gives O(n).

---

## Practice Problems

### Easy
- Valid Palindrome
- Remove Duplicates from Sorted Array
- Two Sum II - Input array is sorted

### Medium
- 3Sum
- 3Sum Closest
- Container With Most Water
- Subarray Product Less Than K

### Hard
- Trapping Rain Water
- Minimum Window Substring
- Longest Substring with At Most Two Distinct Characters
