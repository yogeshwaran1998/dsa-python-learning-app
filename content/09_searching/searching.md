# Searching Algorithms - Theory Guide

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

Searching locates a value — or a *boundary* — within data. Linear search scans every element in O(n); **binary search** halves the search space each step to reach O(log n), but requires the data (or the answer space) to be **monotonic**. Most interview "search" problems are really binary-search-in-disguise.

---

## When to Use

Binary search applies whenever you can phrase the problem as: *"find the smallest/largest x for which a condition is true,"* where the condition is **monotonic** (false, false, …, true, true, …).

Signals:

- The array is **sorted**, or can be sorted cheaply.
- You're looking for a **boundary**: first/last occurrence, insertion point, lower/upper bound.
- The answer lies in a numeric range and a feasibility check is monotonic ("binary search on the answer" — e.g. minimum capacity, smallest divisor).

---

## How It Works

Maintain a `[lo, hi]` window over the search space. Each step, examine `mid`; discard the half that can't contain the answer.

<div class="dsa-diagram dsa-diagram--center">
  <div class="dindex"><small>0</small><b>1</b></div>
  <div class="dindex"><small>1</small><b>3</b></div>
  <div class="dindex"><small>2</small><b>5</b></div>
  <div class="dindex"><small>3</small><b>7</b></div>
  <div class="dindex"><small>4</small><b>9</b></div>
  <div class="dindex"><small>5</small><b>11</b></div>
  <div class="dindex"><small>6</small><b>13</b></div>
  <div class="dsa-caption">Searching for 11: mid=index 3 (7) &lt; 11 → search right half; mid=index 5 (11) → found.</div>
</div>

The canonical loop (see `binary_search()`):

```python
lo, hi = 0, len(arr) - 1
while lo <= hi:
    mid = lo + (hi - lo) // 2   # avoids overflow in other languages
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        lo = mid + 1
    else:
        hi = mid - 1
return -1
```

### Boundaries: lower vs upper bound

Plain binary search finds *an* index; **boundary** search finds the *first* or *last* match — essential for duplicates and ranges. `lower_bound()` returns the first index `>= target`; `upper_bound()` the first `> target`. The difference between them is the count of `target`. See `binary_search_left()`, `binary_search_right()`, `lower_bound()`, `upper_bound()`.

---

## Complexity

| Method | Time | Space |
|--------|------|-------|
| Linear search | O(n) | O(1) |
| Binary search (iterative) | O(log n) | O(1) |
| Binary search (recursive) | O(log n) | O(log n) stack |
| Binary search on answer | O(n · log(range)) | O(1) |

---

## Core Patterns

| Pattern | Idea | Code reference |
|---------|------|----------------|
| **Exact match** | Standard `lo <= hi` loop | `binary_search()` |
| **Lower / upper bound** | First index satisfying a condition | `lower_bound()`, `upper_bound()`, `binary_search_left()`, `binary_search_right()` |
| **Rotated array** | One half is always sorted — search it | `search_rotated()`, `find_min_rotated()`, `find_pivot()` |
| **Unbounded / unknown size** | Exponentially expand, then binary search | `binary_search_unknown_range()` |
| **Binary search on the answer** | Search a numeric range with a feasibility test | `find_sqrt()` |
| **Peak / local extremum** | Compare with neighbor to pick a side | `find_peak()` |

---

## Common Pitfalls

- **Infinite loops** — wrong `mid` update or loop condition. Be deliberate about `lo <= hi` vs `lo < hi`, and whether you move to `mid` or `mid ± 1`.
- **Off-by-one at boundaries** — lower/upper bound logic is easy to flip; test on "target absent", "all equal", "target at the ends".
- **Searching unsorted data** — binary search silently returns wrong results; confirm monotonicity first.
- **Overflow** — `(lo + hi) / 2` overflows in fixed-width languages; use `lo + (hi - lo) // 2` (a good habit even in Python).

---

## Interview Tips

- When you see "sorted" or "find the minimum/maximum value that works", think binary search immediately.
- Articulate the **invariant**: what does `[lo, hi]` still possibly contain at each step? This prevents off-by-one bugs.
- Practice the boundary templates until they're automatic — most interview binary-search bugs are boundary bugs.
- Common follow-ups: "find first and last position" (two boundary searches), "search a 2D sorted matrix", "median of two sorted arrays."

---

## Practice Problems

- **Easy:** Binary Search, Search Insert Position, First Bad Version, Sqrt(x)
- **Medium:** Find First and Last Position, Search in Rotated Sorted Array, Find Peak Element, Koko Eating Bananas, Find Minimum in Rotated Sorted Array
- **Hard:** Median of Two Sorted Arrays, Split Array Largest Sum, Find in Mountain Array

---

## Summary

| Question | Answer |
|----------|--------|
| Precondition? | Monotonic / sorted search space |
| Core idea? | Discard half the space each step |
| Cost? | O(log n) |
| Hard part? | Boundary conditions and loop invariant |

Binary search is less about arrays and more about **monotonic decision spaces** — master the boundary templates and "binary search on the answer."
