# Graphs - Theory Guide

## Table of Contents
1. [What is a Graph?](#what-is-a-graph)
2. [Graph Representations](#graph-representations)
3. [Graph Traversals](#graph-traversals)
4. [Graph Algorithms](#graph-algorithms)
5. [Interview Tips](#interview-tips)

---

## What is a Graph?

A graph is a set of vertices (nodes) connected by edges. Graphs can represent many real-world relationships.

### Types of Graphs

| Type | Description |
|------|-------------|
| Directed | Edges have direction |
| Undirected | Edges bidirectional |
| Weighted | Edges have weights |
| Cyclic | Contains cycles |
| Acyclic | No cycles (DAG) |

---

## Graph Representations

### 1. Adjacency List
```python
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}
```
**Space**: O(V + E)

### 2. Adjacency Matrix
```
    A B C D
A   0 1 1 0
B   1 0 0 1
C   1 0 0 1
D   0 1 1 0
```
**Space**: O(V²)

---

## Time Complexity

| Operation | Adjacency List | Adjacency Matrix |
|-----------|---------------|------------------|
| Add Vertex | O(1) | O(V²) |
| Add Edge | O(1) | O(1) |
| Remove Vertex | O(V + E) | O(V²) |
| Remove Edge | O(E) | O(1) |
| Query Edge | O(E) | O(1) |

---

## Graph Traversals

### 1. BFS (Breadth-First Search)
- Uses queue
- Finds shortest path in unweighted graph
- Time: O(V + E), Space: O(V)

### 2. DFS (Depth-First Search)
- Uses stack (or recursion)
- Time: O(V + E), Space: O(V)

---

## Common Algorithms

### Shortest Path
- **Dijkstra**: O((V + E) log V) - positive weights
- **Bellman-Ford**: O(V * E) - negative weights
- **Floyd-Warshall**: O(V³) - all pairs

### Minimum Spanning Tree
- **Prim's**: O((V + E) log V)
- **Kruskal's**: O(E log V)

### Topological Sort
- **Kahn's Algorithm**: O(V + E)
- **DFS-based**: O(V + E)

---

## Interview Tips

### FAANG Expectations
1. **Choose right representation** - Adjacency list for sparse graphs
2. **Understand algorithm tradeoffs**
3. **Handle edge cases** - Disconnected components

### Follow-up Questions
- "What if graph has negative weights?"
- "How to detect cycle?"
- "What's the space complexity?"

---

## Practice Problems

### Easy
- [x] Clone Graph
- [x] Flood Fill
- [x] Number of Islands

### Medium
- [x] Clone Graph
- [x] Pacific Atlantic Water Flow
- [x] Number of Connected Components
- [x] Course Schedule

### Hard
- [x] Word Ladder
- [x] Alien Dictionary
- [x] Critical Connections
