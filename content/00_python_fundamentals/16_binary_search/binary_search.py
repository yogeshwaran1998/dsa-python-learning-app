"""
Binary Search Pattern - Implementation and Examples
=================================================
Comprehensive Python implementations of binary search patterns
commonly asked in FAANG interviews.

Topics covered:
1. Standard binary search
2. Lower and upper bounds
3. Bisect module
4. Search in rotated array
"""

from typing import List, Optional
import bisect


# =============================================================================
# SECTION 1: STANDARD BINARY SEARCH
# =============================================================================

def binary_search_basic(nums: List[int], target: int) -> int:
    """
    Basic binary search in sorted array.

    How it works:
    - Maintain search space [left, right]
    - Calculate mid point
    - If target found, return
    - If target > mid, search right half
    - Else search left half
    - Use left + (right - left) // 2 to avoid overflow

    Time: O(log n), Space: O(1)

    Args:
        nums: Sorted list of integers
        target: Target value to find

    Returns:
        Index of target if found, -1 otherwise

    Example:
        Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
        Output: 4
    """
    # Edge case: empty array
    if not nums:
        return -1

    # Initialize search boundaries
    left = 0
    right = len(nums) - 1

    # Continue while search space is valid
    # Using <= because we want to check both boundaries
    while left <= right:
        # Calculate middle index
        # Use left + (right - left) // 2 to avoid potential overflow
        # (not an issue in Python but good practice)
        mid = left + (right - left) // 2

        # Check if middle element is target
        if nums[mid] == target:
            return mid

        # Determine which half to search
        elif nums[mid] < target:
            # Target is in right half
            # Move left boundary past mid
            left = mid + 1
        else:
            # Target is in left half
            # Move right boundary before mid
            right = mid - 1

    # Target not found
    return -1


def binary_search_leftmost(nums: List[int], target: int) -> int:
    """
    Find leftmost (first) occurrence of target.
    Returns index of first element >= target if not exact match.

    How it works:
    - Similar to basic but keeps searching left after finding match
    - This finds the leftmost occurrence

    Time: O(log n), Space: O(1)

    Args:
        nums: Sorted list
        target: Target value

    Returns:
        Index of leftmost target, or insertion point if not found
    """
    if not nums:
        return -1

    left = 0
    right = len(nums) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            # Found target, but keep searching left
            result = mid
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result


def binary_search_rightmost(nums: List[int], target: int) -> int:
    """
    Find rightmost (last) occurrence of target.
    Returns index after last element <= target if not exact match.

    Time: O(log n), Space: O(1)
    """
    if not nums:
        return -1

    left = 0
    right = len(nums) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            # Found target, but keep searching right
            result = mid
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result


def search_insert_position(nums: List[int], target: int) -> int:
    """
    Find where to insert target in sorted array.
    Returns the index if target exists, otherwise returns insertion point.

    How it works:
    - Binary search for insertion point
    - When loop ends, left is the insertion point

    Time: O(log n), Space: O(1)

    Example:
        Input: nums = [1,3,5,6], target = 5
        Output: 2 (target is at index 2)
        Input: nums = [1,3,5,6], target = 4
        Output: 2 (should be inserted at index 2)
    """
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # left is now the insertion point
    return left


# =============================================================================
# SECTION 2: LOWER AND UPPER BOUNDS
# =============================================================================

def lower_bound(nums: List[int], target: int) -> int:
    """
    Find lower bound: first index where arr[i] >= target.
    Also known as "floor" of target.

    How it works:
    - When nums[mid] >= target, go left (right = mid - 1)
    - Keep track of best answer found so far

    Time: O(log n), Space: O(1)

    Args:
        nums: Sorted list
        target: Target value

    Returns:
        First index where arr[i] >= target, or len(nums) if not found

    Example:
        Input: [1, 2, 2, 2, 3], target = 2
        Output: 1 (first index where value >= 2)
    """
    if not nums:
        return 0

    left = 0
    right = len(nums)
    # Note: right starts at len (exclusive)

    # Binary search variant: right = len (exclusive)
    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] >= target:
            # This could be answer, but check left side
            right = mid
        else:
            # nums[mid] < target, need to go right
            left = mid + 1

    return left


