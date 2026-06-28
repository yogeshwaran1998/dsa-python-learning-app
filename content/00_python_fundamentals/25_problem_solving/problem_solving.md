# Problem Solving - Theory Guide

## Table of Contents
1. [Introduction](#introduction)
2. [Edge Cases](#edge-cases)
3. [Optimization Path](#optimization-path)
4. [Brute Force Approach](#brute-force-approach)
5. [Hash-based Optimization](#hash-based-optimization)
6. [Two Pointers Optimization](#two-pointers-optimization)
7. [Dynamic Programming](#dynamic-programming)
8. [Problem Classification](#problem-classification)

---

## Introduction

Effective problem solving requires understanding both the problem domain and systematic optimization techniques. This guide covers edge case handling and the progression from simple to optimized solutions.

---

## Edge Cases

Edge cases are inputs that are at the extremes of what the algorithm should handle. Missing edge cases is a common source of bugs.

### Common Edge Cases

| Category | Edge Cases to Consider |
|----------|----------------------|
| Empty input | `[]`, `""`, `None` |
| Single element | `[x]`, `"a"` |
| Two elements | `[a, b]` |
| All same | `[1, 1, 1]` |
| All different | `[1, 2, 3]` |
| Sorted ascending | `[1, 2, 3]` |
| Sorted descending | `[3, 2, 1]` |
| Negative numbers | `[-1, -2, 3]` |
| Zero | `[0]`, `0` |
| Large values | Overflow considerations |
| Duplicates | Repeated elements |

### Examples

```python
def find_max(nums):
    """Find maximum - but what about edge cases?"""
    if not nums:  # Empty list
        return None
    return max(nums)


def two_sum(nums, target):
    """Two sum - consider edge cases."""
    if not nums or len(nums) < 2:
        return []

    # Handle: single element, duplicate values, negative numbers
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return []
```

---

## Optimization Path

### The Progression

```text
Brute Force (O(n^k)) -> Hash (O(n)) -> Two Pointers (O(n)) -> DP (O(n) or O(n^2))
     |                     |               |                   |
   Simple              Fast lookup    Space optimized     Optimal
```

### When to Use Each

| Approach | When to Use |
|----------|-------------|
| Brute Force | Small inputs, first attempt |
| Hash | Need fast lookups, O(n) needed |
| Two Pointers | Sorted input, two elements |
| Sliding Window | Subarrays/substrings |
| DP | Overlapping subproblems |

---

## Brute Force Approach

Start with the simplest solution, even if not optimal. This helps understand the problem.

### Characteristics
- Simple to implement
- Often O(n^2) or worse
- Good starting point
- Helps understand problem

### Example: Two Sum

```python
# Brute force - O(n^2)
def two_sum_brute(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
```

### When to Stop with Brute Force
- Time limit is generous
- Input size is small
- Quick solution needed for testing

---

## Hash-based Optimization

Use hash table (dict/set) for O(1) lookups.

### When to Use
- Need to find complement pairs
- Frequency counting
- Deduplication
- Lookups needed

### Example: Two Sum Optimized

```python
# Hash-based - O(n)
def two_sum_hash(nums, target):
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

### Example: Find Duplicates

```python
# Brute force - O(n^2)
def contains_duplicates_brute(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

# Hash-based - O(n)
def contains_duplicates_hash(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
```

---

## Two Pointers Optimization

Use when:
- Input is sorted
- Need to find pair that sums to target
- Need to merge sorted arrays

### Common Patterns

#### 1. Opposite Ends (Sorted Array)
```python
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current = arr[left] + arr[right]
        if current == target:
            return [left, right]
        elif current < target:
            left += 1
        else:
            right -= 1
    return []
```

#### 2. Same Direction (Sliding Window)
```python
def min_subarray_len(target, nums):
    left = 0
    current_sum = 0
    min_len = float('inf')

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return min_len if min_len != float('inf') else 0
```

#### 3. Fast and Slow (Linked List Cycle)
```python
def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False
```

---

## Dynamic Programming

Use when:
- Overlapping subproblems
- Optimal substructure
- Need to make decisions

### Steps

1. Define the problem recursively
2. Identify base cases
3. Build DP table (bottom-up or top-down)
4. Optimize space if possible

### Example: Fibonacci

```python
# Naive recursion - O(2^n)
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

# Memoization (Top-down) - O(n)
def fib_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

# Tabulation (Bottom-up) - O(n)
def fib_tab(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# Space optimized - O(n) time, O(1) space
def fib_optimized(n):
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr
```

### Example: Climbing Stairs

```python
def climb_stairs(n):
    """Find number of ways to climb n stairs."""
    if n <= 2:
        return n

    # Can climb 1 or 2 steps at a time
    # Ways(n) = Ways(n-1) + Ways(n-2)
    prev, curr = 1, 2
    for _ in range(3, n + 1):
        prev, curr = curr, prev + curr

    return curr
```

---

## Problem Classification

### By Input Structure

| Input Type | Common Patterns |
|------------|-----------------|
| Unsorted array | Hash, Two pointers after sorting |
| Sorted array | Binary search, Two pointers |
| Matrix | DFS/BFS, Matrix traversal |
| String | Sliding window, Two pointers |
| Linked list | Fast-slow pointers, Reversal |
| Tree | DFS, BFS, Recursion |

### By Problem Type

| Problem Type | Approach |
|--------------|----------|
| Find pair | Hash or Two pointers |
| Subarray | Sliding window, Prefix sum |
| Substring | Sliding window, KMP |
| Path/Graph | BFS, DFS, Dijkstra |
| Sorting | Built-in, Custom |
| Search | Binary search, Hash |

### By Optimization Level

1. **Simple (O(n^2))**: Brute force, nested loops
2. **Medium (O(n log n))**: Sorting + single pass
3. **Fast (O(n))**: Hash table, single pass
4. **Optimal (O(1))**: Mathematical, direct formula

---

## Interview Tips

### Problem Solving Approach

1. **Understand**: Read problem carefully, ask clarifications
2. **Edge Cases**: Consider empty, single, extremes
3. **Simple First**: Start with brute force
4. **Optimize**: Look for hash, two pointers, DP
5. **Verify**: Test on examples, edge cases
6. **Complexity**: Explain time and space

### What Interviewers Look For

1. Correctness on all cases
2. Understanding of trade-offs
3. Clean, readable code
4. Communication skills
5. Testing edge cases

---

## Summary

| Approach | Time | Space | When to Use |
|----------|------|-------|-------------|
| Brute Force | O(n^k) | O(1) | Small inputs |
| Hash | O(n) | O(n) | Lookups needed |
| Two Pointers | O(n) | O(1) | Sorted input |
| Sliding Window | O(n) | O(1) | Subarray problems |
| DP | O(n)/O(n^2) | O(n) | Overlapping problems |

---

## Practice Problems

- [x] Two sum (brute -> hash -> two pointers)
- [x] Valid palindrome
- [x] Container with most water
- [x] Longest substring without repeats
- [x] Climbing stairs
