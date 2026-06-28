# Greedy Algorithms - Theory Guide

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

A greedy algorithm builds a solution step by step, always taking the choice that looks best **right now**, and never reconsiders it. When the problem has the right structure, these locally optimal choices add up to a globally optimal answer — with far less work than dynamic programming.

The catch: greedy is only correct when a locally optimal choice is *provably* part of some global optimum. Otherwise it gives a fast but wrong answer.

---

## When to Use

Greedy is a fit when the problem has both:

1. **Greedy-choice property** — a globally optimal solution can be reached by making a locally optimal choice at each step.
2. **Optimal substructure** — after making that choice, what remains is a smaller instance of the same problem.

Practical signals:

- Sorting the input by some key makes the choice "obvious" (earliest finish time, smallest weight, highest ratio).
- You're scheduling, selecting intervals, or covering with the fewest items.
- A DP solution exists but a single sweep clearly dominates.

If a greedy choice can paint you into a corner (a now-good choice forces a worse future), use **DP** instead.

---

## How It Works

Classic example — **Activity Selection**: given intervals, pick the maximum number that don't overlap. The greedy insight: **always pick the activity that finishes earliest**, because it leaves the most room for the rest.

<div class="dsa-diagram dsa-diagram--center">
  <div class="dsa-svg">
    <svg viewBox="0 0 360 150" role="img" aria-label="Five activities on a timeline; the non-overlapping set chosen by earliest finish time is highlighted">
      <line class="tree-edge" x1="20" y1="130" x2="350" y2="130" />
      <rect class="tree-node-shape tree-node-shape--green" x="30" y="20" width="90" height="18" rx="4" />
      <text class="tree-edge-label" x="75" y="14">A (pick)</text>
      <rect class="tree-node-shape" x="80" y="44" width="120" height="18" rx="4" />
      <text class="tree-edge-label" x="140" y="74">B (overlaps A)</text>
      <rect class="tree-node-shape tree-node-shape--green" x="140" y="86" width="100" height="18" rx="4" />
      <text class="tree-edge-label" x="190" y="118">C (pick)</text>
      <rect class="tree-node-shape tree-node-shape--green" x="260" y="20" width="80" height="18" rx="4" />
      <text class="tree-edge-label" x="300" y="14">D (pick)</text>
    </svg>
  </div>
  <div class="dsa-caption">Sort by finish time, then greedily take each activity that starts after the last one taken ends.</div>
</div>

The recipe is almost always: **sort by the right key, then sweep once**, keeping a running choice. See `activity_selection()` and `merge_intervals()` in the code panel.

### Proving a greedy is correct

Two standard arguments:

- **Exchange argument** — show any optimal solution can be transformed into the greedy one without getting worse (swap a non-greedy choice for the greedy choice).
- **"Greedy stays ahead"** — show that after each step the greedy partial solution is at least as good as any other on the relevant metric.

If you can't make such an argument, be suspicious — the greedy is probably wrong.

---

## Complexity

Most greedy algorithms are dominated by the initial **sort**:

| Step | Cost |
|------|------|
| Sort by key | O(n log n) |
| Single greedy sweep | O(n) |
| **Total (typical)** | **O(n log n)** |

Heap-based greedies (Huffman coding, Dijkstra) are O(n log n) from the priority-queue operations rather than an upfront sort. Space is usually O(1)–O(n).

---

## Core Patterns

| Pattern | Greedy choice | Code reference |
|---------|---------------|----------------|
| **Interval scheduling** | Earliest finish time | `activity_selection()`, `activity_selection_all()` |
| **Interval merging** | Sort by start, extend current | `merge_intervals()`, `insert_interval()` |
| **Jump / reachability** | Track farthest reachable index | `can_reach_end()`, `min_jumps()` |
| **Partitioning** | Extend a partition to the last seen index | `partition_labels()` |
| **Gas station / circuit** | Reset start when running total goes negative | `can_complete_circuit()` |
| **Prefix optimum (Kadane)** | Drop prefix when it hurts | `max_subarray_sum()`, `max_subarray_sum_indices()` |
| **Huffman coding** | Merge two smallest frequencies (heap) | `huffman_encoding()` |

---

## Common Pitfalls

- **Assuming greedy works without proof** — many problems (0/1 Knapsack, Coin Change with arbitrary coins) *look* greedy but aren't; they need DP.
- **Sorting by the wrong key** — activity selection by *start* time or *duration* is wrong; it must be *finish* time.
- **Ties and boundaries** — decide whether intervals that merely touch (`end == next.start`) count as overlapping.
- **Forgetting to reset state** — gas-station / Kadane patterns must reset the running accumulator at the right moment.

---

## Interview Tips

- State the greedy choice in one sentence, then **justify it** (exchange argument or "stays ahead"). Interviewers care about the *why*, not just the sweep.
- If you can quickly construct a counterexample, switch to DP and say so.
- Mention the sort cost — it usually sets the overall complexity.
- Common follow-up: "return the actual selected items," not just the count — keep indices while sweeping.

---

## Practice Problems

- **Easy:** Assign Cookies, Lemonade Change, Best Time to Buy and Sell Stock II
- **Medium:** Jump Game, Jump Game II, Gas Station, Partition Labels, Merge Intervals, Task Scheduler, Non-overlapping Intervals
- **Hard:** Candy, Minimum Number of Refueling Stops, Course Schedule III, IPO

---

## Summary

| Question | Greedy answer |
|----------|---------------|
| What's the greedy choice? | The locally best move (often after sorting) |
| Why is it correct? | Exchange argument / greedy stays ahead |
| What's the cost? | Usually O(n log n), dominated by the sort |
| When does it fail? | When a local choice blocks the global optimum → use DP |

Greedy = **sort, then commit**. Fast and elegant when the choice is provably safe — wrong when it isn't.
