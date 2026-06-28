# Sorting Algorithms - Theory Guide

## Table of Contents
1. [Overview](#overview)
2. [When to Use](#when-to-use)
3. [How It Works](#how-it-works)
4. [Complexity](#complexity)
5. [Core Patterns](#core-patterns)
6. [Common Pitfalls](#common-pitfalls)
7. [Interview Tips](#interview-tips)
8. [Practice Problems](#practice-problems)
9. [Summary](#summary)

---

## Overview

Sorting arranges elements into order and is the backbone of countless algorithms — binary search, two-pointer techniques, interval problems, and deduplication all assume sorted input. Knowing the trade-offs between sorting algorithms (time, space, stability, in-place) is a core interview skill.

In practice you'll call the language's built-in sort (Python's Timsort, O(n log n), stable); interviews test whether you *understand* the algorithms underneath.

---

## When to Use

- A later step needs ordered data (binary search, greedy by key, merging intervals).
- You need the **k-th smallest/largest**, a median, or the top-k (a partial sort or heap may beat a full sort).
- Counting/Radix sort fits when keys are **small integers** — they beat the O(n log n) comparison lower bound by not comparing.

Reach for a **heap** instead of sorting when you only need a few extremes, or **quickselect** for a single order statistic in O(n) average.

---

## How It Works

The two O(n log n) workhorses both use **divide and conquer**:

- **Merge Sort** — split in half, sort each half, then *merge* the two sorted halves. Stable, but needs O(n) extra space. See `merge_sort()` / `merge()`.
- **Quick Sort** — pick a pivot, *partition* values into `< pivot` and `> pivot`, recurse on each side. In-place and cache-friendly, but O(n²) worst case on bad pivots. See `quick_sort()`, `quick_sort_inplace()`, `partition()`.

<div class="dsa-diagram dsa-diagram--center">
  <div class="dsa-svg">
    <svg viewBox="0 0 340 170" role="img" aria-label="Merge sort splitting an array into halves and merging them back sorted">
      <g><rect class="tree-node-shape" x="120" y="10" width="100" height="24" rx="4" /><text class="tree-label" x="170" y="22">[5,2,8,1]</text></g>
      <line class="tree-edge" x1="150" y1="34" x2="90" y2="70" />
      <line class="tree-edge" x1="190" y1="34" x2="250" y2="70" />
      <g><rect class="tree-node-shape" x="50" y="70" width="80" height="24" rx="4" /><text class="tree-label" x="90" y="82">[5,2]</text></g>
      <g><rect class="tree-node-shape" x="210" y="70" width="80" height="24" rx="4" /><text class="tree-label" x="250" y="82">[8,1]</text></g>
      <line class="tree-edge tree-edge--accent" x1="90" y1="94" x2="120" y2="130" />
      <line class="tree-edge tree-edge--accent" x1="250" y1="94" x2="220" y2="130" />
      <g><rect class="tree-node-shape tree-node-shape--green" x="110" y="130" width="120" height="24" rx="4" /><text class="tree-label" x="170" y="142">[1,2,5,8]</text></g>
    </svg>
  </div>
  <div class="dsa-caption">Merge sort: split down to single elements, then merge pairs back together in order.</div>
</div>

### Stability

A sort is **stable** if equal elements keep their original relative order. This matters when sorting by multiple keys (e.g. by score, then preserving insertion order for ties). Merge, Insertion, Counting, and Radix are stable; Selection, Quick, and Heap are not.

---

## Complexity

| Algorithm | Time (Avg) | Time (Worst) | Space | Stable | Code |
|-----------|-----------|--------------|-------|--------|------|
| Bubble | O(n²) | O(n²) | O(1) | Yes | `bubble_sort()` |
| Selection | O(n²) | O(n²) | O(1) | No | `selection_sort()` |
| Insertion | O(n²) | O(n²) | O(1) | Yes | `insertion_sort()` |
| Merge | O(n log n) | O(n log n) | O(n) | Yes | `merge_sort()` |
| Quick | O(n log n) | O(n²) | O(log n) | No | `quick_sort()` |
| Heap | O(n log n) | O(n log n) | O(1) | No | `heap_sort()` |
| Counting | O(n + k) | O(n + k) | O(k) | Yes | `counting_sort()` |
| Radix | O(n·k) | O(n·k) | O(n + k) | Yes | `radix_sort()` |

`k` = range of key values / number of digits. Comparison sorts cannot beat **O(n log n)** in the worst case; Counting/Radix/Bucket sidestep this by not comparing.

---

## Core Patterns

| Pattern | Idea | Code reference |
|---------|------|----------------|
| **Divide & conquer** | Split, recurse, combine | `merge_sort()`, `quick_sort()` |
| **Partition (Lomuto/Hoare)** | Rearrange around a pivot | `partition()`, `quick_sort_inplace()` |
| **Heapify** | Build a heap, repeatedly extract max | `heap_sort()`, `heapify()` |
| **Non-comparison (digit/bucket)** | Distribute by key, then collect | `counting_sort()`, `radix_sort()`, `bucket_sort()` |
| **Dutch national flag** | 3-way partition in one pass | `sort_colors()` |
| **Sort then sweep** | Sort to enable a linear second pass | `merge_intervals()` |

---

## Common Pitfalls

- **Quick Sort worst case** — already-sorted input with a naive (first/last) pivot degrades to O(n²); use a random or median-of-three pivot.
- **Forgetting stability requirements** — sorting by a secondary key needs a stable sort (or a composite key).
- **Off-by-one in partition / merge bounds** — the most common source of bugs; test on size 0, 1, 2.
- **Counting/Radix on large or negative key ranges** — space blows up; they only suit small, bounded non-negative keys.

---

## Interview Tips

- Default to the built-in sort and state its guarantees (Timsort: O(n log n), stable). Reach for a custom sort only when asked to implement one.
- If only the top-k or k-th element is needed, say so — a heap (O(n log k)) or quickselect (O(n) avg) beats a full sort.
- Know **why** Quick Sort is usually fastest in practice (in-place, cache-friendly) despite its worse worst case.
- Common follow-ups: "sort a linked list" (merge sort fits — no random access), "sort with O(1) extra space" (heap sort).

---

## Practice Problems

- **Easy:** Sort an Array, Merge Sorted Array, Squares of a Sorted Array
- **Medium:** Sort Colors, Kth Largest Element, Merge Intervals, Largest Number, Pancake Sorting
- **Hard:** Count of Smaller Numbers After Self, Maximum Gap, Reverse Pairs

---

## Summary

| Need | Best choice |
|------|-------------|
| General purpose | Quick Sort / built-in Timsort |
| Stability required | Merge Sort |
| O(1) extra space | Heap Sort |
| Small integer keys | Counting / Radix Sort |
| Linked list | Merge Sort |
| Nearly sorted | Insertion Sort |

Know the **O(n log n) lower bound** for comparison sorts, the stability of each, and when non-comparison sorts apply.
