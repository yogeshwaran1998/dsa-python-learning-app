# Linked Lists - Theory Guide

## Table of Contents
1. [What is a Linked List?](#what-is-a-linked-list)
2. [Types of Linked Lists](#types-of-linked-lists)
3. [Time Complexity](#time-complexity)
4. [Common Patterns](#common-patterns)
5. [Interview Tips](#interview-tips)

---

## What is a Linked List?

A linked list is a linear data structure where elements (nodes) are stored in separate objects. Each node contains:
- **Data**: The actual value
- **Next Pointer**: Reference to the next node

Unlike arrays, linked lists don't require contiguous memory and can grow/shrink dynamically.

### Node Structure
```
┌──────┬──────────┐
│ Data │  Next    │
│  5   │ ────────►│ ─► Next Node
└──────┴──────────┘
```

---

## Types of Linked Lists

### 1. Singly Linked List
- Each node has data and next pointer
- Traversal is one-directional
- Memory efficient (n nodes = n * 2 pointers)

### 2. Doubly Linked List
- Each node has data, next, and previous pointers
- Can traverse both directions
- Enables deletion in O(1) with just node reference
- Extra memory for previous pointer

### 3. Circular Linked List
- Last node points back to first
- Can be singly or doubly
- Useful for round-robin scheduling

---

## Time Complexity

### Singly Linked List

| Operation | Average | Worst Case |
|-----------|---------|------------|
| Access by index | O(n) | O(n) |
| Search | O(n) | O(n) |
| Insert at head | O(1) | O(1) |
| Insert at tail | O(1)* | O(n)** |
| Delete at head | O(1) | O(1) |
| Delete at tail | O(n) | O(n) |

*If tail pointer maintained
**If tail pointer not maintained

### Doubly Linked List

| Operation | Average | Worst Case |
|-----------|---------|------------|
| Insert at position | O(1)* | O(n) |
| Delete at position | O(1)* | O(n) |

*If node reference is given

---

## Key Differences: Array vs Linked List

| Aspect | Array | Linked List |
|--------|-------|-------------|
| Memory | Contiguous | Scattered |
| Access | O(1) by index | O(n) |
| Insert/Delete at beginning | O(n) | O(1) |
| Insert/Delete at end | O(1) | O(n)* |
| Memory overhead | None | Pointer overhead |
| Cache friendly | Yes | No |

---

## Common Patterns

### 1. Fast and Slow Pointers (Tortoise and Hare)
Use two pointers at different speeds:
- **Detect cycle**: If they meet, there's a cycle
- **Find middle**: Fast reaches end, slow is at middle
- **Find nth from end**: Maintain n-distance gap

### 2. Reversal
In-place reversal by reversing pointers:
- Reverse entire list
- Reverse in groups (k-group reversal)

### 3. Merge Two Sorted Lists
Classic problem combining two sorted lists:
- Compare heads, pick smaller
- Recursively merge remaining

### 4. Dummy Node
Use a dummy head node to simplify:
- Edge cases (empty list)
- Building result list
- Adding to beginning

### 5. Window/Sliding
Create "window" of nodes:
- Find length of list
- Find nodes in range

---

## Interview Tips

### Always Clarify
1. **Singly or doubly?**
2. **Is there a tail pointer?**
3. **Should we delete nodes or just skip?**

### Common Mistakes to Avoid
1. **Forgetting to update pointers**
2. **Memory leaks (in C/C++)**
3. **Not handling empty list**
4. **Not handling single node**
5. **Not handling head/tail specially**

### FAANG Expectations
1. **O(1) space** - Can't use extra data structures
2. **In-place** - Modify existing list
3. **Edge cases** - Empty, single node, all same values
4. **Clean pointer manipulation**

### Follow-up Questions
- "Can you do it in O(1) space?"
- "What if it's a circular list?"
- "How would you handle duplicates?"
- "Can you do it recursively?"

---

## Practice Problems

### Easy
- [x] Reverse Linked List
- [x] Merge Two Sorted Lists
- [x] Delete Node in a Linked List
- [x] Palindrome Linked List
- [x] Linked List Cycle

### Medium
- [x] Reverse Linked List II
- [x] Odd Even Linked List
- [x] Swap Nodes in Pairs
- [x] Rotate List
- [x] Reverse Nodes in k-Group
- [x] Copy List with Random Pointer

### Hard
- [x] Merge k Sorted Lists
- [x] LRU Cache
- [x] List Flattening
- [x] Clone Linked List with Next and Random Pointer

---

## Summary

| Pattern | Use Case | Time |
|---------|----------|------|
| Fast-Slow | Find middle, detect cycle | O(n) |
| Reversal | Reverse list | O(n) |
| Dummy Node | Build/merge lists | O(n) |
| Merge | Combine sorted lists | O(n) |
| Gap Method | Find nth from end | O(n) |
