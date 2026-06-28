# Heaps - Theory Guide

## Table of Contents
1. [Introduction](#introduction)
2. [Heap Properties](#heap-properties)
3. [heapq Module](#heapq-module)
4. [Min and Max Heaps](#min-and-max-heaps)
5. [Top K Problems](#top-k-problems)
6. [Kth Largest/Smallest](#kth-largestsmallest)
7. [Common Problems](#common-problems)
8. [Time and Space Complexity](#time-and-space-complexity)
9. [Interview Tips](#interview-tips)
10. [Practice Problems](#practice-problems)

---

## Introduction

A Heap is a specialized tree-based data structure that satisfies the heap property. It is commonly used to implement priority queues and solve problems requiring ordered data.

### Types of Heaps
1. **Min Heap**: Parent is smaller than children
2. **Max Heap**: Parent is larger than children

### Why Use Heaps?
- O(1) access to minimum/maximum element
- Efficient insertion: O(log n)
- Perfect for "K largest/smallest" problems
- Used in Dijkstra's algorithm

---

## Heap Properties

### Complete Binary Tree
- All levels filled except possibly last
- Filled left to right

### Heap Property
- **Min Heap**: `parent <= children`
- **Max Heap**: `parent >= children`

### Array Representation
- Parent of node i: `(i-1) // 2`
- Left child of node i: `2*i + 1`
- Right child of node i: `2*i + 2`

---

## heapq Module

Python's `heapq` provides min-heap operations.

### Key Functions
```python
import heapq

heapq.heappush(heap, item)  # Push item onto heap
heapq.heappop(heap)         # Pop and return smallest item
heapq.heapify(list)         # Transform list into heap
```

### Max Heap Implementation
- Store negative values (Python only has min-heap)
- Or use custom comparison

---

## Min and Max Heaps

### When to Use Min Heap
- Finding K smallest elements
- Priority queue (min first)
- Dijkstra's algorithm

### When to Use Max Heap
- Finding K largest elements
- Max priority queue
- Median of stream

---

## Top K Problems

### Problem: Top K Frequent Elements
Find K most frequent elements.

**Approach:**
- Count frequencies
- Use min-heap of size K
- For each element, if heap size > K, pop smallest
- Result is heap contents

### Problem: K Closest Points
Find K closest points to origin.

**Approach:**
- Calculate distances
- Use max-heap of size K
- Keep K closest points

---

## Kth Largest/Smallest

### Problem: Kth Largest Element
Find Kth largest element in array.

**Approach:**
- Build min-heap of first K elements
- Process remaining elements
- If element > heap[0], replace

### Alternative: QuickSelect
- Average O(n), worst O(n^2)
- In-place

---

## Common Problems

### Problem 1: Merge K Sorted Lists
Merge K sorted linked lists.

**Approach:**
- Use min-heap to track smallest elements
- Push first element from each list
- Pop smallest, push next from same list

### Problem 2: Median of Data Stream
Find median of running data.

**Approach:**
- Use two heaps: max-heap (lower half), min-heap (upper half)
- Balance sizes
- Median from heap tops

### Problem 3: Sliding Window Median
Find median in sliding window.

**Approach:**
- Use balanced BST or two heaps
- Maintain window elements
- O(n log k)

---

## Time and Space Complexity

| Operation | Time | Space |
|-----------|------|-------|
| Push | O(log n) | O(n) |
| Pop | O(log n) | O(1) |
| Peek | O(1) | O(1) |
| Build Heap | O(n) | O(n) |
| K Largest (heap) | O(n log k) | O(k) |
| K Smallest (heap) | O(n log k) | O(k) |

---

## Interview Tips

### Key Questions to Ask
1. Should we return elements or indices?
2. Is there a specific order within top K?
3. Can we modify the original array?
4. What if K equals array length?

### Common Edge Cases
- K = 0 or K > array length
- All same elements
- Empty array
- Single element

### Heaps Checklist
- [ ] Use heapq for Python
- [ ] Consider max-heap via negation
- [ ] Handle duplicates properly
- [ ] Clean up heap after processing

### Follow-up Questions
- "What's the time complexity?"
- "Can you do it without extra space?"
- "How would you handle duplicates?"

---

## Summary

Heaps are essential for:
- Finding K largest/smallest elements
- Priority queue implementation
- Median problems
- Merging sorted sequences

**Key Insight:** Heaps give O(log n) insert/delete and O(1) peek. Perfect for maintaining "best K" candidates while processing stream of data.

---

## Practice Problems

### Easy
- Kth Largest Element in a Stream
- Last Stone Weight
- Maximum Product

### Medium
- Top K Frequent Elements
- K Closest Points to Origin
- Merge K Sorted Lists
- Find Median from Data Stream

### Hard
- Sliding Window Median
- IPO
- Minimum Cost to Hire K Workers
- Median of Two Sorted Arrays
