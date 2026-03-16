"""
Searching Algorithms - Implementation and Examples
===============================================
Comprehensive Python implementations for searching algorithms
commonly asked in FAANG interviews.
"""

from typing import List, Optional


# =============================================================================
# SECTION 1: BINARY SEARCH VARIANTS
# =============================================================================

def binary_search(arr: List[int], target: int) -> int:
    """
    Classic binary search.

    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def binary_search_left(arr: List[int], target: int) -> int:
    """
    Find first occurrence of target (lower bound).

    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continue searching left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result


def binary_search_right(arr: List[int], target: int) -> int:
    """
    Find last occurrence of target (upper bound).

    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            result = mid
            left = mid + 1  # Continue searching right
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result


def lower_bound(arr: List[int], target: int) -> int:
    """
    Find first index where arr[i] >= target.

    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(arr)

    while left < right:
        mid = left + (right - left) // 2

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left


def upper_bound(arr: List[int], target: int) -> int:
    """
    Find first index where arr[i] > target.

    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(arr)

    while left < right:
        mid = left + (right - left) // 2

        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid

    return left


# =============================================================================
# SECTION 2: SEARCH IN ROTATED ARRAY
# =============================================================================

def search_rotated(arr: List[int], target: int) -> int:
    """
    Search in rotated sorted array.

    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid

        # Determine which half is sorted
        if arr[left] <= arr[mid]:
            # Left half sorted
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # Right half sorted
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


def find_min_rotated(arr: List[int]) -> int:
    """
    Find minimum element in rotated sorted array.

    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2

        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid

    return arr[left]


def find_pivot(arr: List[int]) -> int:
    """
    Find pivot (index of smallest element) in rotated array.

    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2

        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid

    return left


# =============================================================================
# SECTION 3: BINARY SEARCH ON ANSWER
# =============================================================================

def binary_search_unknown_range(low: int, high: int, is_valid) -> int:
    """
    Binary search when search space is unknown but monotonic.

    Time: O(log n), Space: O(1)
    """
    # Exponential search first to find range
    if low == -1:
        low = 0
        high = 1
        while not is_valid(high):
            high *= 2

    # Binary search in found range
    while low < high:
        mid = low + (high - low) // 2

        if is_valid(mid):
            high = mid
        else:
            low = mid + 1

    return low


def find_sqrt(x: int) -> int:
    """
    Find integer square root.

    Time: O(log n), Space: O(1)
    """
    left, right = 0, x

    while left <= right:
        mid = left + (right - left) // 2

        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
            result = mid
        else:
            right = mid - 1

    return result


def find_peak(arr: List[int]) -> int:
    """
    Find any peak element (element greater than neighbors).

    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2

        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left


# =============================================================================
# SECTION 4: TESTING
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("SEARCHING ALGORITHMS - TEST DEMO")
    print("=" * 60)

    # Test binary search
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 5
    print(f"\nBinary search {target} in {arr}: {binary_search(arr, target)}")

    # Test lower/upper bound
    arr = [1, 2, 2, 2, 3, 4, 5]
    print(f"Lower bound of 2: {binary_search_left(arr, 2)}")
    print(f"Upper bound of 2: {binary_search_right(arr, 2)}")

    # Test rotated array
    rotated = [4, 5, 6, 7, 0, 1, 2]
    print(f"\nSearch 0 in {rotated}: {search_rotated(rotated, 0)}")
    print(f"Search 3 in {rotated}: {search_rotated(rotated, 3)}")
    print(f"Min in {rotated}: {find_min_rotated(rotated)}")

    # Test sqrt
    print(f"\nSqrt of 16: {find_sqrt(16)}")
    print(f"Sqrt of 15: {find_sqrt(15)}")

    # Test peak
    arr = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    print(f"Peak in {arr}: index {find_peak(arr)}")

    print("\n" + "=" * 60)
    print("All tests completed!")
    print("=" * 60)
