# Hash Tables - Theory Guide

## Table of Contents
1. [What is a Hash Table?](#what-is-a-hash-table)
2. [Time Complexity](#time-complexity)
3. [Hash Functions](#hash-functions)
4. [Collision Resolution](#collision-resolution)
5. [Common Patterns](#common-patterns)
6. [Interview Tips](#interview-tips)

---

## What is a Hash Table?

A hash table (or hash map) is a data structure that implements an associative array. It uses a hash function to compute an index into an array of buckets or slots, from which the desired value can be found.

### Key Components
- **Hash Function**: Converts keys to array indices
- **Buckets**: Array slots storing key-value pairs
- **Collision Resolution**: Handling multiple keys mapping to same index

### Visual Representation

A hash function maps a key to a bucket index in O(1), where its value is stored.

<div class="dsa-diagram dsa-diagram--center">
  <div class="dnode"><span class="dcell dcell--label">key</span><span class="dcell">"apple"</span></div>
  <span class="darrow">&rarr;</span>
  <div class="dnode dnode--highlight"><span class="dcell">hash()</span></div>
  <span class="darrow">&rarr;</span>
  <div class="dnode"><span class="dcell dcell--label">index</span><span class="dcell">3</span></div>
  <span class="darrow">&rarr;</span>
  <div class="dnode dnode--green"><span class="dcell">fruit data</span></div>
  <div class="dsa-caption">key &rarr; hash function &rarr; bucket index &rarr; stored value.</div>
</div>

---

## Time Complexity

| Operation | Average | Worst Case |
|-----------|---------|------------|
| Insert | O(1) | O(n) |
| Delete | O(1) | O(n) |
| Search | O(1) | O(n) |
| Get | O(1) | O(n) |

**Worst case** occurs when all keys hash to the same bucket (hash collision attack).

---

## Hash Functions

A good hash function should:
1. **Uniform distribution**: Distribute keys evenly across buckets
2. **Deterministic**: Same key always produces same hash
3. **Fast computation**: O(1) to compute

### Common Hash Functions
- **Division**: h(k) = k mod m
- **Multiplication**: h(k) = floor(m * (k * A mod 1))
- **Universal Hashing**: Randomize hash function

---

## Collision Resolution

### 1. Chaining (Separate Linked List)
Each bucket stores a linked list of all elements that hash to that index.

**Pros:**
- Simple to implement
- No size limitations
- Easy to delete

**Cons:**
- Memory overhead for pointers
- Performance degrades with many collisions

### 2. Open Addressing
All elements stored in bucket array itself.

**Methods:**
- **Linear Probing**: Check next bucket (h+1, h+2,...)
- **Quadratic Probing**: Check h+1², h+2²,...
- **Double Hashing**: Use second hash function

---

## Python Dictionary Implementation

Python's dict uses:
- **Open Addressing** with random probing
- **Load Factor**: ~2/3 (67%) - resize when exceeded
- **Hash Function**: For strings, uses polynomial rolling hash

---

## Common Patterns

### 1. Frequency Counter
Count occurrences of elements.

### 2. Anagram Detection
Use character frequency as key.

### 3. Two Sum Problem
Use hash map to find complement.

### 4. Subarray Problems
Use prefix sum with hash map.

### 5. Hash Set for Deduplication
Quick membership checking.

---

## Interview Tips

### FAANG Expectations
1. **Know collision handling**
2. **Understand load factor**
3. **Space-time tradeoffs**

### Common Questions
- "How does dict work internally?"
- "What happens when hash collision occurs?"
- "What's the load factor?"

### Follow-up Questions
- "How to handle custom objects as keys?"
- "What if we need ordered keys?"
- "How would you implement LRU cache?"

---

## Practice Problems

### Easy
- [x] Two Sum
- [x] Valid Anagram
- [x] Ransom Note
- [x] First Unique Character

### Medium
- [x] Group Anagrams
- [x] Subarray Sum Equals K
- [x] Longest Substring Without Repeating Characters
- [x] Count Distinct Elements in Window

### Hard
- [x] Longest Consecutive Sequence
- [x] Subarray with K Different Integers
- [x] Random Pick with Weight
