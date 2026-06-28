"""
Heaps/Priority Queues - Implementation and Examples
===================================================
Comprehensive Python implementations for heap problems
commonly asked in FAANG interviews.
"""

from typing import List, Optional
import heapq
from collections import defaultdict


# =============================================================================
# SECTION 1: HEAP IMPLEMENTATION
# =============================================================================

class MinHeap:
    """Min heap implementation using list."""

    def __init__(self):
        self.heap = []

    def push(self, val) -> None:
        heapq.heappush(self.heap, val)

    def pop(self):
        return heapq.heappop(self.heap)

    def peek(self) -> Optional:
        return self.heap[0] if self.heap else None

    def size(self) -> int:
        return len(self.heap)

    def is_empty(self) -> bool:
        return len(self.heap) == 0


class MaxHeap:
    """Max heap by negating values."""

    def __init__(self):
        self.heap = []

    def push(self, val) -> None:
        heapq.heappush(self.heap, -val)

    def pop(self):
        return -heapq.heappop(self.heap)

    def peek(self) -> Optional:
        return -self.heap[0] if self.heap else None


# =============================================================================
# SECTION 2: KTH LARGEST/SMALLEST
# =============================================================================

def find_kth_largest(nums: List[int], k: int) -> int:
    """
    Find kth largest element.

    Time: O(n log k), Space: O(k)
    """
    heap = []

    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]


def find_kth_smallest(nums: List[int], k: int) -> int:
    """
    Find kth smallest element.

    Time: O(n log k), Space: O(k)
    """
    # Use max-heap of size k
    heap = []

    for num in nums:
        heapq.heappush(heap, -num)
        if len(heap) > k:
            heapq.heappop(heap)

    return -heap[0]


def find_kth_largest_quickselect(nums: List[int], k: int) -> int:
    """
    Find kth largest using quickselect.

    Time: O(n) average, Space: O(1)
    """
    k = len(nums) - k  # Convert to (k+1)th smallest

    def quickselect(left, right):
        pivot = nums[right]
        p = left

        for i in range(left, right):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1

        nums[p], nums[right] = nums[right], nums[p]

        if p == k:
            return nums[p]
        elif p < k:
            return quickselect(p + 1, right)
        else:
            return quickselect(left, p - 1)

    return quickselect(0, len(nums) - 1)


# =============================================================================
# SECTION 3: TOP K FREQUENT
# =============================================================================

