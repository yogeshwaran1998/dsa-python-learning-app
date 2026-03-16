# Heaps/Priority Queues - Theory Guide

## Table of Contents
1. [What is a Heap?](#what-is-a-heap)
2. [Time Complexity](#time-complexity)
3. [Heap Operations](#heap-operations)
4. [Common Patterns](#common-patterns)
5. [Interview Tips](#interview-tips)

---

## What is a Heap?

A heap is a complete binary tree where:
- **Max Heap**: Parent >= Children
- **Min Heap**: Parent <= Children

### Properties
- Complete binary tree (filled left to right)
- Operations maintain heap property
- Usually implemented as array

### Array Representation
```
Index:    0   1   2   3   4   5   6
Value:   50  30  20  15  10  8   16

        50(0)
       /    \
     30(1)  20(2)
    /   \   /
  15(3)10(4)8(5)

Parent(i) = (i-1)//2
Left(i)   = 2*i + 1
Right(i)  = 2*i + 2
```

---

## Time Complexity

| Operation | Time |
|-----------|------|
| Insert | O(log n) |
| Extract Min/Max | O(log n) |
| Peek | O(1) |
| Build Heap | O(n) |
| Heapify | O(n) |

---

## Common Patterns

### 1. Kth Largest/Smallest
Use min-heap for kth largest, max-heap for kth smallest.

### 2. Top K Elements
Maintain heap of size k.

### 3. Merge K Sorted
Use min-heap to merge.

### 4. Median Data Stream
Two heaps (max + min).

---

## Interview Tips

### FAANG Expectations
1. **When to use heap** - Know the use cases
2. **Implementation** - Understand heapify
3. **Tradeoffs** - Space vs time

### Follow-up Questions
- "How would you implement?"
- "What's the space complexity?"

---

## Practice Problems

### Easy
- [x] Kth Largest Element
- [x] Median of Data Stream

### Medium
- [x] Top K Frequent Elements
- [x] Merge K Sorted Lists
- [x] Task Scheduler
