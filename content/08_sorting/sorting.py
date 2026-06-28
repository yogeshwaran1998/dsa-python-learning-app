"""
Sorting Algorithms - Implementation and Examples
=============================================
Comprehensive Python implementations for sorting algorithms
commonly asked in FAANG interviews.
"""

from typing import List


# =============================================================================
# SECTION 1: COMPARISON SORTS
# =============================================================================

def bubble_sort(arr: List[int]) -> List[int]:
    """
    Bubble Sort - repeatedly swap adjacent elements if in wrong order.

    Time: O(n²), Space: O(1), Stable: Yes
    """
    arr = arr.copy()
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr


def selection_sort(arr: List[int]) -> List[int]:
    """
    Selection Sort - find minimum and place at beginning.

    Time: O(n²), Space: O(1), Stable: No
    """
    arr = arr.copy()
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


def insertion_sort(arr: List[int]) -> List[int]:
    """
    Insertion Sort - insert each element into sorted portion.

    Time: O(n²), Space: O(1), Stable: Yes
    Best for: Nearly sorted arrays, online sorting
    """
    arr = arr.copy()
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


def merge_sort(arr: List[int]) -> List[int]:
    """
    Merge Sort - divide, conquer, merge.

    Time: O(n log n), Space: O(n), Stable: Yes
    """
    if len(arr) <= 1:
        return arr.copy()

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left: List[int], right: List[int]) -> List[int]:
    """Merge two sorted arrays."""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr: List[int]) -> List[int]:
    """
    Quick Sort - partition around pivot.

    Time: O(n log n), Space: O(log n), Stable: No
    """
    if len(arr) <= 1:
        return arr.copy()

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


def quick_sort_inplace(arr: List[int], low: int = 0, high: int = None) -> None:
    """In-place quick sort."""
    if high is None:
        high = len(arr) - 1

    if low < high:
        pi = partition(arr, low, high)
        quick_sort_inplace(arr, low, pi - 1)
        quick_sort_inplace(arr, pi + 1, high)


def partition(arr: List[int], low: int, high: int) -> int:
    """Partition using last element as pivot."""
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def heap_sort(arr: List[int]) -> List[int]:
    """
    Heap Sort - build max heap, extract elements.

    Time: O(n log n), Space: O(1), Stable: No
    """
    arr = arr.copy()
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr


def heapify(arr: List[int], n: int, i: int) -> None:
    """Heapify subtree rooted at index i."""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


# =============================================================================
# SECTION 2: LINEAR SORTS
# =============================================================================

def counting_sort(arr: List[int]) -> List[int]:
    """
    Counting Sort - for integer arrays in bounded range.

    Time: O(n + k), Space: O(k), Stable: Yes
    where k = max - min + 1
    """
    if not arr:
        return []

    min_val = min(arr)
    max_val = max(arr)
    k = max_val - min_val + 1

    count = [0] * k

    for num in arr:
        count[num - min_val] += 1

    # Prefix sum for stability
    for i in range(1, k):
        count[i] += count[i - 1]

    result = [0] * len(arr)

    for num in reversed(arr):
        result[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    return result


def bucket_sort(arr: List[float]) -> List[float]:
    """
    Bucket Sort - distribute into buckets, sort each, concatenate.

    Time: O(n + k), Space: O(n + k), Stable: Yes
    Best for: Uniformly distributed numbers
    """
    if not arr:
        return []

    n = len(arr)
    min_val, max_val = min(arr), max(arr)

    if min_val == max_val:
        return arr

    bucket_count = n
    buckets = [[] for _ in range(bucket_count)]

    for num in arr:
        idx = int((num - min_val) / (max_val - min_val) * (bucket_count - 1))
        buckets[idx].append(num)

    for bucket in buckets:
        bucket.sort()

    result = []
    for bucket in buckets:
        result.extend(bucket)

    return result


def radix_sort(arr: List[int]) -> List[int]:
    """
    Radix Sort - sort by each digit from least to most significant.

    Time: O(nk), Space: O(n + k), Stable: Yes
    where k = number of digits
    """
    if not arr:
        return []

    max_val = max(arr)

    exp = 1
    while max_val // exp > 0:
        counting_sort_digit(arr, exp)
        exp *= 10

    return arr


def counting_sort_digit(arr: List[int], exp: int) -> None:
    """Counting sort for specific digit."""
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for num in arr:
        digit = (num // exp) % 10
        count[digit] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1

    for i in range(n):
        arr[i] = output[i]


# =============================================================================
# SECTION 3: SORTING PROBLEMS
# =============================================================================

def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """Merge overlapping intervals."""
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])

    return merged


def insertion_sort_list(head) -> None:
    """Sort linked list using insertion sort."""
    if not head or not head.next:
        return

    dummy = ListNode(0)
    current = head

    while current:
        prev = dummy
        next_node = current.next

        while prev.next and prev.next.val < current.val:
            prev = prev.next

        current.next = prev.next
        prev.next = current
        current = next_node


# Definition for singly linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sort_colors(nums: List[int]) -> None:
    """
    Dutch National Flag - sort 0s, 1s, 2s in-place.

    Time: O(n), Space: O(1)
    """
    low = mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1


# =============================================================================
# SECTION 4: TESTING
# =============================================================================

if __name__ == "__main__":
    import time

    print("=" * 60)
    print("SORTING ALGORITHMS - TEST DEMO")
    print("=" * 60)

    test_arrays = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 8, 1, 9, 3, 7],
        [1, 2, 3, 4, 5],  # Already sorted
        [5, 4, 3, 2, 1],  # Reverse sorted
        [3, 3, 3, 1, 1, 2, 2]  # With duplicates
    ]

    for arr in test_arrays:
        print(f"\nOriginal: {arr}")
        print(f"Bubble: {bubble_sort(arr)}")
        print(f"Selection: {selection_sort(arr)}")
        print(f"Insertion: {insertion_sort(arr)}")
        print(f"Merge: {merge_sort(arr)}")
        print(f"Quick: {quick_sort(arr)}")
        print(f"Heap: {heap_sort(arr)}")

    # Test counting sort
    print("\n--- Counting Sort ---")
    arr = [4, 2, 2, 8, 3, 3, 1]
    print(f"Counting sort: {counting_sort(arr)}")

    # Test bucket sort
    print("\n--- Bucket Sort ---")
    arr = [0.9, 0.1, 0.5, 0.4, 0.3, 0.8, 0.7, 0.2, 0.6]
    print(f"Bucket sort: {bucket_sort(arr)}")

    # Test merge intervals
    print("\n--- Merge Intervals ---")
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(f"Merged: {merge_intervals(intervals)}")

    # Test sort colors
    print("\n--- Sort Colors ---")
    nums = [2, 0, 2, 1, 1, 0]
    sort_colors(nums)
    print(f"Sorted: {nums}")

    print("\n" + "=" * 60)
    print("All tests completed!")
    print("=" * 60)
