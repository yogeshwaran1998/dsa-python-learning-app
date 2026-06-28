# Dynamic Programming - Theory Guide

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

Dynamic Programming (DP) solves a problem by breaking it into **overlapping subproblems**, solving each subproblem **once**, and reusing the answer. It turns exponential brute-force recursion into polynomial time by trading memory for speed.

DP applies only when a problem has two properties:

1. **Optimal substructure** — an optimal solution is built from optimal solutions of subproblems.
2. **Overlapping subproblems** — the same subproblems recur many times (this is what separates DP from plain divide-and-conquer like merge sort, where subproblems are disjoint).

---

## When to Use

Reach for DP when you see any of these signals:

- You're asked for an **optimum** ("minimum / maximum / longest / fewest / number of ways").
- The brute-force solution is **exponential** and recomputes the same states.
- A choice at each step ("take it or skip it", "go right or down") leads to a smaller version of the same problem.
- The answer depends on a small number of **state variables** (an index, a remaining capacity, a position in a grid).

If subproblems do **not** repeat, you don't need DP — use plain recursion or greedy.

---

## How It Works

Every DP is defined by three things: the **state**, the **recurrence**, and the **base cases**.

Take **Climbing Stairs** — you can climb 1 or 2 steps at a time; how many ways to reach step `n`?

- **State:** `dp[i]` = number of ways to reach step `i`.
- **Recurrence:** `dp[i] = dp[i-1] + dp[i-2]` (you arrived from one step below or two below).
- **Base cases:** `dp[0] = 1`, `dp[1] = 1`.

Filling the table bottom-up for `n = 5`:

<div class="dsa-diagram dsa-diagram--center">
  <div class="dindex"><small>i=0</small><b>1</b></div>
  <div class="dindex"><small>i=1</small><b>1</b></div>
  <div class="dindex"><small>i=2</small><b>2</b></div>
  <div class="dindex"><small>i=3</small><b>3</b></div>
  <div class="dindex"><small>i=4</small><b>5</b></div>
  <div class="dindex"><small>i=5</small><b>8</b></div>
  <div class="dsa-caption">dp[i] = dp[i-1] + dp[i-2]; each cell is the sum of the two before it. Answer: dp[5] = 8.</div>
</div>

See `climb_stairs()` in the code panel — and `fibonacci_dp()` / `fibonacci_optimized()` for the same recurrence with O(1) space.

### Two ways to implement the same recurrence

| Approach | Direction | How | Trade-off |
|----------|-----------|-----|-----------|
| **Top-down (memoization)** | Main problem → base | Recurse, cache each state in a dict/array | Natural to write; recursion stack + cache overhead |
| **Bottom-up (tabulation)** | Base → main problem | Iterate, fill a table in dependency order | No recursion; easiest to space-optimize |

Both visit each state once, so they share the same time complexity. Bottom-up is usually preferred in interviews because it avoids stack-overflow risk and makes the **space optimization** (keeping only the last row/few cells) obvious.

---

## Complexity

Complexity is almost always **states × work-per-state**:

| Quantity | How to compute | Example (`coin_change`) |
|----------|----------------|-------------------------|
| Number of states | size of the state space | `amount + 1` |
| Work per state | cost of the transition | `len(coins)` |
| **Time** | states × work | `O(amount × coins)` |
| **Space** | size of the table (before optimization) | `O(amount)` |

Many 1D DPs (Fibonacci, House Robber, Climbing Stairs) compress space to **O(1)** by keeping only the last one or two values; 2D grid/string DPs often compress from `O(m·n)` to `O(n)` by keeping a single row.

---

## Core Patterns

| Pattern | State | Example problems | Code reference |
|---------|-------|------------------|----------------|
| **1D DP** | `dp[i]` over a sequence | Climbing Stairs, House Robber, Kadane | `climb_stairs()`, `house_robber()`, `maximum_subarray_kadane()` |
| **Unbounded / coin** | `dp[amount]` | Coin Change, Word Break | `coin_change()`, `word_break()` |
| **Subsequence (LIS)** | `dp[i]` = best ending at `i` | Longest Increasing Subsequence | `longest_increasing_subsequence()` |
| **2D grid** | `dp[r][c]` | Unique Paths, Min Path Sum | `unique_paths()`, `min_path_sum()` |
| **Two-string DP** | `dp[i][j]` over two strings | LCS, Edit Distance, LPS | `longest_common_subsequence()`, `edit_distance()`, `longest_palindromic_subsequence()` |

A reliable solving recipe:

1. Define the **state** in one sentence ("`dp[i][j]` = …").
2. Write the **recurrence** as a choice between subproblems.
3. Nail the **base cases** and the iteration order (dependencies must already be computed).
4. Code top-down first if the recurrence is clearer; convert to bottom-up to optimize.
5. Reduce **space** if only recent states are needed.

---

## Common Pitfalls

- **Wrong iteration order** — a cell is read before it's been computed. Fill states in dependency order.
- **Off-by-one in table size** — for a target of `amount`, the table has `amount + 1` entries (include 0).
- **Missing / wrong base case** — e.g. `coin_change` must seed `dp[0] = 0` and treat "unreachable" as infinity.
- **Memoizing on an incomplete key** — the cache key must include *every* variable the state depends on.
- **Using DP when greedy suffices** (or vice-versa) — if a locally optimal choice is provably globally optimal, greedy is simpler. See the Greedy chapter for the contrast.

---

## Interview Tips

- Start by stating brute-force recursion, then point out the **repeated subproblems** — that justifies DP out loud.
- Always define the state precisely before coding; most bugs come from a fuzzy state definition.
- Mention the **space optimization** even if you don't implement it; interviewers look for it.
- Common follow-ups: "reconstruct the actual solution, not just its value" (store parent pointers / backtrack through the table) and "reduce the space."

---

## Practice Problems

- **Easy:** Climbing Stairs, House Robber, Maximum Subarray (Kadane), Min Cost Climbing Stairs
- **Medium:** Coin Change, Longest Increasing Subsequence, Unique Paths, Word Break, Longest Common Subsequence, Partition Equal Subset Sum
- **Hard:** Edit Distance, Longest Palindromic Subsequence, Regular Expression Matching, Burst Balloons

---

## Summary

| Step | Question to answer |
|------|--------------------|
| State | What does `dp[...]` mean? |
| Recurrence | How does a state combine smaller states? |
| Base case | What are the smallest, directly-known answers? |
| Order | In what order are dependencies ready? |
| Complexity | states × work-per-state |
| Optimize | Can space drop to the last row / few cells? |

DP = **recursion + memory**. Find the state and the recurrence, and the rest is bookkeeping.
