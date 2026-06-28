# Two Pointers & Sliding Window - Theory Guide

## Part 1: Two Pointers

### What is Two Pointers?

A technique using two pointers to solve problems efficiently on sorted arrays or linked lists.

### Types

#### 1. Opposite Direction (Fast-Slow)
- One at start, one at end
- Move toward each other
- Use case: Finding pairs, partitioning

#### 2. Same Direction (Sliding Window)
- Both start at beginning
- One follows the other
- Use case: Removing duplicates

### Time Complexity
- **Time**: O(n) - typically single pass
- **Space**: O(1)

### Common Problems

| Problem | Approach |
|---------|----------|
| Pair sum in sorted | Opposite - inward |
| Remove duplicates | Same direction |
| Partition array | Opposite direction |
| Container with most water | Opposite - inward |
| 3Sum | Fix one, two pointers for rest |

---

## Part 2: Sliding Window

### What is Sliding Window?

A technique to process subarrays/substrings by maintaining a "window" that slides through the data.

### Types

#### 1. Fixed Window Size
```python
for i in range(len(arr) - k + 1):
    window = arr[i:i+k]
```

#### 2. Variable Window Size
- Expand window while condition is met
- Shrink window when condition breaks

### Time Complexity
- **Time**: O(n) - each element visited at most twice
- **Space**: O(1) or O(k)

### Common Problems

| Problem Type | Solution |
|-------------|----------|
| Maximum sum of k elements | Fixed window |
| Minimum subarray with sum >= k | Variable window |
| Longest substring with k distinct | Variable window |
| Count anagrams | Fixed window with frequency |

---

## When to Use What?

| Problem Type | Best Approach |
|-------------|---------------|
| Need pairs in sorted array | Two Pointers |
| Need unique elements | Two Pointers |
| Contiguous subarray problems | Sliding Window |
| String substring problems | Sliding Window |
| Finding middle in linked list | Fast-Slow Pointers |
| Cycle detection | Fast-Slow Pointers |

## Interview Tips

1. **Identify the pattern**: Is it about pairs or subarrays?
2. **Direction matters**: Choose correct pointer movement
3. **Edge cases**: Empty, single element, duplicates
4. **In-place operations**: Can avoid extra space
5. **For sliding window**: Decide fixed vs variable size first
