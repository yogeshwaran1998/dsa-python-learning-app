"""
Heaps Pattern - Implementation and Examples
=========================================
Comprehensive Python implementations of heap patterns
commonly asked in FAANG interviews.

Topics covered:
1. heapq module usage
2. Min/max heap operations
3. Top K problems
4. Kth largest/smallest problems
"""

import heapq
from typing import List, Optional


# =============================================================================
# SECTION 1: HEAPQ BASICS
# =============================================================================

def heapq_basics():
    """
    Demonstrate basic heapq operations.

    heapq implements a min-heap.
    Key operations:
    - heappush: Push item onto heap
    - heappop: Pop smallest item
    - heapify: Transform list into heap
    """
    # Create empty heap
    heap = []

    # Push items onto heap
    # Items are ordered by their natural order
    for item in [5, 2, 8, 1, 9]:
        heapq.heappush(heap, item)
        print(f"Pushed {item}, heap: {heap}")

    # Pop items from heap (gets smallest first)
    print("\nPopping from heap:")
    while heap:
        item = heapq.heappop(heap)
        print(f"Popped {item}, remaining: {heap}")

    # Using heapify - transform existing list
    print("\nUsing heapify:")
    arr = [5, 2, 8, 1, 9]
    heapq.heapify(arr)
    print(f"Heapified array: {arr}")
    # Note: heap property is maintained but array is not sorted!


def heap_peek():
    """
    Peek at smallest element without removing.
    """
    heap = [1, 2, 3, 4, 5]
    heapq.heapify(heap)

    # Peek using index 0
    smallest = heap[0]
    print(f"Smallest element (peek): {smallest}")


# =============================================================================
# SECTION 2: MIN AND MAX HEAPS
# =============================================================================

def max_heap_example():
    """
    Python's heapq is min-heap.
    To get max-heap behavior, use negative numbers.
    """
    # Simulate max-heap using negative values
    heap = []

    # Push max values by storing negatives
    values = [5, 2, 8, 1, 9]
    for val in values:
        heapq.heappush(heap, -val)  # Store negative

    print("Max-heap (using negatives):")
    while heap:
        val = -heapq.heappop(heap)  # Negate back
        print(f"Popped: {val}")


def find_smallest_k_elements(nums: List[int], k: int) -> List[int]:
    """
    Find K smallest elements in array.

    How it works:
    - Use min-heap
    - If heap size > k, pop smallest
    - Result: heap contains k smallest

    Time: O(n log k), Space: O(k)

    Args:
        nums: Input array
        k: Number of smallest elements

    Returns:
        List of k smallest elements

    Example:
        Input: nums = [1, 5, 2, 8, 3, 9], k = 3
        Output: [1, 2, 3] (order may vary)
    """
    if k == 0:
        return []

    # Use min-heap of size k
    heap = []

    for num in nums:
        heapq.heappush(heap, num)

        # If heap exceeds k, remove smallest
        if len(heap) > k:
            heapq.heappop(heap)

    return list(heap)


def find_largest_k_elements(nums: List[int], k: int) -> List[int]:
    """
    Find K largest elements using max-heap (negation).

    Time: O(n log k), Space: O(k)

    Example:
        Input: nums = [1, 5, 2, 8, 3, 9], k = 3
        Output: [8, 9, 5] (order may vary)
    """
    if k == 0:
        return []

    heap = []

    for num in nums:
        # Store negative for max-heap behavior
        heapq.heappush(heap, -num)

        if len(heap) > k:
            heapq.heappop(heap)

    # Convert back to positive
    return [-x for x in heap]


# =============================================================================
# SECTION 3: TOP K PROBLEMS
# =============================================================================

