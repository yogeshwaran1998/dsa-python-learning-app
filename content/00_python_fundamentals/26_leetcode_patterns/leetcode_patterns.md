# LeetCode Patterns - Theory Guide

## Table of Contents
1. [Introduction](#introduction)
2. [Two Pointers](#two-pointers)
3. [Sliding Window](#sliding-window)
4. [Fast and Slow Pointers](#fast-and-slow-pointers)
5. [Binary Search](#binary-search)
6. [Prefix Sum](#prefix-sum)
7. [Depth-First Search (DFS)](#depth-first-search-dfs)
8. [Breadth-First Search (BFS)](#breadth-first-search-bfs)
9. [Backtracking](#backtracking)
10. [Dynamic Programming Patterns](#dynamic-programming-patterns)

---

## Introduction

Recognizing patterns is key to solving LeetCode problems efficiently. This guide covers the most common algorithmic patterns with examples.

---

## Two Pointers

Use two pointers moving in same or opposite directions.

### Pattern 1: Opposite Ends (Sorted Array)

**When**: Input is sorted, need to find pair that sums to target.

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

### Pattern 2: Same Direction (In-place Modification)

**When**: Remove elements or deduplicate in sorted array.

```python
def remove_duplicates(arr):
    slow = 0
    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
    return slow + 1
```

### Problems
- [x] Valid Palindrome
- [x] 3Sum
- [x] Container With Most Water
- [x] Remove Duplicates from Sorted Array

---

## Sliding Window

Maintain a window that slides through data.

### Fixed Window Size

```python
def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum
```

### Variable Window Size

```python
def min_subarray_len(target, arr):
    left = 0
    current_sum = 0
    min_len = float('inf')

    for right in range(len(arr)):
        current_sum += arr[right]

        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= arr[left]
            left += 1

    return min_len if min_len != float('inf') else 0
```

### Problems
- [x] Maximum Sum Subarray
- [x] Longest Substring Without Repeating Characters
- [x] Minimum Window Substring
- [x] Fruits Into Baskets

---

## Fast and Slow Pointers

Two pointers moving at different speeds. Used for cycle detection.

### Detect Cycle in Linked List

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

### Find Middle of Linked List

```python
def middle_node(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow
```

### Problems
- [x] Linked List Cycle
- [x] Middle of Linked List
- [x] Happy Number

---

## Binary Search

For sorted arrays or monotonic functions.

### Standard Binary Search

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

### Find First/Last Position

```python
def find_first(arr, target):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continue searching left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result
```

### Search in Rotated Array

```python
def search_rotated(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        # Left half is sorted
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1
```

### Problems
- [x] Binary Search
- [x] Search in Rotated Array
- [x] Find First and Last Position
- [x] Search Insert Position

---

## Prefix Sum

Pre-compute cumulative sums for fast range queries.

### Basic Prefix Sum

```python
def range_sum(arr, left, right):
    prefix = [0] * (len(arr) + 1)
    for i, val in enumerate(arr):
        prefix[i + 1] = prefix[i] + val

    return prefix[right + 1] - prefix[left]
```

### Subarray Sum Equals K

```python
def subarray_sum(nums, k):
    count = 0
    prefix_sum = 0
    sum_freq = {0: 1}

    for num in nums:
        prefix_sum += num
        if prefix_sum - k in sum_freq:
            count += sum_freq[prefix_sum - k]
        sum_freq[prefix_sum] = sum_freq.get(prefix_sum, 0) + 1

    return count
```

### Problems
- [x] Range Sum Query
- [x] Subarray Sum Equals K
- [x] Continuous Subarray Sum

---

## Depth-First Search (DFS)

Explore as far as possible before backtracking.

### Recursive DFS

```python
def dfs(node, visited):
    if not node or node in visited:
        return

    visited.add(node)
    print(node.val)

    for neighbor in node.neighbors:
        if neighbor not in visited:
            dfs(neighbor, visited)
```

### Binary Tree DFS

```python
def preorder(root):
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

def postorder(root):
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]
```

### Problems
- [x] Maximum Depth of Binary Tree
- [x] Validate Binary Search Tree
- [x] Path Sum
- [x] Clone Graph

---

## Breadth-First Search (BFS)

Explore level by level using queue.

### Level Order Traversal

```python
from collections import deque

def level_order(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)

    return result
```

### Shortest Path in Unweighted Graph

```python
def shortest_path(graph, start, end):
    if start == end:
        return 0

    visited = {start}
    queue = deque([(start, 0)])

    while queue:
        node, dist = queue.popleft()

        for neighbor in graph[node]:
            if neighbor == end:
                return dist + 1
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))

    return -1
```

### Problems
- [x] Binary Tree Level Order Traversal
- [x] Minimum Depth of Binary Tree
- [x] Number of Islands
- [x] Open the Lock

---

## Backtracking

Try all possibilities, backtrack when dead end.

### Permutations

```python
def permute(nums):
    result = []

    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])

        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]

    backtrack(0)
    return result
```

### Subsets

```python
def subsets(nums):
    result = []

    def backtrack(index, path):
        result.append(path[:])

        for i in range(index, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result
```

### Problems
- [x] Subsets
- [x] Permutations
- [x] Combination Sum
- [x] N-Queens

---

## Dynamic Programming Patterns

### Pattern 1: Fibonacci

```python
def fib(n):
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr
```

### Pattern 2: 0/1 Knapsack

```python
def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]
```

### Pattern 3: Longest Common Subsequence

```python
def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]
```

### Pattern 4: House Robber

```python
def house_robber(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    prev, curr = nums[0], max(nums[0], nums[1])

    for i in range(2, len(nums)):
        prev, curr = curr, max(curr, prev + nums[i])

    return curr
```

### Problems
- [x] Climbing Stairs
- [x] House Robber
- [x] Coin Change
- [x] Longest Increasing Subsequence

---

## Summary Table

| Pattern | Time | Space | Use Case |
|---------|------|-------|----------|
| Two Pointers | O(n) | O(1) | Sorted array, pairs |
| Sliding Window | O(n) | O(1) | Subarrays |
| Fast-Slow | O(n) | O(1) | Cycle detection |
| Binary Search | O(log n) | O(1) | Sorted arrays |
| Prefix Sum | O(n) | O(n) | Range queries |
| DFS | O(V+E) | O(V) | Tree/graph traversal |
| BFS | O(V+E) | O(V) | Shortest path |
| Backtracking | O(n!) | O(n) | Combinations |
| DP | O(n^2) | O(n) | Optimization |

---

## Interview Quick Reference

| Problem Type | First Try |
|--------------|-----------|
| Array sorted | Two pointers |
| Subarray | Sliding window |
| Linked list cycle | Fast-slow |
| Sorted array search | Binary search |
| Range sum | Prefix sum |
| Tree path | DFS |
| Shortest path | BFS |
| Generate combinations | Backtracking |
| Optimization | DP |
