# BFS and DFS - Theory Guide

## Table of Contents
1. [Introduction](#introduction)
2. [Depth-First Search (DFS)](#depth-first-search-dfs)
3. [Breadth-First Search (BFS)](#breadth-first-search-bfs)
4. [Graph Traversal Patterns](#graph-traversal-patterns)
5. [Common Problems](#common-problems)
6. [Time and Space Complexity](#time-and-space-complexity)
7. [Interview Tips](#interview-tips)
8. [Practice Problems](#practice-problems)

---

## Introduction

BFS (Breadth-First Search) and DFS (Depth-First Search) are fundamental graph traversal algorithms. They form the foundation for solving many algorithmic problems involving trees, graphs, and matrices.

### When to Use BFS
- Finding shortest path in unweighted graphs
- Level-order traversal
- Finding all nodes at distance k
- When you need to explore by "layers"

### When to Use DFS
- Path finding problems
- Detecting cycles
- Topological sorting
- When memory is a concern (less space)
- When exploring deep paths first

---

## Depth-First Search (DFS)

### Concept
Explore as far as possible along each branch before backtracking.

### Implementation Approaches

#### Recursive DFS
```python
def dfs(node):
    if node not in visited:
        visited.add(node)
        process(node)
        for neighbor in node.neighbors:
            dfs(neighbor)
```

#### Iterative DFS (using Stack)
```python
stack = [start_node]
while stack:
    node = stack.pop()
    if node not in visited:
        visited.add(node)
        process(node)
        stack.extend(neighbors)
```

### Types of DFS
1. **Pre-order**: Process before children
2. **In-order**: Process between children (trees)
3. **Post-order**: Process after children

---

## Breadth-First Search (BFS)

### Concept
Explore all nodes at current distance before moving to next layer.

### Implementation (using Queue/Deque)
```python
from collections import deque

def bfs(start):
    queue = deque([start])
    visited = {start}

    while queue:
        node = queue.popleft()
        process(node)
        for neighbor in node.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

### Key Properties
- Uses queue data structure
- Guarantees shortest path in unweighted graphs
- Processes level by level

---

## Graph Traversal Patterns

### Pattern 1: Connected Components
Find number of connected components in graph.

**Approach:**
- Iterate through all nodes
- For unvisited node, do DFS/BFS to mark all reachable nodes
- Count each new exploration as one component

### Pattern 2: Cycle Detection
Detect if graph contains a cycle.

**Approach:**
- Use DFS with three states: unvisited, visiting, visited
- If we encounter "visiting" node, there's a cycle

### Pattern 3: Topological Sort
Order nodes in dependency order.

**Approach:**
- Use DFS and add to result in post-order
- Reverse the result

---

## Common Problems

### Problem 1: Number of Islands
Count number of islands in 2D grid.

**Approach:**
- Iterate through grid
- When land ('1') found and not visited:
  - Do DFS/BFS to mark entire island
  - Increment island count

**Example:**
```text
Input: [
  ['1','1','0','0','0'],
  ['1','1','0','0','0'],
  ['0','0','1','0','0'],
  ['0','0','0','1','1']
]
Output: 3
```

### Problem 2: Binary Tree Level Order Traversal
Traverse tree level by level.

**Approach:**
- Use BFS with queue
- Track level size to separate levels

### Problem 3: Clone Graph
Deep copy a graph.

**Approach:**
- Use BFS/DFS with hashmap to map original to clone

### Problem 4: Word Ladder
Find shortest transformation sequence.

**Approach:**
- Use BFS starting from begin word
- Each level represents one transformation step

---

## Time and Space Complexity

| Operation | Time | Space |
|-----------|------|-------|
| DFS (recursive) | O(V + E) | O(V) |
| DFS (iterative) | O(V + E) | O(V) |
| BFS | O(V + E) | O(V) |

Where V = vertices/nodes, E = edges

---

## Interview Tips

### Key Questions to Ask
1. Is the graph directed or undirected?
2. Is there a starting node specified?
3. Should we use recursion or iteration?
4. Are there cycles to handle?

### Common Edge Cases
- Empty graph
- Single node
- Disconnected graph
- Graph with cycles

### BFS vs DFS Decision
- **Use BFS**: Shortest path, level-order, when answer is close to start
- **Use DFS**: Path finding, when tree depth is not too large, less memory

### DFS Checklist
- [ ] Handle visited set to avoid infinite loops
- [ ] Handle base cases (null, empty)
- [ ] Choose recursion vs iteration

### BFS Checklist
- [ ] Use deque for O(1) pop operations
- [ ] Mark visited when adding to queue (not when popping)
- [ ] Track level for multi-level problems

---

## Summary

BFS and DFS are essential for:
- Graph and tree traversals
- Finding connected components
- Path finding problems
- Level-order problems
- Cycle detection

**Key Insight:** BFS uses more memory but finds shortest path. DFS uses less memory for certain problems. Choose based on problem requirements.

---

## Practice Problems

### Easy
- Maximum Depth of Binary Tree
- Same Tree
- Symmetric Tree
- Binary Tree Inorder Traversal

### Medium
- Number of Islands
- Clone Graph
- Binary Tree Level Order Traversal
- Maximum Depth of N-ary Tree

### Hard
- Word Ladder
- Shortest Path in Binary Matrix
- Reconstruct Itinerary
- Word Search II