def upper_bound(nums: List[int], target: int) -> int:
    """
    Find upper bound: first index where arr[i] > target.
    Also known as "ceiling" of target + 1.

    How it works:
    - When nums[mid] > target, go left
    - Different from lower_bound in comparison

    Time: O(log n), Space: O(1)

    Example:
        Input: [1, 2, 2, 2, 3], target = 2
        Output: 4 (first index where value > 2)
    """
    if not nums:
        return 0

    left = 0
    right = len(nums)

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] > target:
            # This could be answer
            right = mid
        else:
            # nums[mid] <= target, need to go right
            left = mid + 1

    return left


def first_and_last_position(nums: List[int], target: int) -> List[int]:
    """
    Find first and last position of target in sorted array.
    If not found, return [-1, -1].

    How it works:
    - Use lower_bound to find first position
    - Use upper_bound to find last position (then -1)

    Time: O(log n), Space: O(1)

    Example:
        Input: [5,7,7,8,8,10], target = 8
        Output: [3, 4]
    """
    if not nums:
        return [-1, -1]

    # Find first occurrence using lower_bound
    first = lower_bound(nums, target)

    # Check if target exists at first position
    if first == len(nums) or nums[first] != target:
        return [-1, -1]

    # Find last occurrence using upper_bound
    last = upper_bound(nums, target) - 1

    return [first, last]


# =============================================================================
# SECTION 3: BISECT MODULE
# =============================================================================

def bisect_examples():
    """
    Demonstrate Python's bisect module functions.

    How it works:
    - bisect_left: Find leftmost insertion point
    - bisect_right: Find rightmost insertion point
    - bisect: Alias for bisect_right
    """
    # Sorted list
    a = [1, 2, 2, 2, 3, 4, 5]

    # bisect_left: leftmost position where to insert
    # Returns index of first element >= x
    pos_left = bisect.bisect_left(a, 2)
    print(f"bisect_left(a, 2): {pos_left}")  # 1

    # bisect_right: rightmost position where to insert
    # Returns index after last element <= x
    pos_right = bisect.bisect_right(a, 2)
    print(f"bisect_right(a, 2): {pos_right}")  # 4

    # bisect is alias for bisect_right
    pos = bisect.bisect(a, 2)
    print(f"bisect(a, 2): {pos}")  # 4

    # Use case: counting occurrences
    count = pos_right - pos_left
    print(f"Count of 2: {count}")  # 3


def bisect_insert():
    """
    Use bisect to insert elements while maintaining sorted order.
    """
    import bisect

    # Start with empty list
    sorted_list = []

    # Insert elements in random order
    elements = [5, 2, 8, 1, 9, 3]

    for elem in elements:
        # Find insertion point
        pos = bisect.bisect_left(sorted_list, elem)
        # Insert at that position
        sorted_list.insert(pos, elem)
        print(f"Inserted {elem}: {sorted_list}")

    print(f"Final sorted list: {sorted_list}")


# =============================================================================
# SECTION 4: SEARCH IN ROTATED ARRAY
# =============================================================================

def search_rotated_array(nums: List[int], target: int) -> int:
    """
    Search in sorted but rotated array.
    Array was sorted then rotated at some pivot.

    How it works:
    - Modified binary search
    - At each step, determine which half is sorted
    - Check if target is in sorted half

    Time: O(log n), Space: O(1)

    Args:
        nums: Sorted array rotated at some pivot
        target: Target to find

    Returns:
        Index of target if found, -1 otherwise

    Example:
        Input: nums = [4,5,6,7,0,1,2], target = 0
        Output: 4
    """
    if not nums:
        return -1

    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        # Found target
        if nums[mid] == target:
            return mid

        # Determine which half is sorted
        # Check if left half is sorted
        if nums[left] <= nums[mid]:
            # Left half is sorted (normal order)
            # Check if target is in left half
            if nums[left] <= target < nums[mid]:
                # Target in left half, search there
                right = mid - 1
            else:
                # Target in right half
                left = mid + 1
        else:
            # Right half is sorted
            # Check if target is in right half
            if nums[mid] < target <= nums[right]:
                # Target in right half
                left = mid + 1
            else:
                # Target in left half
                right = mid - 1

    return -1


