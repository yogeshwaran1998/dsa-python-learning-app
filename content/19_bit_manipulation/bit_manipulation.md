# Bit Manipulation - Theory Guide

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

Bit manipulation operates directly on the binary representation of integers. It enables O(1) tricks (parity, power-of-two checks), compact **bitmask** state (subsets, visited sets), and constant-factor speedups. The key insight is that each operator acts on **all bits in parallel**.

---

## When to Use

- Working with **flags / sets of up to ~64 items** — represent a subset as the bits of one integer (a bitmask).
- "Find the unique number", "single number", or parity problems — **XOR** cancels pairs.
- Multiply/divide by powers of two, extract digits, or pack multiple small fields into one integer.
- DP over subsets (bitmask DP) where the state is "which elements are chosen."

---

## How It Works

Six operators, each acting bitwise:

| Operator | Name | Example | Use |
|----------|------|---------|-----|
| `&` | AND | `1 & 1 = 1` | mask / test bits |
| `\|` | OR | `1 \| 0 = 1` | set bits |
| `^` | XOR | `1 ^ 1 = 0` | toggle / cancel pairs |
| `~` | NOT | `~1 = -2` | flip all bits |
| `<<` | left shift | `1 << 3 = 8` | × 2ⁿ |
| `>>` | right shift | `8 >> 1 = 4` | ÷ 2ⁿ |

A byte viewed as bits (bit `i` has place value `2^i`):

<div class="dsa-diagram dsa-diagram--center">
  <div class="dnode">
    <span class="dcell dcell--label">b7</span>
    <span class="dcell dcell--label">b6</span>
    <span class="dcell dcell--label">b5</span>
    <span class="dcell dcell--label">b4</span>
    <span class="dcell dcell--label">b3</span>
    <span class="dcell dcell--label">b2</span>
    <span class="dcell dcell--label">b1</span>
    <span class="dcell dcell--label">b0</span>
  </div>
  <div class="dnode dnode--green">
    <span class="dcell">0</span>
    <span class="dcell">0</span>
    <span class="dcell">1</span>
    <span class="dcell">0</span>
    <span class="dcell">1</span>
    <span class="dcell">1</span>
    <span class="dcell">0</span>
    <span class="dcell">1</span>
  </div>
  <div class="dsa-caption">0b00101101 = 32 + 8 + 4 + 1 = 45. Bit i contributes 2^i when set.</div>
</div>

### XOR — the workhorse

XOR has three properties that solve a surprising number of problems:

- `a ^ a = 0` (a value cancels itself)
- `a ^ 0 = a` (identity)
- XOR is commutative and associative, so order doesn't matter.

So XOR-ing every element of an array where all values appear twice except one leaves exactly the unique value. See `single_number()`, and `missing_number()` for the index-vs-value variant.

### Two's complement

Negative integers use two's complement: `-n == ~n + 1`. This is why `~1 == -2`, and why right-shifting negatives needs care. Python integers are **arbitrary precision** (no fixed 32/64-bit width), so masking with `& 0xFFFFFFFF` is sometimes needed to emulate fixed-width behavior — see `add_without_plus()`, `reverse_bits()`.

---

## Complexity

Single bitwise ops are **O(1)** (on fixed-width integers). Algorithms that loop over bits are **O(number of bits)** = O(32) or O(64) ≈ O(1), or O(log n) in terms of the value.

| Task | Time |
|------|------|
| Get/set/clear/toggle a bit | O(1) |
| Count set bits (Brian Kernighan) | O(number of set bits) |
| Iterate all subsets of an n-bit mask | O(2ⁿ) |

---

## Core Patterns

| Pattern | Trick | Code reference |
|---------|-------|----------------|
| **Single bit ops** | `get/set/clear/update` with `1 << i` | `get_bit()`, `set_bit()`, `clear_bit()`, `update_bit()` |
| **Count set bits** | `n &= n - 1` drops the lowest set bit | `count_set_bits()`, `count_bits()` |
| **Power-of-two check** | `n > 0 and n & (n - 1) == 0` | `is_power_of_two()`, `is_power_of_four()` |
| **XOR pair cancel** | Unique element / missing number | `single_number()`, `single_number_ii()`, `missing_number()` |
| **Swap without temp** | `a ^= b; b ^= a; a ^= b` | `swap_bits()` |
| **Arithmetic via bits** | Add/subtract/multiply with shifts & carries | `add_without_plus()`, `multiply_without_star()`, `divide_without_slash()` |
| **Subset enumeration (bitmask)** | Each integer 0..2ⁿ−1 is a subset | `subsets()`, `gray_code()` |

The lowest set bit is `n & (-n)`; clearing it is `n & (n - 1)` — both appear constantly.

---

## Common Pitfalls

- **Operator precedence** — `&`, `|`, `^` bind *looser* than `==` and `+`. Always parenthesize: `(n & mask) == 0`, not `n & mask == 0`.
- **Power-of-two edge case** — `n & (n-1) == 0` is also true for `n == 0`; guard with `n > 0`.
- **Signed shifts / Python's big ints** — Python has no fixed width; emulate 32-bit with `& 0xFFFFFFFF` and convert back for negatives.
- **Off-by-one on bit index** — bit `i` is `1 << i`; the highest bit of a 32-bit int is index 31.
- **Confusing logical and bitwise** — `and`/`or` (boolean) vs `&`/`|` (bitwise) are different operators.

---

## Interview Tips

- When you see "appears once/twice/odd number of times" or "without using +/-/*", think XOR and bit tricks.
- Know `n & (n-1)` (clear lowest set bit) and `n & -n` (isolate lowest set bit) cold — they power many one-liners.
- For "all subsets," mention bitmask enumeration; for state-compression DP, mention bitmask DP.
- Common follow-ups: "do it in O(1) space", "count bits for all numbers 0..n" (`count_bits()` uses `dp[i] = dp[i>>1] + (i&1)`), "reverse the bits of a 32-bit integer."

---

## Practice Problems

- **Easy:** Number of 1 Bits, Single Number, Power of Two, Missing Number, Reverse Bits, Hamming Distance
- **Medium:** Single Number II, Subsets, Counting Bits, Sum of Two Integers, Gray Code, Bitwise AND of Numbers Range
- **Hard:** Maximum XOR of Two Numbers in an Array, Minimum Number of Flips, Concatenated Words (bitmask DP variants)

---

## Summary

| Trick | Expression |
|-------|------------|
| Get bit i | `(n >> i) & 1` |
| Set bit i | `n \| (1 << i)` |
| Clear bit i | `n & ~(1 << i)` |
| Clear lowest set bit | `n & (n - 1)` |
| Isolate lowest set bit | `n & (-n)` |
| Power of two? | `n > 0 and n & (n-1) == 0` |
| Cancel pairs | XOR everything |

Master XOR's cancellation, the two lowest-set-bit idioms, and bitmasks for subsets — that covers most interview bit problems.
