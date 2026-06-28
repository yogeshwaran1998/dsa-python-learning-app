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

Each edge is a character; a path from the root spells a prefix. Green nodes mark the end of a stored word.

<div class="dsa-diagram dsa-diagram--center">
  <div class="dsa-svg">
    <svg viewBox="0 0 320 240" role="img" aria-label="Trie storing the words app, and, and cat">
      <line class="tree-edge" x1="160" y1="28" x2="100" y2="84" />
      <line class="tree-edge" x1="160" y1="28" x2="240" y2="84" />
      <line class="tree-edge" x1="100" y1="84" x2="60" y2="142" />
      <line class="tree-edge" x1="100" y1="84" x2="150" y2="142" />
      <line class="tree-edge" x1="240" y1="84" x2="240" y2="142" />
      <line class="tree-edge" x1="60" y1="142" x2="60" y2="198" />
      <line class="tree-edge" x1="150" y1="142" x2="150" y2="198" />
      <line class="tree-edge" x1="240" y1="142" x2="240" y2="198" />
      <g><circle class="tree-node-shape" cx="160" cy="26" r="18" /><text class="tree-label tree-label--muted" x="160" y="26">root</text></g>
      <g><circle class="tree-node-shape" cx="100" cy="86" r="16" /><text class="tree-label" x="100" y="86">a</text></g>
      <g><circle class="tree-node-shape" cx="240" cy="86" r="16" /><text class="tree-label" x="240" y="86">c</text></g>
      <g><circle class="tree-node-shape" cx="60" cy="142" r="16" /><text class="tree-label" x="60" y="142">p</text></g>
      <g><circle class="tree-node-shape" cx="150" cy="142" r="16" /><text class="tree-label" x="150" y="142">n</text></g>
      <g><circle class="tree-node-shape" cx="240" cy="142" r="16" /><text class="tree-label" x="240" y="142">a</text></g>
      <g><circle class="tree-node-shape tree-node-shape--green" cx="60" cy="198" r="16" /><text class="tree-label" x="60" y="198">p</text></g>
      <g><circle class="tree-node-shape tree-node-shape--green" cx="150" cy="198" r="16" /><text class="tree-label" x="150" y="198">d</text></g>
      <g><circle class="tree-node-shape tree-node-shape--green" cx="240" cy="198" r="16" /><text class="tree-label" x="240" y="198">t</text></g>
    </svg>
  </div>
  <div class="dsa-caption">Green = end of word. Stored words: app, and, cat. "a" is a shared prefix of app and and.</div>
</div>

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
