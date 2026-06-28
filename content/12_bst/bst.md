# Binary Search Trees - Theory Guide

## Table of Contents
1. [What is a BST?](#what-is-a-bst)
2. [Time Complexity](#time-complexity)
3. [BST Operations](#bst-operations)
4. [Common Patterns](#common-patterns)
5. [Interview Tips](#interview-tips)

---

## What is a BST?

A Binary Search Tree is a binary tree with the following properties:
- **Left subtree** contains nodes with values **less than** root
- **Right subtree** contains nodes with values **greater than** root
- **Both subtrees** are also BSTs

### Visual Example

For every node, all left-subtree values are smaller and all right-subtree values are larger — so an in-order traversal yields sorted output.

<div class="dsa-diagram dsa-diagram--center">
  <div class="dsa-svg">
    <svg viewBox="0 0 360 240" role="img" aria-label="Binary search tree rooted at 8">
      <line class="tree-edge" x1="180" y1="28" x2="110" y2="80" />
      <line class="tree-edge" x1="180" y1="28" x2="250" y2="80" />
      <line class="tree-edge" x1="110" y1="80" x2="70" y2="132" />
      <line class="tree-edge" x1="110" y1="80" x2="150" y2="132" />
      <line class="tree-edge" x1="250" y1="80" x2="290" y2="132" />
      <line class="tree-edge" x1="150" y1="132" x2="120" y2="186" />
      <line class="tree-edge" x1="150" y1="132" x2="180" y2="186" />
      <line class="tree-edge" x1="290" y1="132" x2="260" y2="186" />
      <g><circle class="tree-node-shape" cx="180" cy="28" r="18" /><text class="tree-label" x="180" y="28">8</text></g>
      <g><circle class="tree-node-shape" cx="110" cy="80" r="18" /><text class="tree-label" x="110" y="80">3</text></g>
      <g><circle class="tree-node-shape" cx="250" cy="80" r="18" /><text class="tree-label" x="250" y="80">10</text></g>
      <g><circle class="tree-node-shape" cx="70" cy="132" r="18" /><text class="tree-label" x="70" y="132">1</text></g>
      <g><circle class="tree-node-shape" cx="150" cy="132" r="18" /><text class="tree-label" x="150" y="132">6</text></g>
      <g><circle class="tree-node-shape" cx="290" cy="132" r="18" /><text class="tree-label" x="290" y="132">14</text></g>
      <g><circle class="tree-node-shape" cx="120" cy="186" r="18" /><text class="tree-label" x="120" y="186">4</text></g>
      <g><circle class="tree-node-shape" cx="180" cy="186" r="18" /><text class="tree-label" x="180" y="186">7</text></g>
      <g><circle class="tree-node-shape" cx="260" cy="186" r="18" /><text class="tree-label" x="260" y="186">13</text></g>
    </svg>
  </div>
  <div class="dsa-caption">In-order traversal: 1 3 4 6 7 8 10 13 14 (sorted).</div>
</div>

---

## Time Complexity

| Operation | Average | Worst Case |
|-----------|---------|------------|
| Search | O(log n) | O(n) |
| Insert | O(log n) | O(n) |
| Delete | O(log n) | O(n) |
| Min/Max | O(log n) | O(n) |
| Traversal | O(n) | O(n) |

**Worst case**: Sorted input creates degenerate tree (linked list)

---

## BST Operations

### 1. Search
- Compare with root
- Go left if smaller, right if larger
- Recurse until found or null

### 2. Insert
- Search for position (same as search)
- Insert new node at null position

### 3. Delete
- **Case 1**: Leaf node - simply remove
- **Case 2**: One child - replace with child
- **Case 3**: Two children - replace with in-order successor, delete successor

### 4. Validation
- For each node, check valid range
- Recursively validate left and right

---

## Common Patterns

### 1. In-order Traversal
Gives sorted output for BST.

### 2. Range Queries
Find nodes in given range.

### 3. BST to Array
Convert to sorted array.

### 4. Iterator Pattern
Implement next smallest element.

---

## Interview Tips

### FAANG Expectations
1. **Understand deletion** (two children case)
2. **Handle duplicates** (usually ignore or handle specially)
3. **Space complexity** for recursive solutions

### Common Mistakes
1. Not handling empty tree
2. Wrong range in validation
3. Forgetting to update pointers

### Follow-up Questions
- "How would you balance the tree?"
- "What if duplicates are allowed?"
- "Can you do it iteratively?"

---

## Practice Problems

### Easy
- [x] Search in BST
- [x] Minimum BST
- [x] Convert Sorted Array to BST

### Medium
- [x] Validate BST
- [x] Insert into BST
- [x] Delete Node in BST
- [x] BST Iterator
- [x] Kth Smallest Element

### Hard
- [x] Recover BST
- [x] BST Range Sum
- [x] Count Complete Tree Nodes
