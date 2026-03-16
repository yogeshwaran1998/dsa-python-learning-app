# Queues - Theory Guide

## Table of Contents
1. [What is a Queue?](#what-is-a-queue)
2. [Time Complexity](#time-complexity)
3. [Queue Types](#queue-types)
4. [Common Patterns](#common-patterns)
5. [Interview Tips](#interview-tips)

---

## What is a Queue?

A queue is a FIFO (First In, First Out) data structure. Think of it like a line at a store - the first person in line gets served first.

### Operations
- **enqueue**: Add element to rear - O(1)
- **dequeue**: Remove element from front - O(1)
- **peek/front**: View front element - O(1)
- **isEmpty**: Check if queue is empty - O(1)

### Visual Representation
```
Front → [1] [2] [3] [4] ← Rear
        ↑
        Next to be dequeued
```

---

## Time Complexity

| Operation | Time | Space |
|-----------|------|-------|
| enqueue | O(1) | O(n) total |
| dequeue | O(1) | O(n) total |
| peek | O(1) | O(1) |
| isEmpty | O(1) | O(1) |
| search | O(n) | O(n) |

---

## Queue Types

### 1. Simple Queue
Basic FIFO queue.

### 2. Circular Queue
- Front and rear wrap around
- Efficient space utilization
- Used in buffering, scheduling

### 3. Deque (Double-Ended Queue)
- Insert/delete from both ends
- Used in sliding window problems

### 4. Priority Queue
- Elements have priority
- Higher priority dequeued first
- Implemented using heap

---

## Common Patterns

### 1. BFS (Breadth-First Search)
Level-order traversal of trees/graphs.

### 2. Sliding Window Maximum
Find maximum in each window using deque.

### 3. Recent Counter
Track recent events within time window.

### 4. Task Scheduler
Execute tasks based on cooling time.

---

## Interview Tips

### FAANG Expectations
1. **Understand underlying implementation**
2. **Know when to use each type**
3. **Circular queue for fixed size**

### Common Mistakes
1. Forgetting to update front/rear pointers
2. Not handling overflow/underflow
3. Incorrect handling of empty queue

### Follow-up Questions
- "How would you implement using two stacks?"
- "What about priority queue?"
- "How does this scale?"

---

## Practice Problems

### Easy
- [x] Implement Queue using Stacks
- [x] Moving Average from Data Stream

### Medium
- [x] Sliding Window Maximum
- [x] Task Scheduler
- [x] Number of Recent Calls

### Hard
- [x] Design Messenger
- [x] Circular Dependents
