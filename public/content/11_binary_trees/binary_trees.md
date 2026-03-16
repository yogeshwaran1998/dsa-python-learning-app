# Binary Trees - Theory Guide

## Table of Contents
1. [What is a Binary Tree?](#what-is-a-binary-tree)
2. [Tree Terminology](#tree-terminology)
3. [Tree Traversals](#tree-traversals)
4. [Time Complexity](#time-complexity)
5. [Common Patterns](#common-patterns)
6. [Interview Tips](#interview-tips)

---

## What is a Binary Tree?

A binary tree is a hierarchical data structure where each node has at most two children, referred to as the left child and right child.

### Node Structure
```
    ┌───────┐
    │  val  │
    ├───┬───┤
    │   │   │
  left right
```

---

## Tree Terminology

- **Root**: Topmost node
- **Leaf**: Node with no children
- **Parent/Child**: Relative terms
- **Siblings**: Nodes with same parent
- **Ancestor/Descendant**: Direct lineage
- **Depth**: Distance from root (root = 0)
- **Height**: Longest path from node to leaf
- **Level**: All nodes at same depth

### Tree Properties
- **Binary Tree**: Max 2 children per node
- **Full Binary Tree**: Every node has 0 or 2 children
- **Complete Binary Tree**: All levels filled except last
- **Perfect Binary Tree**: All internal nodes have 2 children + all leaves at same level
- **Balanced Tree**: Left and right subtree heights differ by at most 1

---

## Tree Traversals

### 1. Depth-First Search (DFS)

| Order | Visit Sequence | Use Case |
|-------|---------------|----------|
| Pre-order | Root → Left → Right | Copy tree, prefix expression |
| In-order | Left → Root → Right | BST sorted output |
| Post-order | Left → Right → Root | Delete tree, postfix expression |

### 2. Breadth-First Search (BFS)
- Level order: Visit all nodes at current level before moving to next

### Visual Example
```
        1
       / \
      2   3
     / \   \
    4   5   6

Pre-order:   1 2 4 5 3 6
In-order:    4 2 5 1 3 6
Post-order:  4 5 2 6 3 1
Level-order: 1 2 3 4 5 6
```

---

## Time Complexity

| Operation | Average | Worst Case |
|-----------|---------|------------|
| Search | O(log n) | O(n) |
| Insert | O(log n) | O(n) |
| Delete | O(log n) | O(n) |
| Traversal | O(n) | O(n) |

**Worst case**: Linked list (degenerate tree)

---

## Common Patterns

### 1. Recursive Traversal
Process left subtree, then right, etc.

### 2. Level-by-Level (BFS)
Use queue to process level by level.

### 3. Tree to Array
Convert tree to array representation.

### 4. Path Sum
Find paths with specific sum.

### 5. Lowest Common Ancestor
Find common ancestor of two nodes.

---

## Interview Tips

### FAANG Expectations
1. **Recursive thinking**: Most tree problems are recursive
2. **Base cases**: Handle null nodes properly
3. **Space complexity**: Consider iterative solutions

### Common Mistakes
1. Not handling null nodes
2. Forgetting to return values in recursion
3. Not updating pointers correctly

### Follow-up Questions
- "Can you do it iteratively?"
- "What's the space complexity?"
- "How would you handle duplicates?"

---

## Practice Problems

### Easy
- [x] Maximum Depth of Binary Tree
- [x] Same Tree
- [x] Invert Binary Tree
- [x] Binary Tree Inorder Traversal

### Medium
- [x] Level Order Traversal
- [x] Maximum Depth (Bottom-up)
- [x] Validate Binary Search Tree
- [x] Symmetric Tree
- [x] Path Sum

### Hard
- [x] Binary Tree Maximum Path Sum
- [x] Serialize and Deserialize Binary Tree
- [x] Lowest Common Ancestor
- [x] Count Complete Tree Nodes
