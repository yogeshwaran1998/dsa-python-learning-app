# Sorting Algorithms - Theory Guide

## Comparison of Sorting Algorithms

| Algorithm | Time (Avg) | Time (Worst) | Space | Stable |
|-----------|-----------|--------------|-------|--------|
| Bubble | O(n²) | O(n²) | O(1) | Yes |
| Selection | O(n²) | O(n²) | O(1) | No |
| Insertion | O(n²) | O(n²) | O(1) | Yes |
| Merge | O(n log n) | O(n log n) | O(n) | Yes |
| Quick | O(n log n) | O(n²) | O(log n) | No |
| Heap | O(n log n) | O(n log n) | O(1) | No |
| Counting | O(n+k) | O(n+k) | O(k) | Yes |
| Radix | O(nk) | O(nk) | O(n+k) | Yes |

## When to Use Which?

- **Small arrays**: Insertion Sort
- **Nearly sorted**: Insertion Sort
- **General purpose**: Quick Sort or Merge Sort
- **Integer keys**: Counting Sort or Radix Sort
- **Memory constrained**: Heap Sort or Quick Sort
- **Stable sort required**: Merge Sort

## Interview Tips

1. Know tradeoffs between algorithms
2. Understand when to use in-place vs stable
3. Consider time vs space tradeoffs
