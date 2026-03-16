# Recursion - Theory Guide

## What is Recursion?

A function that calls itself to solve smaller subproblems.

## Key Components

1. **Base Case**: Condition to stop recursion
2. **Recursive Case**: Function calls itself with smaller input

## Recurrence Relations

| Problem | Recurrence |
|---------|-----------|
| Fibonacci | F(n) = F(n-1) + F(n-2) |
| Binary Search | T(n) = T(n/2) + O(1) |
| Merge Sort | T(n) = 2T(n/2) + O(n) |

## Space Complexity

Recursion uses call stack: O(depth) = O(n) worst case

## Interview Tips

- Always define base case first
- Make sure to reduce problem size
- Consider memoization for overlapping subproblems
