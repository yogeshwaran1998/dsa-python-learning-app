# Union-Find (Disjoint Set Union) - Theory Guide

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

Union-Find (a.k.a. Disjoint Set Union, DSU) tracks a collection of **disjoint sets** and answers "are these two elements in the same set?" while letting you **merge** sets. With its two standard optimizations it does both operations in near-constant amortized time, making it the go-to structure for **dynamic connectivity** problems.

It supports two operations:

- **find(x)** — return the representative ("root") of x's set.
- **union(x, y)** — merge the sets containing x and y.

---

## When to Use

- You need to **group elements** and repeatedly ask whether two are connected.
- **Cycle detection** in an undirected graph (a cycle exists if an edge connects two nodes already in the same set).
- **Connected components**, number of islands, friend circles, account merging.
- Building a **Minimum Spanning Tree** with Kruskal's algorithm.

Prefer Union-Find over BFS/DFS when connectivity queries and merges arrive **incrementally** (online), or when you only care about *which* component, not the actual path.

---

## How It Works

Each set is a tree; every element points to a parent, and the **root** identifies the set. `find` walks to the root; `union` links one root under another.

<div class="dsa-diagram dsa-diagram--center">
  <div class="dsa-svg">
    <svg viewBox="0 0 320 150" role="img" aria-label="Two disjoint trees merged by pointing one root to the other">
      <line class="tree-edge" x1="70" y1="42" x2="45" y2="100" />
      <line class="tree-edge" x1="70" y1="42" x2="95" y2="100" />
      <line class="tree-edge tree-edge--accent" x1="230" y1="42" x2="70" y2="42" />
      <line class="tree-edge" x1="230" y1="42" x2="255" y2="100" />
      <g><circle class="tree-node-shape tree-node-shape--green" cx="230" cy="40" r="20" /><text class="tree-label" x="230" y="40">2</text></g>
      <g><circle class="tree-node-shape" cx="70" cy="40" r="20" /><text class="tree-label" x="70" y="40">0</text></g>
      <g><circle class="tree-node-shape" cx="45" cy="102" r="18" /><text class="tree-label" x="45" y="102">1</text></g>
      <g><circle class="tree-node-shape" cx="95" cy="102" r="18" /><text class="tree-label" x="95" y="102">3</text></g>
      <g><circle class="tree-node-shape" cx="255" cy="102" r="18" /><text class="tree-label" x="255" y="102">4</text></g>
    </svg>
  </div>
  <div class="dsa-caption">union(0, 2): root 2 (larger tree) becomes the parent of root 0. All five elements now share root 2.</div>
</div>

Two optimizations make it fast (see the `UnionFind` class in the code panel):

1. **Path compression** — during `find`, repoint every node directly to the root, flattening the tree for next time.
2. **Union by rank/size** — always attach the *smaller* tree under the *larger* root, keeping trees shallow.

Used together, the amortized cost per operation is **O(α(n))**, where α is the inverse Ackermann function — effectively constant (≤ 4 for any realistic n).

---

## Complexity

| Operation | No optimization | Path compression + union by rank |
|-----------|-----------------|----------------------------------|
| find | O(n) | O(α(n)) ≈ O(1) |
| union | O(n) | O(α(n)) ≈ O(1) |
| Space | O(n) | O(n) |

A sequence of `m` operations on `n` elements runs in **O(m · α(n))** ≈ O(m).

---

## Core Patterns

| Pattern | Idea | Code reference |
|---------|------|----------------|
| **Core DSU** | parent[] + rank[], compress on find | `UnionFind` |
| **Cycle detection (undirected)** | Edge within the same set ⇒ cycle | `has_cycle()` |
| **Connected components / grid** | Union adjacent cells, count roots | `num_islands()`, `friend_circles()` |
| **Kruskal's MST** | Sort edges, union if they don't form a cycle | `kruskal_mst()` |

> Note: cycle detection in a **directed** graph uses DFS colors, not DSU — see `has_cycle_directed()`.

---

## Common Pitfalls

- **Comparing nodes, not roots** — "same set?" must compare `find(a) == find(b)`, never `a == b` or `parent[a] == parent[b]`.
- **Skipping path compression** — without it, trees grow tall and `find` degrades toward O(n).
- **Union by rank done wrong** — attach the smaller tree under the larger; equal ranks bump the new root's rank by 1.
- **Counting components incorrectly** — count *distinct roots* (or maintain a running component counter, decrementing on each successful union).
- **Index vs. value mapping** — for non-integer elements, map them to indices first.

---

## Interview Tips

- If a problem mentions "connected", "groups", "merge", or "is X reachable from Y" with incremental edges, reach for Union-Find.
- Mention both optimizations and the α(n) result — interviewers expect you to know why it's near-constant.
- Maintaining a **component count** that decrements on each real union is a common, clean trick.
- Common follow-ups: "number of connected components", "redundant connection (find the cycle edge)", "accounts merge."

---

## Practice Problems

- **Easy:** Find if Path Exists in Graph, Number of Provinces
- **Medium:** Number of Islands, Redundant Connection, Accounts Merge, Graph Valid Tree, Most Stones Removed
- **Hard:** Number of Islands II, Smallest String With Swaps, Bricks Falling When Hit

---

## Summary

| Aspect | Detail |
|--------|--------|
| Operations | find(x), union(x, y) |
| Optimizations | Path compression + union by rank/size |
| Amortized cost | O(α(n)) ≈ O(1) |
| Killer apps | Connectivity, cycle detection, Kruskal's MST |
| vs. BFS/DFS | Better for incremental merges & pure connectivity |

Union-Find = **near-constant connectivity**. Always compare **roots**, and always apply both optimizations.