def search_rotated_array_with_duplicates(nums: List[int], target: int) -> bool:
    """
    Search in rotated array that may have duplicates.
    Slightly modified - may need O(n) in worst case.

    How it works:
    - Same as without duplicates
    - But when left, mid, right are equal, shrink search space

    Time: O(log n) average, O(n) worst case

    Example:
        Input: nums = [2,2,2,3,4,1,2], target = 3
        Output: True
    """
    if not nums:
        return False

    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return True

        # Handle duplicates - shrink search space
        if nums[left] == nums[mid] == nums[right]:
            left += 1
            right -= 1
        elif nums[left] <= nums[mid]:
            # Left half sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # Right half sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return False


def find_minimum_in_rotated_array(nums: List[int]) -> int:
    """
    Find minimum element in rotated sorted array.

    How it works:
    - Modified binary search
    - Minimum is the only element where previous > current
    - It's at the "pivot" point
    - If array not rotated (sorted), minimum is at index 0

    Time: O(log n), Space: O(1)

    Example:
        Input: [4,5,6,7,0,1,2]
        Output: 0
    """
    if not nums:
        return -1

    # Edge case: not rotated
    if nums[0] <= nums[-1]:
        return nums[0]

    left = 0
    right = len(nums) - 1

    # Binary search
    while left < right:
        mid = left + (right - left) // 2

        # Check if mid is the minimum
        # If mid > mid+1, then mid+1 is minimum
        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]

        # If mid-1 > mid, then mid is minimum
        if nums[mid - 1] > nums[mid]:
            return nums[mid]

        # Decide which half to search
        if nums[mid] > nums[left]:
            # Minimum is in right half
            left = mid + 1
        else:
            # Minimum is in left half (including mid)
            right = mid - 1

    return nums[left]


def find_rotation_count(nums: List[int]) -> int:
    """
    Find how many times the array was rotated.
    (Index of minimum element)

    Time: O(log n), Space: O(1)

    Example:
        Input: [4,5,6,7,0,1,2]
        Output: 4 (index of 0)
    """
    if not nums:
        return 0

    # Not rotated
    if nums[0] <= nums[-1]:
        return 0

    left = 0
    right = len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        # Check if mid is the pivot
        if nums[mid] > nums[mid + 1]:
            return mid + 1

        # Decide which half
        if nums[mid] >= nums[left]:
            # Left half is sorted, go right
            left = mid + 1
        else:
            # Right half is not sorted, go left
            right = mid - 1

    return left


# =============================================================================
# SECTION 5: BINARY SEARCH ON ANSWER
# =============================================================================

def binary_search_on_answer():
    """
    Binary search can be used to find answers in monotonic functions.

    Example problems:
    - Find square root
    - Find k-th element
    - Find capacity to ship packages
    """


def my_sqrt(x: int) -> int:
    """
    Find integer square root of a non-negative integer.

    How it works:
    - Binary search on possible answers [0, x]
    - Find largest number whose square <= x

    Time: O(log n), Space: O(1)
    """
    if x < 0:
        raise ValueError("Square root not defined for negative numbers")
    if x == 0 or x == 1:
        return x

    left = 1
    right = x

    while left <= right:
        mid = left + (right - left) // 2

        # Check if mid is the square root
        if mid == x // mid:
            return mid
        elif mid < x // mid:
            # Mid could be larger, search right
            left = mid + 1
            answer = mid
        else:
            # Mid is too large, search left
            right = mid - 1

    return answer


