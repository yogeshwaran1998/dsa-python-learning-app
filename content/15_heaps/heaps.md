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

A heap is a complete binary tree stored compactly in an array — no pointers needed. The tree below is the same data as the array.

<div class="dsa-diagram dsa-diagram--center">
  <div class="dindex"><small>0</small><b>50</b></div>
  <div class="dindex"><small>1</small><b>30</b></div>
  <div class="dindex"><small>2</small><b>20</b></div>
  <div class="dindex"><small>3</small><b>15</b></div>
  <div class="dindex"><small>4</small><b>10</b></div>
  <div class="dindex"><small>5</small><b>8</b></div>
  <div class="dindex"><small>6</small><b>16</b></div>
</div>

<div class="dsa-diagram dsa-diagram--center">
  <div class="dsa-svg">
    <svg viewBox="0 0 340 200" role="img" aria-label="Max-heap as a complete binary tree">
      <line class="tree-edge" x1="170" y1="30" x2="100" y2="88" />
      <line class="tree-edge" x1="170" y1="30" x2="240" y2="88" />
      <line class="tree-edge" x1="100" y1="88" x2="60" y2="150" />
      <line class="tree-edge" x1="100" y1="88" x2="140" y2="150" />
      <line class="tree-edge" x1="240" y1="88" x2="210" y2="150" />
      <line class="tree-edge" x1="240" y1="88" x2="280" y2="150" />
      <g><circle class="tree-node-shape tree-node-shape--green" cx="170" cy="28" r="20" /><text class="tree-label" x="170" y="28">50</text></g>
      <g><circle class="tree-node-shape" cx="100" cy="90" r="20" /><text class="tree-label" x="100" y="90">30</text></g>
      <g><circle class="tree-node-shape" cx="240" cy="90" r="20" /><text class="tree-label" x="240" y="90">20</text></g>
      <g><circle class="tree-node-shape" cx="60" cy="152" r="18" /><text class="tree-label" x="60" y="152">15</text></g>
      <g><circle class="tree-node-shape" cx="140" cy="152" r="18" /><text class="tree-label" x="140" y="152">10</text></g>
      <g><circle class="tree-node-shape" cx="210" cy="152" r="18" /><text class="tree-label" x="210" y="152">8</text></g>
      <g><circle class="tree-node-shape" cx="280" cy="152" r="18" /><text class="tree-label" x="280" y="152">16</text></g>
    </svg>
  </div>
  <div class="dsa-caption">Max-heap: every parent ≥ its children. The root (50) is the maximum.</div>
</div>

Index arithmetic ties the array and tree together:

```text
Parent(i) = (i - 1) // 2
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
