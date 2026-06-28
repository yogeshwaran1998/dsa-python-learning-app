# Union Find - Theory Guide

## Table of Contents
1. [Introduction](#introduction)
2. [Data Structure](#data-structure)
3. [Path Compression](#path-compression)
4. [Union by Rank/Size](#union-by-rank-size)
5. [Connected Components](#connected-components)
6. [Common Problems](#common-problems)
7. [Time and Space Complexity](#time-and-space-complexity)
8. [Interview Tips](#interview-tips)
9. [Practice Problems](#practice-problems)

---

## Introduction

Union Find (Disjoint Set Union - DSU) is a data structure that tracks a set of elements partitioned into disjoint (non-overlapping) subsets. It supports two main operations:
- **Find**: Determine which subset a particular element belongs to
- **Union**: Merge two subsets into one

### Why Use Union Find?
- Efficiently track connected components
- Solve graph connectivity problems
- Used in Kruskal's MST algorithm
- Common in FAANG interviews

### When to Use
- Finding connected components
- Detecting cycles in graphs
- Network connectivity problems
- Grouping related elements

---

## Data Structure

### Components
1. **Parent Array**: Each element points to its parent
2. **Root**: Elements that point to themselves are roots

### Initial State
- Each element is its own parent
- Each element is its own set

### Visual Representation
```text
Initially:     After union(0,1), union(2,3):
0 1 2 3        0   2
| | | |        |   |
v v v v        v   v
0 1 2 3        0   2
```

---

## Path Compression

### Problem
Tree can become deep, making Find operations slow.

### Solution
Path Compression: During Find, make each node point directly to root.

### Implementation
```python
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # Recursively find root
    return parent[x]
```

### Effect
Near-constant time operations!

---

## Union by Rank/Size

### Problem
Unions can create unbalanced trees.

### Solution
- Track "rank" or "size" of each set
- Attach smaller tree under larger tree

### Implementation
- Union by Rank: Use tree height
- Union by Size: Use number of elements

### Result
O(log n) tree height even without path compression.

---

## Connected Components

### Concept
Union Find naturally tracks connected components in a graph.

### Algorithm
1. Initialize each node as separate component
2. Process edges, union connected nodes
3. Count unique roots = number of components

---

## Common Problems

### Problem 1: Number of Connected Components
Count connected components in undirected graph.

**Approach:**
- Initialize UnionFind with n nodes
- Union all edges
- Count unique parents

**Example:**
```text
Input: n = 5, edges = [[0,1], [1,2], [3,4]]
Output: 2
```

### Problem 2: Graph Valid Tree
Check if graph forms a valid tree.

**Approach:**
- Valid tree: connected and no cycles
- Check: edges = n - 1 AND single component

### Problem 3: Redundant Connection
Find edge that creates cycle.

**Approach:**
- Process edges sequentially
- If find() returns same root, edge is redundant

### Problem 4: Longest Consecutive Sequence
Use UnionFind with position mapping.

---

## Time and Space Complexity

| Operation | Without Optimization | With Both Optimizations |
|-----------|---------------------|------------------------|
| Initialize | O(n) | O(n) |
| Find | O(n) | O(alpha(n)) ~ O(1) |
| Union | O(n) | O(alpha(n)) ~ O(1) |
| Connected | O(n) | O(alpha(n)) ~ O(1) |

**Alpha(n)** = Inverse Ackermann function, practically constant.

---

## Interview Tips

### Key Questions to Ask
1. Is the graph directed or undirected?
2. How many nodes/edges?
3. Do we need to track additional info (weights, sizes)?

### Common Edge Cases
- Empty graph (0 nodes)
- Single node
- All connected
- Disconnected components

### Union Find Checklist
- [ ] Initialize parent array
- [ ] Implement find with path compression
- [ ] Implement union by rank/size
- [ ] Handle edge cases properly

### Follow-up Questions
- "How would you add cycle detection?"
- "How would you track component sizes?"
- "What's the time complexity?"

---

## Summary

Union Find is essential for:
- Connected component problems
- Graph connectivity
- Cycle detection
- Dynamic grouping

**Key Insight:** With path compression and union by rank, operations are effectively O(1). Perfect for problems involving dynamic connectivity.

---

## Practice Problems

### Easy
- Number of Connected Components
- Graph Valid Tree

### Medium
- Redundant Connection
- Friend Circles
- Number of Islands II

### Hard
- Number of Operations to Make Network Connected
- Minimum Cost to Make at Least One Valid Path
- Shortest Distance from All Buildings