def find_pythagorean_triples(n: int) -> List[List[int]]:
    """
    Find all Pythagorean triples with a <= n.
    Uses binary search for b value.

    Note: This is just an example of binary search application.
    """
    # Simple approach: a^2 + b^2 = c^2
    result = []

    # a from 1 to n
    for a in range(1, n + 1):
        # b from a to n (to avoid duplicates)
        for b in range(a, n + 1):
            # c^2 = a^2 + b^2
            c_squared = a*a + b*b
            c = int(math.sqrt(c_squared))

            if c <= n and c*c == c_squared:
                result.append([a, b, c])

    return result


# =============================================================================
# SECTION 6: PEAK ELEMENT PROBLEMS
# =============================================================================

def find_peak_element(nums: List[int]) -> int:
    """
    Find a peak element (greater than neighbors).
    Array may have multiple peaks, return any one.

    How it works:
    - Binary search
    - If mid is peak, return
    - If mid < mid+1, peak is to the right
    - Else peak is to the left (or at mid)

    Time: O(log n), Space: O(1)

    Example:
        Input: [1,2,3,1]
        Output: 2 (index of 3)
    """
    if not nums:
        return -1

    left = 0
    right = len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        # Check if mid is peak
        # If mid > mid+1, there's a peak on left (including mid)
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            # Peak must be on right
            left = mid + 1

    return left


def find_peak_2d(grid: List[List[int]]) -> List[int]:
    """
    Find a peak in 2D grid where element is greater than all neighbors.
    Uses binary search on columns.

    Time: O(n log m) where n = rows, m = columns

    Args:
        grid: 2D matrix

    Returns:
        [row, col] of a peak element
    """
    if not grid or not grid[0]:
        return [-1, -1]

    rows = len(grid)
    cols = len(grid[0])

    # Binary search on columns
    left = 0
    right = cols - 1

    while left <= right:
        mid = left + (right - left) // 2

        # Find max element in this column
        max_row = 0
        for r in range(rows):
            if grid[r][mid] > grid[max_row][mid]:
                max_row = r

        # Check neighbors
        current = grid[max_row][mid]

        # Check left neighbor
        if mid > 0 and grid[max_row][mid - 1] > current:
            right = mid - 1
        # Check right neighbor
        elif mid < cols - 1 and grid[max_row][mid + 1] > current:
            left = mid + 1
        else:
            # Found peak
            return [max_row, mid]

    # Fallback
    return [0, 0]


# =============================================================================
# TEST FUNCTIONS
# =============================================================================

def run_tests():
    """Run test cases for all implementations."""

    # Test basic binary search
    nums = [-1, 0, 3, 5, 9, 12]
    result = binary_search_basic(nums, 9)
    print(f"Binary Search: {result}")  # 4

    # Test search insert position
    result = search_insert_position([1, 3, 5, 6], 5)
    print(f"Search Insert Position: {result}")  # 2

    # Test first and last position
    result = first_and_last_position([5, 7, 7, 8, 8, 10], 8)
    print(f"First and Last: {result}")  # [3, 4]

    # Test lower and upper bound
    arr = [1, 2, 2, 2, 3]
    print(f"Lower bound: {lower_bound(arr, 2)}")  # 1
    print(f"Upper bound: {upper_bound(arr, 2)}")  # 4

    # Test rotated array search
    nums = [4, 5, 6, 7, 0, 1, 2]
    result = search_rotated_array(nums, 0)
    print(f"Search Rotated: {result}")  # 4

    # Test find minimum in rotated
    result = find_minimum_in_rotated_array([4, 5, 6, 7, 0, 1, 2])
    print(f"Find Minimum: {result}")  # 0

    # Test find peak
    result = find_peak_element([1, 2, 3, 1])
    print(f"Find Peak: {result}")  # 2


if __name__ == "__main__":
    import math
    run_tests()
