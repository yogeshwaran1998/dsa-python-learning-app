# Stacks - Theory Guide

## Table of Contents
1. [What is a Stack?](#what-is-a-stack)
2. [Time Complexity](#time-complexity)
3. [Stack Variations](#stack-variations)
4. [Common Patterns](#common-patterns)
5. [Interview Tips](#interview-tips)

---

## What is a Stack?

A stack is a LIFO (Last In, First Out) data structure. Think of it like a stack of plates - you can only add or remove from the top.

### Operations
- **push**: Add element to top - O(1)
- **pop**: Remove element from top - O(1)
- **peek/top**: View top element without removing - O(1)
- **isEmpty**: Check if stack is empty - O(1)

### Visual Representation

A stack is **LIFO** (last in, first out): the most recently pushed element is the first one popped.

<div class="dsa-diagram dsa-diagram--col">
  <div class="dnode dnode--highlight"><span class="dcell">5</span><span class="dcell dcell--label">top (pushed last)</span></div>
  <div class="dnode"><span class="dcell">3</span></div>
  <div class="dnode"><span class="dcell">1</span><span class="dcell dcell--label">bottom (pushed first)</span></div>
  <div class="dsa-caption">push/pop/peek all act on the top in O(1).</div>
</div>

---

## Time Complexity

| Operation | Time | Space |
|-----------|------|-------|
| push | O(1) | O(n) total |
| pop | O(1) | O(n) total |
| peek | O(1) | O(n) total |
| isEmpty | O(1) | O(1) |
| search | O(n) | O(n) |

---

## Stack Variations

### 1. Monotonic Stack
A stack where elements are in monotonic (increasing or decreasing) order.

**Use Cases:**
- Next Greater/Smaller Element
- Largest Rectangle in Histogram
- Daily Temperatures

### 2. Min Stack
A stack that supports retrieving the minimum element in O(1).

**Implementation:**
- Use two stacks: main stack and min stack
- Push to min stack if <= current minimum

### 3. Stack with Max
Similar to Min Stack but for maximum element.

---

## Common Patterns

### 1. Valid Parentheses
Check if brackets are balanced: (), {}, []

### 2. Expression Evaluation
Evaluate arithmetic expressions: infix, prefix, postfix

### 3. Next Greater/Smaller Element
For each element, find next element that's greater/smaller.

### 4. Undo/Redo Operations
Use two stacks for undo/redo functionality.

### 5. Function Call Stack
Used by programming languages for recursion.

---

## Interview Tips

### FAANG Expectations
1. **O(1) space** when possible
2. **Handle edge cases**: empty input, single element
3. **Monotonic stack** is frequently asked

### Common Mistakes
1. Not checking for empty before pop
2. Not handling all bracket types
3. Off-by-one errors in indices

### Follow-up Questions
- "Can you do it with O(1) space?"
- "What about multiple types of brackets?"
- "How would you extend this for other bracket types?"

---

## Practice Problems

### Easy
- [x] Valid Parentheses
- [x] Min Stack
- [x] Implement Queue using Stacks

### Medium
- [x] Daily Temperatures
- [x] Next Greater Element II
- [x] Remove All Adjacent Duplicates in String
- [x] Asteroid Collision

### Hard
- [x] Trapping Rain Water
- [x] Largest Rectangle in Histogram
- [x] Validate Stack Sequences
