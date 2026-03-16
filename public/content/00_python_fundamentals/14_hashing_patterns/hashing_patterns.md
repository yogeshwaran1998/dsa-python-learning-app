# Hashing Patterns - Theory Guide

## Table of Contents
1. [Introduction](#introduction)
2. [Frequency Counting](#frequency-counting)
3. [Two Sum Problem](#two-sum-problem)
4. [Anagram Detection](#anagram-detection)
5. [Custom Keys](#custom-keys)
6. [Common Problems](#common-problems)
7. [Time and Space Complexity](#time-and-space-complexity)
8. [Interview Tips](#interview-tips)
9. [Practice Problems](#practice-problems)

---

## Introduction

Hashing uses hash functions to map data to fixed-size values. In algorithmic problems, hash tables (dictionaries in Python) provide O(1) average-case lookup, making them essential for solving many problems efficiently.

### Why Use Hashing?
- O(1) average lookup time
- Solve problems impossible with arrays alone
- Essential for many interview patterns
- Handles duplicates efficiently

### When to Use
- Counting frequencies
- Finding pairs/triples with target sum
- Detecting anagrams
- Caching/memoization
- Removing duplicates

---

## Frequency Counting

### Concept
Use hashmap to count occurrences of each element.

### Implementation
```python
from collections import Counter
counts = Counter(arr)  # Automatic frequency counting
```

### Use Cases
- Finding most common elements
- Checking if duplicates exist
- Grouping by frequency

---

## Two Sum Problem

### Classic Problem
Find two numbers that add up to target.

### Approach
1. Iterate through array
2. For each number, check if (target - number) exists
3. Store numbers seen so far

### Variations
- Return indices (most common)
- Return values
- Multiple pairs
- Three sum, Four sum

---

## Anagram Detection

### Concept
An anagram has same characters with same frequencies.

### Methods
1. **Sort and compare**: Sort both strings, compare
2. **Character count**: Count frequency of each character

### Use Cases
- Valid anagrams
- Group anagrams
- Find anagram pairs

---

## Custom Keys

### Tuples as Keys
Multiple values can form composite keys.

### Examples
- Position-based: (row, col)
- Character count: tuple of 26 counts
- Frequency pattern: tuple of counts sorted

### Benefits
- Complex lookups
- Multi-dimensional problems

---

## Common Problems

### Problem 1: Contains Duplicate
Check if array contains duplicates.

**Approach:**
- Use set for O(1) lookup
- Or use Counter

**Example:**
```
Input: [1,2,3,1]
Output: True
```

### Problem 2: Valid Anagram
Check if two strings are anagrams.

**Approach:**
- Count characters in both
- Compare counts

**Example:**
```
Input: s = "anagram", t = "nagaram"
Output: True
```

### Problem 3: Group Anagrams
Group strings by anagram signature.

**Approach:**
- Create signature (sorted chars or char count tuple)
- Use dictionary to group

**Example:**
```
Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat","tea","ate"], ["tan","nat"], ["bat"]]
```

### Problem 4: Longest Consecutive Sequence
Find length of longest consecutive sequence.

**Approach:**
- Put all numbers in set
- For each number, check if start of sequence
- Count consecutive

**Example:**
```
Input: [100, 4, 200, 1, 3, 2]
Output: 4 (sequence: 1,2,3,4)
```

---

## Time and Space Complexity

| Operation | Average | Worst |
|-----------|---------|-------|
| Insert | O(1) | O(n) |
| Lookup | O(1) | O(n) |
| Delete | O(1) | O(n) |

| Problem | Time | Space |
|---------|------|-------|
| Two Sum | O(n) | O(n) |
| Frequency Count | O(n) | O(n) |
| Group Anagrams | O(n*k*logk) | O(n*k) |
| Valid Anagram | O(n) | O(1) |

---

## Interview Tips

### Key Questions to Ask
1. Are there negative numbers?
2. What is the data type of elements?
3. Should we return indices or values?
4. How to handle duplicates?

### Common Edge Cases
- Empty array/string
- Single element
- No solution exists
- Multiple valid answers

### Hashing Checklist
- [ ] Use appropriate data structure (set, dict, Counter)
- [ ] Handle edge cases
- [ ] Consider space vs time trade-off
- [ ] Watch for hash collisions in interviews (usually not an issue in Python)

### Follow-up Questions
- "How would you handle large inputs?"
- "What if multiple pairs exist?"
- "Can you do it with O(1) space?"

---

## Summary

Hashing is essential for:
- O(1) lookups and insertions
- Frequency counting and grouping
- Finding pairs/triples with target sums
- Anagram detection and grouping
- Caching and memoization

**Key Insight:** Hash tables trade space for time. Use when you need fast lookups or have complex key requirements.

---

## Practice Problems

### Easy
- Contains Duplicate
- Valid Anagram
- Intersection of Two Arrays
- First Unique Character

### Medium
- Group Anagrams
- Top K Frequent Elements
- Longest Consecutive Sequence
- Valid Sudoku

### Hard
- LRU Cache
- Find All Anagrams in a String
- Word Search II
- Minimum Window Substring
