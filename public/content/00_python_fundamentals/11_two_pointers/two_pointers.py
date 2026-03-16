"""
Two Pointers Pattern - Implementation and Examples
===================================================
Comprehensive Python implementations of two pointers technique
commonly asked in FAANG interviews.

Topics covered:
1. Opposite direction two pointers
2. Same direction (slow-fast) pointers
3. Classic problems: remove duplicates, 3Sum, container with most water
"""

from typing import List, Tuple, Optional


# =============================================================================
# SECTION 1: OPPOSITE DIRECTION TWO POINTERS
# =============================================================================

def two_sum_sorted(arr: List[int], target: int) -> Tuple[int, int]:
    """
    Find two numbers that add up to target in a sorted array.
    Uses two pointers starting from opposite ends.

    How it works:
    - Left pointer starts at beginning, right at end
    - If sum is too small, move left pointer right (increase sum)
    - If sum is too large, move right pointer left (decrease sum)

    Time: O(n), Space: O(1)

    Args:
        arr: Sorted list of integers
        target: Target sum to find

    Returns:
        Tuple of indices (left_idx, right_idx) or empty tuple if not found

    Example:
        arr = [1, 2, 3, 4, 6], target = 6
        Returns (1, 4) because arr[1]=2 + arr[4]=4 = 6
    """
    # Initialize pointers at both ends of the array
    # Left pointer starts at the beginning (smallest element)
    # Right pointer starts at the end (largest element)
    left, right = 0, len(arr) - 1

    # Continue until pointers meet (all pairs checked)
    while left < right:
        # Calculate current sum of elements at both pointers
        current_sum = arr[left] + arr[right]

        # Found the target - return the indices
        if current_sum == target:
            return (left, right)

        # Sum is too small - need larger sum
        # Move left pointer right to get larger element
        elif current_sum < target:
            left += 1

        # Sum is too large - need smaller sum
        # Move right pointer left to get smaller element
        else:
            right -= 1

    # No pair found that sums to target
    return ()