def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    Find k most frequent elements.

    How it works:
    - First count frequencies
    - Use min-heap of size k
    - Keep top k frequent elements

    Time: O(n log k), Space: O(n)

    Args:
        nums: Input array
        k: Number of most frequent elements

    Returns:
        List of k most frequent elements

    Example:
        Input: nums = [1,1,1,2,2,3], k = 2
        Output: [1, 2]
    """
    from collections import Counter

    # Count frequencies
    freq = Counter(nums)

    # Use min-heap with (frequency, number)
    # Keep k most frequent
    heap = []

    for num, count in freq.items():
        heapq.heappush(heap, (count, num))

        if len(heap) > k:
            heapq.heappop(heap)

    # Extract from heap (in increasing frequency order)
    result = []
    while heap:
        count, num = heapq.heappop(heap)
        result.append(num)

    return result


def k_closest_points(points: List[List[int]], k: int) -> List[List[int]]:
    """
    Find k closest points to origin (0, 0).

    How it works:
    - Calculate distance (squared to avoid sqrt)
    - Use max-heap of size k
    - Keep k closest points

    Time: O(n log k), Space: O(k)

    Args:
        points: List of [x, y] coordinates
        k: Number of closest points

    Returns:
        List of k closest points

    Example:
        Input: points = [[1,3],[-2,2]], k = 1
        Output: [[-2,2]]
    """
    # Use max-heap (store negative distance)
    heap = []

    for point in points:
        x, y = point
        dist = x*x + y*y  # Squared distance (same ordering as actual)

        # Store as (negative distance, point) for max-heap
        heapq.heappush(heap, (-dist, point))

        if len(heap) > k:
            heapq.heappop(heap)

    # Extract points
    result = []
    while heap:
        dist, point = heapq.heappop(heap)
        result.append(point)

    return result


def top_k_longest_sentences(lines: List[str], k: int) -> List[str]:
    """
    Find k longest sentences (by word count).

    How it works:
    - Count words in each line
    - Use min-heap of size k
    """
    heap = []

    for line in lines:
        word_count = len(line.split())

        # Store as (word_count, line)
        heapq.heappush(heap, (word_count, line))

        if len(heap) > k:
            heapq.heappop(heap)

    # Extract (largest first by popping all)
    result = []
    while heap:
        count, line = heapq.heappop(heap)
        result.append(line)

    return result[::-1]  # Reverse to get largest first


# =============================================================================
# SECTION 4: KTH LARGEST/SMALLEST
# =============================================================================

def kth_largest_element(nums: List[int], k: int) -> int:
    """
    Find kth largest element in array.

    How it works:
    - Use min-heap of first k elements
    - Process remaining, replace if larger

    Time: O(n log k), Space: O(k)

    Args:
        nums: Input array
        k: Position from largest (1-indexed)

    Returns:
        Kth largest element

    Example:
        Input: nums = [3,2,1,5,6,4], k = 2
        Output: 5 (2nd largest)
    """
    if k <= 0 or k > len(nums):
        return -1

    # Build min-heap of first k elements
    heap = nums[:k]
    heapq.heapify(heap)

    # Process remaining elements
    for num in nums[k:]:
        # If current element is larger than smallest in heap, replace
        if num > heap[0]:
            heapq.heapreplace(heap, num)

    # heap[0] is kth largest
    return heap[0]


def kth_smallest_element(nums: List[int], k: int) -> int:
    """
    Find kth smallest element using max-heap.

    Time: O(n log k), Space: O(k)

    Example:
        Input: nums = [3,2,1,5,6,4], k = 2
        Output: 2
    """
    if k <= 0 or k > len(nums):
        return -1

    # Use max-heap (negate values)
    heap = []

    for num in nums:
        heapq.heappush(heap, -num)

        if len(heap) > k:
            heapq.heappop(heap)

    # -heap[0] is kth smallest
    return -heap[0]


def kth_smallest_matrix(mat: List[List[int]], k: int) -> int:
    """
    Find kth smallest element in n x n matrix.
    Matrix has rows sorted in ascending order.

    How it works:
    - Use min-heap with (value, row, col)
    - Start with first element of each row
    - Pop k times

    Time: O(k log n), Space: O(n)

    Example:
        Input: mat = [[1,5,9],[10,11,13],[12,13,15]], k = 8
        Output: 13
    """
    n = len(mat)

    # Use min-heap with (value, row, col)
    # Start with first column
    heap = [(mat[i][0], i, 0) for i in range(n)]
    heapq.heapify(heap)

    # Pop k times
    for _ in range(k - 1):
        val, row, col = heapq.heappop(heap)

        # Push next element in same row if exists
        if col + 1 < n:
            heapq.heappush(heap, (mat[row][col + 1], row, col + 1))

    # kth smallest
    return heap[0][0]


# =============================================================================
# SECTION 5: MERGING SORTED SEQUENCES
# =============================================================================

def merge_k_sorted_arrays(arrays: List[List[int]]) -> List[int]:
    """
    Merge k sorted arrays into one sorted array.

    How it works:
    - Use min-heap to track smallest elements
    - Push first element from each array
    - Pop smallest, push next from same array
    - Repeat until heap empty

    Time: O(N log k), Space: O(k)
    Where N = total elements, k = number of arrays

    Args:
        arrays: List of sorted arrays

    Returns:
        Merged sorted array

    Example:
        Input: [[1,4,7],[2,5,8],[3,6,9]]
        Output: [1,2,3,4,5,6,7,8,9]
    """
    # Edge case
    if not arrays:
        return []

    # Use min-heap with (value, array_index, element_index)
    heap = []

    # Push first element from each array
    for i, arr in enumerate(arrays):
        if arr:  # Skip empty arrays
            heapq.heappush(heap, (arr[0], i, 0))

    result = []

    # Process heap
    while heap:
        val, arr_idx, elem_idx = heapq.heappop(heap)
        result.append(val)

        # Push next element from same array
        if elem_idx + 1 < len(arrays[arr_idx]):
            next_val = arrays[arr_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, arr_idx, elem_idx + 1))

    return result


def merge_k_sorted_lists(lists: List[Optional[List[int]]]) -> List[int]:
    """
    Merge k sorted linked lists (simulated as arrays).

    Similar to above but handles None lists.
    """
    heap = []

    # Push first element from each non-null list
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))

    result = []

    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)

        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))

    return result


# =============================================================================
# SECTION 6: MEDIAN PROBLEMS
# =============================================================================

class MedianFinder:
    """
    Find median of running data stream.

    How it works:
    - Use two heaps: max-heap for lower half, min-heap for upper half
    - Balance sizes: max-heap has equal or one more element
    - Median: top of max-heap (if sizes differ) or average

    Time: O(n log n), Space: O(n)

    Example:
        addNum(1), addNum(2), addNum(3) -> median = 2
        addNum(4) -> median = (2+3)/2 = 2.5
    """

    def __init__(self):
        """
        Initialize median finder.
        """
        # Max-heap for lower half (store negatives)
        self.lower = []  # max-heap (negated values)

        # Min-heap for upper half
        self.upper = []  # min-heap

    def add_num(self, num: float) -> None:
        """
        Add a number to data stream.
        """
        # Add to max-heap first (negate for max behavior)
        heapq.heappush(self.lower, -num)

        # Balance: move largest from lower to upper
        heapq.heappush(self.upper, -heapq.heappop(self.lower))

        # Ensure lower has >= elements as upper
        if len(self.lower) < len(self.upper):
            heapq.heappush(self.lower, -heapq.heappop(self.upper))

    def find_median(self) -> float:
        """
        Return median of current data stream.
        """
        if len(self.lower) > len(self.upper):
            # Odd count: median is top of lower heap
            return -self.lower[0]
        else:
            # Even count: average of both tops
            return (-self.lower[0] + self.upper[0]) / 2


def running_median_stream():
    """
    Demonstrate running median with MedianFinder.
    """
    finder = MedianFinder()

    numbers = [5, 15, 1, 3, 8, 7, 9, 2]

    for num in numbers:
        finder.add_num(num)
        median = finder.find_median()
        print(f"Added {num}, median: {median}")


# =============================================================================
# SECTION 7: SLIDING WINDOW MEDIAN
# =============================================================================

def sliding_window_median(nums: List[int], k: int) -> List[float]:
    """
    Find median of each sliding window of size k.

    How it works:
    - Use balanced BST approach or maintain sorted window
    - For each position, calculate median

    Time: O(n log k), Space: O(k)

    Example:
        Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
        Output: [1, -1, -1, 3, 5, 6]
    """
    if not nums or k > len(nums):
        return []

    # Use two heaps with lazy deletion
    # lower: max-heap (lower half), upper: min-heap (upper half)
    lower = []  # max-heap (store negatives)
    upper = []  # min-heap
    to_remove = {}  # lazy deletion map

    result = []

    for i, num in enumerate(nums):
        # Add new number
        heapq.heappush(lower, -num)

        # Balance
        heapq.heappush(upper, -heapq.heappop(lower))

        if len(lower) < len(upper):
            heapq.heappush(lower, -heapq.heappop(upper))

        # Remove element that slides out of window
        if i >= k:
            out_num = nums[i - k]

            # Mark for lazy deletion
            to_remove[out_num] = to_remove.get(out_num, 0) + 1

            # Clean heaps if needed
            while lower and to_remove.get(-lower[0], 0) > 0:
                to_remove[-lower[0]] -= 1
                if to_remove[-lower[0]] == 0:
                    del to_remove[-lower[0]]
                heapq.heappop(lower)

            while upper and to_remove.get(upper[0], 0) > 0:
                to_remove[upper[0]] -= 1
                if to_remove[upper[0]] == 0:
                    del to_remove[upper[0]]
                heapq.heappop(upper)

        # Record median when window is full
        if i >= k - 1:
            if len(lower) > len(upper):
                median = -lower[0]
            else:
                median = (-lower[0] + upper[0]) / 2
            result.append(median)

    return result


# =============================================================================
# SECTION 8: PRIORITY QUEUE PATTERNS
# =============================================================================

class KthLargest:
    """
    Kth Largest element in a stream.
    LeetCode 703 problem.
    """

    def __init__(self, k: int, nums: List[int]):
        """
        Initialize with k and initial array.
        """
        self.k = k
        self.heap = []

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        """
        Add value and return kth largest.
        """
        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]


# =============================================================================
# TEST FUNCTIONS
# =============================================================================

def run_tests():
    """Run test cases for all implementations."""

    # Test smallest k elements
    result = find_smallest_k_elements([1, 5, 2, 8, 3, 9], 3)
    print(f"Smallest 3: {result}")  # [1, 2, 3]

    # Test largest k elements
    result = find_largest_k_elements([1, 5, 2, 8, 3, 9], 3)
    print(f"Largest 3: {result}")  # [9, 8, 5]

    # Test kth largest
    result = kth_largest_element([3, 2, 1, 5, 6, 4], 2)
    print(f"2nd Largest: {result}")  # 5

    # Test top k frequent
    result = top_k_frequent([1, 1, 1, 2, 2, 3], 2)
    print(f"Top 2 Frequent: {result}")  # [1, 2]

    # Test merge k sorted arrays
    arrays = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    result = merge_k_sorted_arrays(arrays)
    print(f"Merged: {result}")  # [1,2,3,4,5,6,7,8,9]

    # Test median finder
    print("\nRunning Median:")
    running_median_stream()

    # Test k closest points
    points = [[1, 3], [-2, 2], [2, -2]]
    result = k_closest_points(points, 2)
    print(f"2 Closest Points: {result}")


if __name__ == "__main__":
    run_tests()
