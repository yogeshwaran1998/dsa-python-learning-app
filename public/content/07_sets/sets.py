"""
Sets - Implementation and Examples
===================================
Comprehensive Python implementations for set problems
commonly asked in FAANG interviews.
"""

from typing import List, Set, Tuple


# =============================================================================
# SECTION 1: SET OPERATIONS
# =============================================================================

def find_intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Find intersection of two arrays (unique elements).

    Time: O(n + m), Space: O(n + m)
    """
    return list(set(nums1) & set(nums2))


def find_intersection_preserving_order(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Find intersection while preserving order from nums1.

    Time: O(n + m), Space: O(m)
    """
    set2 = set(nums2)
    result = []

    for num in nums1:
        if num in set2 and num not in result:
            result.append(num)

    return result


def union_arrays(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Find union of two arrays (unique elements).

    Time: O(n + m), Space: O(n + m)
    """
    return list(set(nums1) | set(nums2))


def find_difference(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Find elements in nums1 that are not in nums2.

    Time: O(n + m), Space: O(m)
    """
    return list(set(nums1) - set(nums2))


def symmetric_difference(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Find elements in either array but not both.

    Time: O(n + m), Space: O(n + m)
    """
    return list(set(nums1) ^ set(nums2))


# =============================================================================
# SECTION 2: DEDUPLICATION PATTERNS
# =============================================================================

def remove_duplicates_list(nums: List[int]) -> int:
    """
    Remove duplicates in-place from sorted array.
    Returns count of unique elements.

    Time: O(n), Space: O(1)
    """
    if not nums:
        return 0

    unique_idx = 0

    for i in range(1, len(nums)):
        if nums[i] != nums[unique_idx]:
            unique_idx += 1
            nums[unique_idx] = nums[i]

    return unique_idx + 1


def remove_duplicates_unsorted(nums: List[int]) -> List[int]:
    """
    Remove duplicates while preserving order.

    Time: O(n), Space: O(n)
    """
    seen = set()
    result = []

    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)

    return result


def find_duplicates(nums: List[int]) -> List[int]:
    """
    Find all duplicates in O(n) time and O(1) space.

    Time: O(n), Space: O(1) - excluding output
    """
    result = []

    for num in nums:
        idx = abs(num) - 1
        if nums[idx] < 0:
            result.append(abs(num))
        else:
            nums[idx] = -nums[idx]

    return result


# =============================================================================
# SECTION 3: SET-BASED PROBLEMS
# =============================================================================

def single_number(nums: List[int]) -> int:
    """
    Find element that appears exactly once.

    Time: O(n), Space: O(1) - using XOR

    Note: XOR approach works when all others appear twice.
    """
    result = 0
    for num in nums:
        result ^= num
    return result


def single_number_set(nums: List[int]) -> int:
    """
    Find element that appears exactly once using sets.

    Time: O(n), Space: O(n)
    """
    seen = set()

    for num in nums:
        if num in seen:
            seen.remove(num)
        else:
            seen.add(num)

    return seen.pop()


def find_disappeared_numbers(nums: List[int]) -> List[int]:
    """
    Find numbers from 1 to n that are missing.

    Time: O(n), Space: O(1) - excluding output
    """
    result = []

    for num in nums:
        idx = abs(num) - 1
        if nums[idx] > 0:
            nums[idx] = -nums[idx]

    for i in range(len(nums)):
        if nums[i] > 0:
            result.append(i + 1)

    return result


def longest_consecutive_sequence_set(nums: List[int]) -> int:
    """
    Find length of longest consecutive sequence.

    Time: O(n), Space: O(n)
    """
    if not nums:
        return 0

    num_set = set(nums)
    max_length = 0

    for num in num_set:
        if num - 1 not in num_set:
            current = num
            length = 1

            while current + 1 in num_set:
                current += 1
                length += 1

            max_length = max(max_length, length)

    return max_length


# =============================================================================
# SECTION 4: TWO SUM WITH SETS
# =============================================================================

def two_sum_set(nums: List[int], target: int) -> List[int]:
    """
    Find indices of two numbers that add up to target.
    Uses set for O(n) space.

    Time: O(n), Space: O(n)
    """
    seen = set()

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            # Find complement's index
            for j in range(i):
                if nums[j] == complement:
                    return [j, i]
        seen.add(num)

    return []


def two_sum_sorted_two_pointers(nums: List[int], target: int) -> List[int]:
    """
    Find two numbers that add up to target in sorted array.

    Time: O(n), Space: O(1)
    """
    left, right = 0, len(nums) - 1

    while left < right:
        current = nums[left] + nums[right]

        if current == target:
            return [left, right]
        elif current < target:
            left += 1
        else:
            right -= 1

    return []


# =============================================================================
# SECTION 5: SUBSET PATTERNS
# =============================================================================

def is_subset(set1: Set[int], set2: Set[int]) -> bool:
    """
    Check if set1 is subset of set2.

    Time: O(len(set1)), Space: O(1)
    """
    return set1.issubset(set2)


def subsets(nums: List[int]) -> List[List[int]]:
    """
    Find all possible subsets (power set).

    Time: O(n * 2^n), Space: O(2^n)
    """
    result = [[]]

    for num in nums:
        result += [curr + [num] for curr in result]

    return result


def subsets_with_duplicates(nums: List[int]) -> List[List[int]]:
    """
    Find all subsets handling duplicates.

    Time: O(n * 2^n), Space: O(2^n)
    """
    nums.sort()
    result = [[]]

    for i in range(len(nums)):
        # Only add to subsets that include previous element
        if i == 0 or nums[i] != nums[i - 1]:
            result += [curr + [nums[i]] for curr in result]

    return result


# =============================================================================
# SECTION 6: SET VALIDATION
# =============================================================================

def has_unique_characters(s: str) -> bool:
    """
    Check if string has all unique characters.

    Time: O(n), Space: O(1) - using set
    """
    seen = set()

    for char in s:
        if char in seen:
            return False
        seen.add(char)

    return True


def is_isogram(s: str) -> bool:
    """
    Check if string is an isogram (no repeated letters).

    Time: O(n), Space: O(n)
    """
    return len(s) == len(set(s.lower()))


# =============================================================================
# SECTION 7: TESTING AND DEMO
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("SET ALGORITHMS - TEST DEMO")
    print("=" * 60)

    # Test Intersection
    print("\n--- Intersection ---")
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    result = find_intersection(nums1, nums2)
    print(f"Intersection of {nums1} and {nums2}: {result}")

    # Test Union
    print("\n--- Union ---")
    nums1 = [1, 2, 3]
    nums2 = [2, 4, 5]
    result = union_arrays(nums1, nums2)
    print(f"Union of {nums1} and {nums2}: {result}")

    # Test Difference
    print("\n--- Difference ---")
    nums1 = [1, 2, 3]
    nums2 = [2]
    result = find_difference(nums1, nums2)
    print(f"Difference {nums1} - {nums2}: {result}")

    # Test Single Number
    print("\n--- Single Number ---")
    nums = [2, 2, 1]
    result = single_number(nums)
    print(f"Single number in {nums}: {result}")

    # Test Longest Consecutive
    print("\n--- Longest Consecutive ---")
    nums = [100, 4, 200, 1, 3, 2]
    result = longest_consecutive_sequence_set(nums)
    print(f"Longest consecutive in {nums}: {result}")

    # Test Has Unique Characters
    print("\n--- Has Unique Characters ---")
    print(f"'abcde': {has_unique_characters('abcde')}")
    print(f"'hello': {has_unique_characters('hello')}")

    # Test Subsets
    print("\n--- Subsets ---")
    nums = [1, 2, 3]
    result = subsets(nums)
    print(f"Subsets of {nums}:")
    for subset in result:
        print(f"  {subset}")

    # Test Subsets with Duplicates
    print("\n--- Subsets with Duplicates ---")
    nums = [1, 2, 2]
    result = subsets_with_duplicates(nums)
    print(f"Subsets of {nums}:")
    for subset in result:
        print(f"  {subset}")

    print("\n" + "=" * 60)
    print("All tests completed!")
    print("=" * 60)
