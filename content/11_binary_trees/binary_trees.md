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

Each node stores a value and two pointers — `left` and `right` — to its child subtrees (either may be `null`).

<div class="dsa-diagram dsa-diagram--center">
  <div class="dsa-svg">
    <svg viewBox="0 0 260 170" role="img" aria-label="A binary tree node with value and left and right child pointers">
      <line class="tree-edge" x1="130" y1="48" x2="70" y2="112" />
      <line class="tree-edge" x1="130" y1="48" x2="190" y2="112" />
      <text class="tree-edge-label" x="86" y="86">left</text>
      <text class="tree-edge-label" x="174" y="86">right</text>
      <circle class="tree-node-shape" cx="130" cy="32" r="24" />
      <text class="tree-label" x="130" y="32">val</text>
      <circle class="tree-node-shape tree-node-shape--null" cx="70" cy="132" r="20" />
      <text class="tree-label tree-label--muted" x="70" y="132">L</text>
      <circle class="tree-node-shape tree-node-shape--null" cx="190" cy="132" r="20" />
      <text class="tree-label tree-label--muted" x="190" y="132">R</text>
    </svg>
  </div>
  <div class="dsa-caption">A node holds a value plus left (L) and right (R) child pointers; dashed nodes may be null.</div>
</div>

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

<div class="dsa-diagram dsa-diagram--center">
  <div class="dsa-svg">
    <svg viewBox="0 0 320 200" role="img" aria-label="Binary tree with root 1, children 2 and 3, leaves 4, 5 under 2 and 6 under 3">
      <line class="tree-edge" x1="160" y1="30" x2="90" y2="92" />
      <line class="tree-edge" x1="160" y1="30" x2="230" y2="92" />
      <line class="tree-edge" x1="90" y1="92" x2="45" y2="160" />
      <line class="tree-edge" x1="90" y1="92" x2="135" y2="160" />
      <line class="tree-edge" x1="230" y1="92" x2="265" y2="160" />
      <g><circle class="tree-node-shape" cx="160" cy="30" r="20" /><text class="tree-label" x="160" y="30">1</text></g>
      <g><circle class="tree-node-shape" cx="90" cy="95" r="20" /><text class="tree-label" x="90" y="95">2</text></g>
      <g><circle class="tree-node-shape" cx="230" cy="95" r="20" /><text class="tree-label" x="230" y="95">3</text></g>
      <g><circle class="tree-node-shape" cx="45" cy="165" r="20" /><text class="tree-label" x="45" y="165">4</text></g>
      <g><circle class="tree-node-shape" cx="135" cy="165" r="20" /><text class="tree-label" x="135" y="165">5</text></g>
      <g><circle class="tree-node-shape" cx="265" cy="165" r="20" /><text class="tree-label" x="265" y="165">6</text></g>
    </svg>
  </div>
  <div class="dsa-caption">Example tree used for the traversal orders below.</div>
</div>

```text
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
