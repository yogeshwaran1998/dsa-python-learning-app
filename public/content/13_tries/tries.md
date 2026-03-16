# Tries (Prefix Trees) - Theory Guide

## Table of Contents
1. [What is a Trie?](#what-is-a-trie)
2. [Time Complexity](#time-complexity)
3. [Trie Operations](#trie-operations)
4. [Common Patterns](#common-patterns)
5. [Interview Tips](#interview-tips)

---

## What is a Trie?

A Trie (also called prefix tree) is a tree data structure used for efficient string operations:
- **Insert**: O(m) where m = word length
- **Search**: O(m)
- **Prefix Search**: O(m)

### Visual Example
```
Root
├── a
│   ├── p
│   │   └── p*
│   └── n
│       └── d*
└── c
    └── a
        └── t*
```
* = end of word (app, an, cat)

---

## Time Complexity

| Operation | Time | Space |
|-----------|------|-------|
| Insert | O(m) | O(m) |
| Search | O(m) | O(m) |
| Prefix Search | O(m) | O(m) |
| Delete | O(m) | O(m) |

---

## When to Use Tries

1. **Autocomplete/Prefix Matching**
2. **Spell Checking**
3. **IP Routing (Longest Prefix)**
4. **Word Games (Boggle)**

---

## Interview Tips

### FAANG Expectations
1. **Space optimization** - Consider compressing tries
2. **Memory tradeoffs** - Children as array vs hash map
3. **Edge cases** - Empty strings, single character

### Common Mistakes
1. Not marking word endings
2. Forgetting to delete empty nodes
3. Not handling case sensitivity

---

## Practice Problems

### Easy
- [x] Implement Trie
- [x] Longest Common Prefix

### Medium
- [x] Prefix Trie
- [x] Word Search
- [x] Auto-complete

### Hard
- [x] Palindrome Pairs
- [x] Maximum XOR Trie
