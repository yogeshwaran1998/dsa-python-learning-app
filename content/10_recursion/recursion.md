# Recursion & Backtracking - Theory Guide

## Table of Contents
1. [Overview](#overview)
2. [When to Use](#when-to-use)
3. [How It Works](#how-it-works)
4. [Complexity](#complexity)
5. [Core Patterns](#core-patterns)
6. [Common Pitfalls](#common-pitfalls)
7. [Interview Tips](#interview-tips)
8. [Practice Problems](#practice-problems)
9. [Summary](#summary)

---

## Overview

Recursion solves a problem by having a function **call itself** on smaller inputs until it reaches a trivial **base case**. It's the natural tool for problems with self-similar structure — trees, divide-and-conquer, and combinatorial generation. **Backtracking** is recursion that explores choices, undoing each one before trying the next.

---

## When to Use

- The problem breaks into **smaller subproblems of the same shape** (trees, nested structures, divide and conquer).
- You must **generate or explore all candidates**: subsets, permutations, combinations, board configurations.
- A definition is naturally recursive (factorial, Fibonacci, tree height).

If subproblems overlap heavily, add **memoization** (that's top-down DP). If recursion depth could be huge and the call is the last action, consider an **iterative** rewrite to avoid stack overflow.

---

## How It Works

Every correct recursion has two parts:

1. **Base case(s)** — the smallest input you can answer directly (stops the recursion).
2. **Recursive case** — reduce toward the base case and combine results.

The calls form a **recursion tree**; each node is one invocation, and the call stack holds the path from the root to the current node.

<div class="dsa-diagram dsa-diagram--center">
  <div class="dsa-svg">
    <svg viewBox="0 0 320 180" role="img" aria-label="Recursion tree for fibonacci of 4 expanding into overlapping subcalls">
      <line class="tree-edge" x1="160" y1="28" x2="90" y2="78" />
      <line class="tree-edge" x1="160" y1="28" x2="230" y2="78" />
      <line class="tree-edge" x1="90" y1="78" x2="45" y2="140" />
      <line class="tree-edge" x1="90" y1="78" x2="135" y2="140" />
      <line class="tree-edge" x1="230" y1="78" x2="195" y2="140" />
      <line class="tree-edge" x1="230" y1="78" x2="275" y2="140" />
      <g><circle class="tree-node-shape" cx="160" cy="26" r="22" /><text class="tree-label" x="160" y="26">f(4)</text></g>
      <g><circle class="tree-node-shape" cx="90" cy="80" r="22" /><text class="tree-label" x="90" y="80">f(3)</text></g>
      <g><circle class="tree-node-shape" cx="230" cy="80" r="22" /><text class="tree-label" x="230" y="80">f(2)</text></g>
      <g><circle class="tree-node-shape" cx="45" cy="142" r="20" /><text class="tree-label" x="45" y="142">f(2)</text></g>
      <g><circle class="tree-node-shape" cx="135" cy="142" r="20" /><text class="tree-label" x="135" y="142">f(1)</text></g>
      <g><circle class="tree-node-shape" cx="195" cy="142" r="20" /><text class="tree-label" x="195" y="142">f(1)</text></g>
      <g><circle class="tree-node-shape" cx="275" cy="142" r="20" /><text class="tree-label" x="275" y="142">f(0)</text></g>
    </svg>
  </div>
  <div class="dsa-caption">fib(4)'s recursion tree — note f(2) is computed twice; memoizing it turns this into DP.</div>
</div>

See `factorial()`, `fibonacci()`, and `power()` for simple recursion; `max_depth()` / `is_same_tree()` for tree recursion.

### Backtracking template

Explore a choice, recurse, then **undo** it (backtrack) so the next choice starts clean:

```python
def backtrack(path, choices):
    if is_complete(path):
        result.append(path[:])     # record a copy
        return
    for choice in choices:
        path.append(choice)        # choose
        backtrack(path, next_choices)
        path.pop()                 # un-choose (backtrack)
```

See `subsets()`, `permutations()`, `combinations()`, and `solve_n_queens()`.

---

## Complexity

Cost = **(number of nodes in the recursion tree) × (work per node)**, and the recursion uses stack space equal to its **maximum depth**.

| Problem | Time | Space (stack) |
|---------|------|---------------|
| Factorial / linear recursion | O(n) | O(n) |
| Naive Fibonacci | O(2ⁿ) | O(n) |
| Subsets | O(n · 2ⁿ) | O(n) |
| Permutations | O(n · n!) | O(n) |
| Balanced divide & conquer | O(n log n) | O(log n) |

---

## Core Patterns

| Pattern | Idea | Code reference |
|---------|------|----------------|
| **Linear recursion** | One call per step toward base | `factorial()`, `power()` |
| **Tree recursion** | Multiple self-calls; combine results | `fibonacci()`, `max_depth()`, `is_same_tree()` |
| **Divide & conquer** | Split, solve halves, merge | `merge_sort()`, `quick_sort()` |
| **Subsets / combinations** | Include or exclude each element | `subsets()`, `combinations()` |
| **Permutations** | Fix each unused element at each position | `permutations()` |
| **Constraint backtracking** | Place, validate, recurse, undo | `solve_n_queens()` |

---

## Common Pitfalls

- **Missing or wrong base case** → infinite recursion and `RecursionError`.
- **Not reducing toward the base case** → the input must shrink on every call.
- **Mutating shared state without undoing it** → backtracking must `pop`/restore; record **copies** of results, not references.
- **Exponential recomputation** → overlapping subproblems need memoization (top-down DP).
- **Stack overflow on deep recursion** → Python's default limit is ~1000; convert deep tail recursion to iteration or an explicit stack.

---

## Interview Tips

- Always state the base case and the recursive reduction **before** coding — it's the clearest way to reason about correctness.
- For backtracking, describe the choice / explore / un-choose loop explicitly.
- Mention memoization the moment you notice repeated subproblems.
- Common follow-ups: "return all solutions vs. just count", "prune invalid branches early", "convert to iterative."

---

## Practice Problems

- **Easy:** Fibonacci Number, Power of Two, Reverse String (recursive), Merge Two Sorted Lists
- **Medium:** Subsets, Permutations, Combination Sum, Generate Parentheses, Letter Combinations of a Phone Number
- **Hard:** N-Queens, Sudoku Solver, Word Search II, Regular Expression Matching

---

## Summary

| Element | Question |
|---------|----------|
| Base case | When can I answer directly? |
| Recursive case | How do I shrink toward the base case? |
| Combine | How do subresults form the answer? |
| Backtrack | What state must I undo after each choice? |
| Cost | tree nodes × work; depth = stack space |

Recursion = **base case + a smaller version of the same problem**. Backtracking adds *choose → explore → un-choose*.
