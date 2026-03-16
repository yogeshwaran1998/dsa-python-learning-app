# Union-Find (Disjoint Set Union) - Theory Guide

## What is Union-Find?

A data structure that tracks disjoint sets and supports:
- **Find**: Which set does element belong to?
- **Union**: Merge two sets together

## Time Complexity

| Operation | Without Optimization | With Both Optimizations |
|-----------|---------------------|------------------------|
| Find | O(n) | O(α(n)) ≈ O(1) |
| Union | O(1) | O(α(n)) ≈ O(1) |

**α(n)** = Inverse Ackermann function (practically constant)

## Optimizations

1. **Path Compression**: Flatten tree during find
2. **Union by Rank**: Attach smaller tree to larger

## Use Cases

- Cycle detection in graphs
- Connected components
- Kruskal's MST
- Network connectivity

## Interview Tips

- Know both optimizations
- Understand when to use vs BFS/DFS
