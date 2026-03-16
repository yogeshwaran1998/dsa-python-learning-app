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
```
        8
       / \
      3   10
     / \    \
    1   6    14
      / \   /
     4   7 13
```

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
