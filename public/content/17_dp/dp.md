# Dynamic Programming - Theory Guide

## What is Dynamic Programming?

DP is an optimization technique that solves problems by breaking them into overlapping subproblems.

## Key Properties

1. **Optimal Substructure**: Solution can be built from optimal solutions of subproblems
2. **Overlapping Subproblems**: Same subproblems solved multiple times

## Approaches

### 1. Top-Down (Memoization)
- Recursive with caching
- Start from main problem, recurse, cache results

### 2. Bottom-Up (Tabulation)
- Iterative, build from smallest subproblems
- Usually more efficient (no recursion overhead)

## Common DP Patterns

| Pattern | Example |
|---------|---------|
| 1D DP | Fibonacci, Climbing Stairs |
| 2D DP | Grid paths, LCS |
| Knapsack | 0/1 Knapsack |
| String DP | Edit Distance, LPS |

## Interview Tips

1. Identify if problem has optimal substructure
2. Define state clearly
3. Find recurrence relation
4. Decide top-down or bottom-up
5. Optimize space if needed