def is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome (reads same forwards and backwards).
    Only considers alphanumeric characters, case-insensitive.

    How it works:
    - Use two pointers from start and end
    - Skip non-alphanumeric characters
    - Compare characters at both pointers

    Time: O(n), Space: O(1)

    Args:
        s: Input string to check

    Returns:
        True if palindrome, False otherwise

    Example:
        "A man, a plan, a canal: Panama" -> True
        "race a car" -> False
    """
    # Initialize pointers at both ends
    left, right = 0, len(s) - 1

    # Continue until pointers meet or cross
    while left < right:
        # Skip non-alphanumeric characters from left
        # isalnum() returns True for letters and numbers
        while left < right and not s[left].isalnum():
            left += 1

        # Skip non-alphanumeric characters from right
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare characters (case-insensitive)
        # Use lower() to convert to same case
        if s[left].lower() != s[right].lower():
            return False

        # Move both pointers toward center
        left += 1
        right -= 1

    # All characters matched - it's a palindrome
    return True


def container_with_most_water(height: List[int]) -> int:
    """
    Find the container that can hold the most water.
    Container is formed by two vertical lines at indices i and j,
    with width = j - i and height = min(height[i], height[j]).

    How it works:
    - Start with maximum width (pointers at both ends)
    - The limiting factor is the shorter line
    - Move the pointer with shorter line inward
    - This gives us a chance to find a taller line

    Time: O(n), Space: O(1)

    Args:
        height: List of non-negative integers representing heights of lines

    Returns:
        Maximum area of water container

    Example:
        height = [1,8,6,2,5,4,8,3,7]
        Maximum area is 49 (between indices 1 and 8)
        Width = 7, Height = min(8,7) = 7, Area = 49
    """
    # Edge case: need at least two lines
    if not height or len(height) < 2:
        return 0

    # Initialize pointers at both ends
    # Starting with maximum possible width
    left, right = 0, len(height) - 1

    # Track maximum area found so far
    max_area = 0

    # Continue until pointers meet
    while left < right:
        # Calculate width between the two lines
        width = right - left

        # Height is limited by the shorter line
        # Water would spill over the shorter side
        current_height = min(height[left], height[right])

        # Calculate area and update maximum
        max_area = max(max_area, width * current_height)

        # Key insight: move the pointer with shorter height
        # If we move the taller side, we can't get more height
        # (still limited by the shorter side) and we lose width
        if height[left] < height[right]:
            # Left side is shorter, move it inward
            left += 1
        else:
            # Right side is shorter or equal, move it inward
            right -= 1

    return max_area


def three_sum_closest(nums: List[int], target: int) -> int:
    """
    Find three numbers that sum closest to target.

    How it works:
    - Sort the array
    - Fix one element, use two pointers for remaining two
    - Track closest sum to target

    Time: O(n^2), Space: O(1) excluding sort

    Args:
        nums: List of integers
        target: Target sum

    Returns:
        Sum of three numbers closest to target
    """
    # Sort to enable two pointers approach
    nums.sort()
    n = len(nums)

    # Need at least 3 elements
    if n < 3:
        return 0

    # Initialize with first three elements as closest
    # (any valid initial value works)
    closest = nums[0] + nums[1] + nums[2]

    # Fix first element, iterate through array
    for i in range(n - 2):
        # Two pointers for remaining two elements
        left, right = i + 1, n - 1

        while left < right:
            # Calculate current sum
            current_sum = nums[i] + nums[left] + nums[right]

            # Update closest if this is better
            # (closer to target in absolute difference)
            if abs(current_sum - target) < abs(closest - target):
                closest = current_sum

            # Move pointers based on comparison with target
            if current_sum < target:
                # Sum too small, need larger value
                left += 1
            elif current_sum > target:
                # Sum too large, need smaller value
                right -= 1
            else:
                # Exact match found
                return target

    return closest


# =============================================================================
# SECTION 2: SAME DIRECTION (SLOW-FAST) TWO POINTERS
# =============================================================================

def remove_duplicates_sorted(arr: List[int]) -> int:
    """
    Remove duplicates from sorted array in-place.
    Returns the count of unique elements.

    How it works:
    - Slow pointer tracks position for next unique element
    - Fast pointer scans through array
    - When new element found, copy to slow position

    Time: O(n), Space: O(1)

    Args:
        arr: Sorted list with possible duplicates (modified in-place)

    Returns:
        Count of unique elements

    Example:
        Input: [1,1,1,2,2,3]
        After: [1,2,3,2,2,3] (first 3 elements are unique)
        Returns: 3
    """
    # Edge case: empty array
    if not arr:
        return 0

    # Slow pointer starts at index 0
    # This is where we'll place the next unique element
    slow = 0

    # Fast pointer starts at index 1
    # This scans through the array looking for new elements
    for fast in range(1, len(arr)):
        # Check if current element is different from previous unique
        # If different, it's a new unique element
        if arr[fast] != arr[slow]:
            # Move slow pointer to next position
            slow += 1

            # Copy the new unique element to slow position
            # This overwrites the duplicate
            arr[slow] = arr[fast]

    # Number of unique elements = slow position + 1
    # (since slow is 0-indexed)
    return slow + 1


def remove_element_sorted(arr: List[int], val: int) -> int:
    """
    Remove all occurrences of val from sorted array in-place.
    Returns count of elements that are not val.

    How it works:
    - Use slow-fast pattern
    - Fast pointer finds non-val elements
    - Slow pointer tracks where to place them

    Time: O(n), Space: O(1)

    Args:
        arr: Sorted list (modified in-place)
        val: Value to remove

    Returns:
        Count of elements not equal to val

    Example:
        Input: [1,2,2,2,3,4,5], val = 2
        After: [1,3,4,5,2,2,2] (first 4 elements are valid)
        Returns: 4
    """
    # Slow pointer tracks position for next valid element
    slow = 0

    # Fast pointer scans the array
    for fast in range(len(arr)):
        # If current element is not the value to remove
        if arr[fast] != val:
            # Place it at slow position
            arr[slow] = arr[fast]
            # Move slow pointer
            slow += 1

    # Return count of valid elements
    return slow


def move_zeros(arr: List[int]) -> None:
    """
    Move all zeros to the end of array while maintaining relative order
    of non-zero elements.

    How it works:
    - Use slow pointer to track position for next non-zero element
    - Fast pointer finds non-zero elements
    - After finding all non-zeros, fill remaining with zeros

    Time: O(n), Space: O(1)

    Args:
        arr: List of integers (modified in-place)
    """
    # Edge case: empty array
    if not arr:
        return

    # Slow pointer for position of next non-zero element
    slow = 0

    # Find all non-zero elements
    for fast in range(len(arr)):
        if arr[fast] != 0:
            # Place non-zero at slow position
            arr[slow] = arr[fast]
            slow += 1

    # Fill remaining positions with zeros
    while slow < len(arr):
        arr[slow] = 0
        slow += 1


def dutch_national_flag_partition(arr: List[int], pivot: int) -> int:
    """
    Partition array into three sections:
    - Elements less than pivot
    - Elements equal to pivot
    - Elements greater than pivot

    This is the Dutch National Flag problem (3-way partition).

    How it works:
    - Use three pointers: low, mid, high
    - Low tracks end of "less than" section
    - Mid tracks current element being processed
    - High tracks start of "greater than" section

    Time: O(n), Space: O(1)

    Args:
        arr: List of integers (modified in-place)
        pivot: Value to partition around

    Returns:
        Index range of elements equal to pivot (start, end+1)

    Example:
        Input: [2, 0, 2, 1, 1, 0], pivot = 1
        Output: [0, 0, 1, 1, 2, 2]
        Returns (2, 4) - indices 2 and 3 have value 1
    """
    # Initialize pointers
    # low: marks end of elements < pivot
    # mid: current element being processed
    # high: marks start of elements > pivot
    low, mid, high = 0, 0, len(arr) - 1

    # Process until mid crosses high
    while mid <= high:
        if arr[mid] < pivot:
            # Element less than pivot
            # Swap with low pointer position
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == pivot:
            # Element equal to pivot - already in correct section
            # Just move mid forward
            mid += 1
        else:
            # Element greater than pivot
            # Swap with high pointer position
            arr[mid], arr[high] = arr[high], arr[mid]
            # Don't increment mid - need to check swapped element
            high -= 1

    # Return range of elements equal to pivot
    return (low, high + 1)


# =============================================================================
# SECTION 3: CLASSIC INTERVIEW PROBLEMS
# =============================================================================

def three_sum(nums: List[List[int]]) -> List[List[int]]:
    """
    Find all unique triplets that sum to zero.

    How it works:
    - Sort the array
    - For each element, find pairs that sum to -element
    - Use two pointers to find pairs efficiently
    - Skip duplicates to avoid repeated triplets

    Time: O(n^2), Space: O(1) excluding output

    Args:
        nums: List of integers

    Returns:
        List of unique triplets summing to zero

    Example:
        Input: [-1, 0, 1, 2, -1, -4]
        Output: [[-1, -1, 2], [-1, 0, 1]]
    """
    # Sort to enable two pointers and skip duplicates easily
    nums.sort()
    result = []
    n = len(nums)

    # Need at least 3 elements
    if n < 3:
        return result

    # Fix first element of triplet
    for i in range(n - 2):
        # Skip duplicates for first element
        # If same as previous, skip to avoid duplicate triplets
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Use two pointers for remaining two elements
        left, right = i + 1, n - 1
        target = -nums[i]

        while left < right:
            # Calculate sum of current triplet
            current_sum = nums[left] + nums[right]

            if current_sum == target:
                # Found valid triplet
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicates for left pointer
                # Move past all elements with same value
                while left < right and nums[left] == nums[left + 1]:
                    left += 1

                # Skip duplicates for right pointer
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                # Move both pointers after finding match
                left += 1
                right -= 1

            elif current_sum < target:
                # Need larger sum, move left pointer right
                left += 1
            else:
                # Need smaller sum, move right pointer left
                right -= 1

    return result


def four_sum(nums: List[int], target: int) -> List[List[int]]:
    """
    Find all unique quadruplets that sum to target.

    How it works:
    - Similar to 3Sum but with one extra loop
    - Fix two elements, use two pointers for remaining

    Time: O(n^3), Space: O(1) excluding output

    Args:
        nums: List of integers
        target: Target sum

    Returns:
        List of unique quadruplets summing to target

    Example:
        Input: [1, 0, -1, 0, -2, 2, 0, 2], target = 0
        Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    """
    nums.sort()
    result = []
    n = len(nums)

    if n < 4:
        return result

    # Fix first two elements
    for i in range(n - 3):
        # Skip duplicates for first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, n - 2):
            # Skip duplicates for second element
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            # Two pointers for remaining two elements
            left, right = j + 1, n - 1
            current_target = target - nums[i] - nums[j]

            while left < right:
                current_sum = nums[left] + nums[right]

                if current_sum == current_target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])

                    # Skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif current_sum < current_target:
                    left += 1
                else:
                    right -= 1

    return result


def trapping_rain_water(height: List[int]) -> int:
    """
    Calculate how much water can be trapped between bars.

    How it works:
    - Water at each position = min(max_left, max_right) - height[i]
    - Use two pointers from ends
    - Track max height from each side

    Time: O(n), Space: O(1)

    Args:
        height: List of non-negative integers representing bar heights

    Returns:
        Total units of trapped water

    Example:
        Input: [0,1,0,2,1,0,1,3,2,1,2,1]
        Output: 6 (trapped in positions 2,4,5,6)
    """
    if not height or len(height) < 3:
        return 0

    # Initialize pointers at both ends
    left, right = 0, len(height) - 1

    # Track maximum height from left and right
    max_left, max_right = 0, 0

    # Track total water trapped
    water = 0

    # Process until pointers meet
    while left < right:
        # Determine which side has smaller height
        if height[left] < height[right]:
            # Left side is limiting factor
            # Check if current height is greater than max from left
            if height[left] >= max_left:
                # Update max height
                max_left = height[left]
            else:
                # Water can be trapped here
                water += max_left - height[left]

            # Move left pointer
            left += 1
        else:
            # Right side is limiting factor
            if height[right] >= max_right:
                max_right = height[right]
            else:
                water += max_right - height[right]

            # Move right pointer
            right -= 1

    return water


# =============================================================================
# SECTION 4: TWO POINTERS WITH HASHING
# =============================================================================

def find_subarray_with_sum(arr: List[int], target: int) -> List[int]:
    """
    Find continuous subarray that sums to target.
    Uses sliding window (special case of two pointers).

    Time: O(n), Space: O(1)

    Args:
        arr: List of positive integers
        target: Target sum

    Returns:
        Start and end indices of subarray, or empty if not found
    """
    # Initialize pointers and current sum
    left = 0
    current_sum = 0

    for right in range(len(arr)):
        # Add current element to window
        current_sum += arr[right]

        # Shrink window from left while sum exceeds target
        while current_sum > target and left <= right:
            current_sum -= arr[left]
            left += 1

        # Check if we found the target
        if current_sum == target:
            return [left, right]

    return []


# =============================================================================
# TEST FUNCTIONS
# =============================================================================

def run_tests():
    """Run test cases for all implementations."""

    # Test two_sum_sorted
    arr = [1, 2, 3, 4, 6]
    result = two_sum_sorted(arr, 6)
    print(f"Two Sum Sorted: {result}")  # Expected: (1, 4)

    # Test is_palindrome
    print(f"Is Palindrome: {is_palindrome('A man, a plan, a canal: Panama')}")  # True

    # Test container_with_most_water
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(f"Container With Most Water: {container_with_most_water(height)}")  # 49

    # Test remove_duplicates_sorted
    arr = [1, 1, 1, 2, 2, 3]
    count = remove_duplicates_sorted(arr)
    print(f"Remove Duplicates: {count}, Array: {arr[:count]}")  # 3, [1,2,3]

    # Test three_sum
    nums = [-1, 0, 1, 2, -1, -4]
    result = three_sum(nums)
    print(f"3Sum: {result}")  # [[-1,-1,2],[-1,0,1]]

    # Test trapping_rain_water
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(f"Trapping Rain Water: {trapping_rain_water(height)}")  # 6

    # Test dutch_national_flag
    arr = [2, 0, 2, 1, 1, 0]
    result = dutch_national_flag_partition(arr, 1)
    print(f"Dutch National Flag: {arr}, Equal range: {result}")  # [0,0,1,1,2,2], (2,4)


if __name__ == "__main__":
    run_tests()
