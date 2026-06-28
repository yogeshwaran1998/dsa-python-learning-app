# Problem-Solving Patterns Summary

## Quick Reference for Interviews

### Pattern 1: Two Pointers
- **Use**: Sorted array, pair finding, partitioning
- **Time**: O(n), Space: O(1)

### Pattern 2: Sliding Window
- **Use**: Subarray/substring problems
- **Time**: O(n), Space: O(1) or O(k)

### Pattern 3: Binary Search
- **Use**: Sorted data, monotonic functions
- **Time**: O(log n), Space: O(1)

### Pattern 4: Fast & Slow Pointers
- **Use**: Linked list cycle detection, finding middle
- **Time**: O(n), Space: O(1)

### Pattern 5: BFS
- **Use**: Level-order, shortest path in unweighted graph
- **Time**: O(V+E), Space: O(V)

### Pattern 6: DFS
- **Use**: Tree/graph traversal, backtracking
- **Time**: O(V+E), Space: O(V)

### Pattern 7: Dynamic Programming
- **Use**: Optimization with overlapping subproblems
- **Time**: O(n²) or O(n*k), Space: varies

### Pattern 8: Union-Find
- **Use**: Cycle detection, connected components
- **Time**: O(α(n)), Space: O(V)

### Pattern 9: Monotonic Stack
- **Use**: Next greater/smaller element, stock span
- **Time**: O(n), Space: O(n)

### Pattern 10: Heap Priority Queue
- **Use**: Top K elements, merging sorted lists
- **Time**: O(n log k), Space: O(k)

---

## When to Use What?

| Problem Type | Best Approach |
|-------------|---------------|
| Find pair in sorted array | Two Pointers |
| Subarray with condition | Sliding Window |
| Find in sorted data | Binary Search |
| Kth largest/smallest | Heap |
| Tree level order | BFS |
| Tree path problems | DFS |
| Optimization with choices | DP |
| Graph connectivity | Union-Find |
| Next element problems | Monotonic Stack |
| Graph shortest path | Dijkstra/BFS |