def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    Find top k frequent elements.

    Time: O(n log k), Space: O(n)
    """
    # Count frequencies
    freq = defaultdict(int)
    for num in nums:
        freq[num] += 1

    # Min-heap of size k
    heap = []

    for num, count in freq.items():
        heapq.heappush(heap, (count, num))
        if len(heap) > k:
            heapq.heappop(heap)

    return [num for count, num in sorted(heap, reverse=True)]


def top_k_frequent_bucket(nums: List[int], k: int) -> List[int]:
    """
    Find top k frequent using bucket sort.

    Time: O(n), Space: O(n)
    """
    if not nums:
        return []

    # Count frequencies
    freq = defaultdict(int)
    max_freq = 0
    for num in nums:
        freq[num] += 1
        max_freq = max(max_freq, freq[num])

    # Bucket sort by frequency
    buckets = [[] for _ in range(max_freq + 1)]
    for num, count in freq.items():
        buckets[count].append(num)

    # Get top k from highest frequency
    result = []
    for count in range(max_freq, 0, -1):
        for num in buckets[count]:
            result.append(num)
            if len(result) == k:
                return result

    return result


# =============================================================================
# SECTION 4: MERGE K SORTED
# =============================================================================

def merge_k_sorted_lists(lists: List[List[int]]) -> List[int]:
    """
    Merge k sorted lists.

    Time: O(N log k), Space: O(k)
    where N = total elements
    """
    heap = []
    result = []

    # Add first element from each list
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))

    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)

        # Add next element from same list
        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))

    return result


def merge_sorted_arrays(arrays: List[List[int]]) -> List[int]:
    """Merge multiple sorted arrays."""
    result = []
    heap = []

    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(heap, (arr[0], i, 0))

    while heap:
        val, arr_idx, elem_idx = heapq.heappop(heap)
        result.append(val)

        if elem_idx + 1 < len(arrays[arr_idx]):
            next_val = arrays[arr_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, arr_idx, elem_idx + 1))

    return result


# =============================================================================
# SECTION 5: MEDIAN DATA STREAM
# =============================================================================

class MedianFinder:
    """
    Median of data stream using two heaps.

    Time: O(n log n), Space: O(n)

    - max_heap: stores smaller half
    - min_heap: stores larger half
    """

    def __init__(self):
        self.max_heap = []  # Lower half (negated for max)
        self.min_heap = []  # Upper half

    def add_num(self, num: int) -> None:
        # Add to max_heap first
        heapq.heappush(self.max_heap, -num)

        # Balance: move largest from max to min
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        # Ensure max_heap has >= elements
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def find_median(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]

        return (-self.max_heap[0] + self.min_heap[0]) / 2


# =============================================================================
# SECTION 6: SLIDING WINDOW MEDIAN
# =============================================================================

def median_sliding_window(nums: List[int], k: int) -> List[float]:
    """
    Find median of each sliding window.

    Time: O(n log k), Space: O(k)
    """
    result = []
    max_heap = []  # Left half
    min_heap = []  # Right half

    def balance():
        # Ensure max_heap has one more or equal elements
        if len(max_heap) > len(min_heap) + 1:
            val = -heapq.heappop(max_heap)
            heapq.heappush(min_heap, val)
        elif max_heap and min_heap and -max_heap[0] > min_heap[0]:
            left = -heapq.heappop(max_heap)
            right = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -left)
            heapq.heappush(min_heap, right)

    def remove(val, heap, is_max=True):
        """Remove value from heap."""
        idx = heap.index(val)
        heap[idx] = heap[-1]
        heap.pop()

        if is_max:
            heapq._siftup_max(heap, idx)
            heapq._siftdown_max(heap, 0, idx)
        else:
            heapq.heapify(heap)

    for i in range(len(nums)):
        # Add current number
        if not max_heap or nums[i] <= -max_heap[0]:
            heapq.heappush(max_heap, -nums[i])
        else:
            heapq.heappush(min_heap, nums[i])

        balance()

        # Remove if window is full
        if i >= k:
            left_num = nums[i - k]
            if left_num <= -max_heap[0]:
                remove(left_num, max_heap, True)
            else:
                remove(left_num, min_heap, False)
            balance()

        # Record median when window is ready
        if i >= k - 1:
            if len(max_heap) > len(min_heap):
                result.append(float(-max_heap[0]))
            else:
                result.append((-max_heap[0] + min_heap[0]) / 2.0)

    return result


# =============================================================================
# SECTION 7: K CLOSEST POINTS
# =============================================================================

def k_closest_points(points: List[List[int]], k: int) -> List[List[int]]:
    """
    Find k closest points to origin.

    Time: O(n log k), Space: O(k)
    """
    heap = []

    for x, y in points:
        dist = x * x + y * y
        heapq.heappush(heap, (-dist, x, y))

        if len(heap) > k:
            heapq.heappop(heap)

    return [[x, y] for dist, x, y in heap]


# =============================================================================
# SECTION 8: TASK SCHEDULER WITH HEAP
# =============================================================================

def least_interval(tasks: List[str], n: int) -> int:
    """
    Minimum intervals with cooling period.

    Time: O(n log 26), Space: O(26)
    """
    from collections import Counter

    # Max frequency
    freq = [-c for c in Counter(tasks).values()]
    heapq.heapify(freq)

    time = 0
    cooldown = deque()  # (remaining_tasks, available_time)

    while heap or cooldown:
        time += 1

        if heap:
            tasks_remaining = heapq.heappop(heap) + 1
            if tasks_remaining != 0:
                cooldown.append((tasks_remaining, time + n))

        if cooldown and cooldown[0][1] == time:
            remaining, _ = cooldown.popleft()
            heapq.heappush(heap, remaining)

    return time


# =============================================================================
# SECTION 9: REORGANIZE STRING
# =============================================================================

def reorganize_string(s: str) -> str:
    """
    Rearrange characters so no two adjacent are same.

    Time: O(n log k), Space: O(k)
    """
    from collections import Counter

    freq = [(-count, char) for char, count in Counter(s).items()]
    heapq.heapify(freq)

    result = []
    prev_count, prev_char = 0, ''

    while freq:
        count, char = heapq.heappop(freq)
        result.append(char)

        # Add previous character back
        if prev_count < 0:
            heapq.heappush(freq, (prev_count, prev_char))

        # Update prev
        prev_count = count + 1  # One less occurrence
        prev_char = char

    return ''.join(result) if len(result) == len(s) else ""


# =============================================================================
# SECTION 10: TESTING AND DEMO
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("HEAP ALGORITHMS - TEST DEMO")
    print("=" * 60)

    # Test Kth Largest
    print("\n--- Kth Largest ---")
    nums = [3, 2, 1, 5, 6, 4]
    print(f"Array: {nums}")
    print(f"3rd largest: {find_kth_largest(nums, 3)}")
    print(f"2nd smallest: {find_kth_smallest(nums, 2)}")

    # Test Top K Frequent
    print("\n--- Top K Frequent ---")
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    result = top_k_frequent(nums, k)
    print(f"Top {k} frequent in {nums}: {result}")

    # Test Merge K Sorted
    print("\n--- Merge K Sorted ---")
    lists = [[1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 12]]
    result = merge_k_sorted_lists(lists)
    print(f"Merged {lists}: {result}")

    # Test Median Finder
    print("\n--- Median Finder ---")
    mf = MedianFinder()
    nums = [2, 1, 3, 5, 4]
    for n in nums:
        mf.add_num(n)
        print(f"Add {n}: median = {mf.find_median()}")

    # Test K Closest
    print("\n--- K Closest Points ---")
    points = [[1, 3], [-2, 2], [5, 8], [0, 1]]
    k = 2
    result = k_closest_points(points, k)
    print(f"Top {k} closest to origin: {result}")

    # Test Reorganize String
    print("\n--- Reorganize String ---")
    s = "aaabbc"
    result = reorganize_string(s)
    print(f"Reorganized '{s}': '{result}'")

    print("\n" + "=" * 60)
    print("All tests completed!")
    print("=" * 60)
