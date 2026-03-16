"""
Hashing Patterns - Implementation and Examples
============================================
Comprehensive Python implementations of hashing patterns
commonly asked in FAANG interviews.

Topics covered:
1. Frequency counting
2. Two-sum and variations
3. Anagram detection
4. Custom keys
"""

from typing import List, Dict, Set, Tuple
from collections import Counter, defaultdict


# =============================================================================
# SECTION 1: FREQUENCY COUNTING
# =============================================================================

def contains_duplicate(nums: List[int]) -> bool:
    """
    Check if array contains any duplicate.

    How it works:
    - Use set to track seen elements
    - If element already in set, we found a duplicate
    - Set provides O(1) lookup

    Time: O(n), Space: O(n)

    Args:
        nums: List of integers

    Returns:
        True if any duplicate exists, False otherwise

    Example:
        Input: [1, 2, 3, 1]
        Output: True
    """
    # Use set to store seen elements
    # This is more efficient than checking in list (O(n))
    seen = set()

    # Iterate through array
    for num in nums:
        # If element already in set, it's a duplicate
        if num in seen:
            return True

        # Add element to seen set
        seen.add(num)

    # No duplicates found
    return False


def contains_duplicate_nearby(nums: List[int], k: int) -> bool:
    """
    Check if there are duplicates within k distance of each other.

    How it works:
    - Use set of size k to track elements in window
    - If element already in window, duplicate found

    Time: O(n), Space: O(k)

    Args:
        nums: List of integers
        k: Maximum distance between duplicates

    Returns:
        True if duplicate within k distance exists

    Example:
        Input: [1, 2, 3, 1], k = 3
        Output: True (elements at indices 0 and 3)
    """
    # Use sliding window set
    seen = set()

    for i, num in enumerate(nums):
        # Check if element in current window
        if num in seen:
            return True

        # Add current element to window
        seen.add(num)

        # Remove element that's k positions behind
        # This maintains window size of k+1
        if i >= k:
            seen.remove(nums[i - k])

    return False


def frequency_counter(nums: List[int]) -> Dict[int, int]:
    """
    Count frequency of each element in array.

    How it works:
    - Use dictionary to store element -> count
    - Iterate and increment count

    Time: O(n), Space: O(n)

    Args:
        nums: List of integers

    Returns:
        Dictionary mapping element to its frequency
    """
    # Dictionary to store counts
    freq = {}

    for num in nums:
        # Increment count (default to 0 if not present)
        freq[num] = freq.get(num, 0) + 1

    return freq


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    Find k most frequent elements.

    How it works:
    - First count frequencies using Counter
    - Sort by frequency (or use heap for O(n log k))
    - Return top k

    Time: O(n log n), Space: O(n)

    Args:
        nums: List of integers
        k: Number of most frequent elements to return

    Returns:
        List of k most frequent elements

    Example:
        Input: [1,1,1,2,2,3], k = 2
        Output: [1, 2] (or [1,2])
    """
    # Use Counter to get frequencies
    count = Counter(nums)

    # Sort by frequency (descending) and return top k
    # Using most_common is cleaner but here's manual approach
    sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)

    # Return first k elements
    return [item[0] for item in sorted_items[:k]]


def top_k_frequent_heap(nums: List[int], k: int) -> List[int]:
    """
    Find k most frequent elements using heap (more efficient).

    How it works:
    - Count frequencies
    - Use min-heap of size k
    - Maintain only top k frequencies

    Time: O(n log k), Space: O(n)

    Args:
        nums: List of integers
        k: Number of most frequent elements

    Returns:
        List of k most frequent elements
    """
    import heapq

    # Count frequencies
    count = Counter(nums)

    # Use negative frequency for max heap behavior
    # heapq is min-heap, so negate for max behavior
    heap = []

    for num, freq in count.items():
        # Push (negative frequency, number) into heap
        heapq.heappush(heap, (-freq, num))

    # Extract top k elements
    result = []
    for _ in range(k):
        if heap:
            freq, num = heapq.heappop(heap)
            result.append(num)

    return result


# =============================================================================
# SECTION 2: TWO SUM AND VARIATIONS
# =============================================================================

def two_sum_indices(nums: List[int], target: int) -> List[int]:
    """
    Find indices of two numbers that add up to target.
    Returns indices of the two numbers such that they add up to target.

    How it works:
    - Use dictionary to store value -> index
    - For each element, check if complement (target - element) exists
    - This gives O(n) time

    Time: O(n), Space: O(n)

    Args:
        nums: List of integers
        target: Target sum

    Returns:
        Indices of two numbers that add up to target

    Example:
        Input: nums = [2,7,11,15], target = 9
        Output: [0, 1] (because nums[0] + nums[1] = 9)
    """
    # Dictionary to store number -> index
    num_to_index = {}

    # Iterate through array with index
    for i, num in enumerate(nums):
        # Calculate complement (the number we need)
        complement = target - num

        # Check if complement exists in dictionary
        if complement in num_to_index:
            # Found the pair
            return [num_to_index[complement], i]

        # Store current number and its index
        num_to_index[num] = i

    # No solution found (shouldn't happen for valid inputs)
    return []


def two_sum_sorted(arr: List[int], target: int) -> List[int]:
    """
    Find two numbers in sorted array that add up to target.
    Returns their values (not indices).

    How it works:
    - Since array is sorted, use two pointers
    - More space-efficient than hash approach

    Time: O(n), Space: O(1)

    Args:
        arr: Sorted list of integers
        target: Target sum

    Returns:
        Values of two numbers that add up to target
    """
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return [arr[left], arr[right]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []


def two_sum_multiple_pairs(nums: List[int], target: int) -> List[List[int]]:
    """
    Find all unique pairs that sum to target.

    How it works:
    - Use Counter to count occurrences
    - Handle cases where same number can be used twice
    - Generate all unique pairs

    Time: O(n), Space: O(n)

    Args:
        nums: List of integers
        target: Target sum

    Returns:
        List of all unique pairs [a, b]
    """
    # Count frequencies
    count = Counter(nums)
    result = []

    # Handle special cases based on number types
    # Iterate through unique numbers only
    for num in list(count.keys()):
        complement = target - num

        if complement not in count:
            # No complement exists
            continue

        if num == complement:
            # Same number - need at least 2 occurrences
            if count[num] >= 2:
                result.append([num, num])
        elif num < complement:
            # Avoid duplicate pairs by only processing when num < complement
            result.append([num, complement])

    return result


def three_sum(nums: List[int]) -> List[List[int]]:
    """
    Find all unique triplets that sum to zero.

    How it works:
    - Sort the array first
    - For each element, find pairs that sum to negative of element
    - Use two pointers for pair finding
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
    # Sort to enable two pointers and skip duplicates
    nums.sort()
    result = []
    n = len(nums)

    # Fix first element
    for i in range(n - 2):
        # Skip duplicates for first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Find pairs for remaining sum = -nums[i]
        left = i + 1
        right = n - 1
        target = -nums[i]

        while left < right:
            current_sum = nums[left] + nums[right]

            if current_sum == target:
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicates for left and right
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return result


# =============================================================================
# SECTION 3: ANAGRAM DETECTION
# =============================================================================

def is_anagram(s: str, t: str) -> bool:
    """
    Check if two strings are anagrams of each other.
    Anagrams have same characters with same frequencies.

    How it works:
    - Method 1: Sort both strings and compare
    - Method 2: Count characters and compare

    Time: O(n log n) for sort, O(n) for counting, Space: O(1)

    Args:
        s: First string
        t: Second string

    Returns:
        True if strings are anagrams, False otherwise

    Example:
        Input: s = "anagram", t = "nagaram"
        Output: True
    """
    # Quick check: different lengths can't be anagrams
    if len(s) != len(t):
        return False

    # Use Counter to count characters
    # This is O(n) time and O(1) space (fixed alphabet)
    return Counter(s) == Counter(t)


def is_anagram_sort(s: str, t: str) -> bool:
    """
    Check if anagrams using sorting method.
    Simpler but O(n log n) time.
    """
    # Quick check
    if len(s) != len(t):
        return False

    # Sort both strings and compare
    return sorted(s) == sorted(t)


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    Group anagrams together.

    How it works:
    - Create a signature for each string
    - Signature can be: sorted characters OR character count tuple
    - Use dictionary to group by signature

    Time: O(n * k log k) with sorting, O(n * k) with counting
    Space: O(n * k)

    Args:
        strs: List of strings

    Returns:
        List of groups, where each group contains anagrams

    Example:
        Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
        Output: [["eat","tea","ate"], ["tan","nat"], ["bat"]]
    """
    # Method: Use sorted string as key
    # This works because anagrams have same sorted form

    # Dictionary to group anagrams
    anagram_groups = defaultdict(list)

    for s in strs:
        # Create key: sorted characters
        key = tuple(sorted(s))

        # Add to appropriate group
        anagram_groups[key].append(s)

    # Convert to list of lists
    return list(anagram_groups.values())


def group_anagrams_count(strs: List[str]) -> List[List[str]]:
    """
    Group anagrams using character count (more efficient for long strings).

    How it works:
    - Use tuple of 26 counts as key
    - Avoids sorting overhead

    Time: O(n * k), Space: O(n * k)
    """
    anagram_groups = defaultdict(list)

    for s in strs:
        # Count characters using array of 26 (for lowercase)
        count = [0] * 26

        for c in s:
            count[ord(c) - ord('a')] += 1

        # Use tuple as key (immutable)
        key = tuple(count)
        anagram_groups[key].append(s)

    return list(anagram_groups.values())


def find_anagrams(s: str, p: str) -> List[int]:
    """
    Find all starting indices of anagram substrings in s.

    How it works:
    - Use sliding window with character count
    - Compare window count with pattern count

    Time: O(n), Space: O(1) - fixed alphabet

    Args:
        s: Source string
        p: Pattern string

    Returns:
        List of starting indices of anagrams
    """
    # Need pattern length for window
    p_len = len(p)

    # If pattern longer than source, no anagrams possible
    if p_len > len(s):
        return []

    # Count characters in pattern
    p_count = Counter(p)
    window_count = Counter()

    # Build initial window of size p_len
    for i in range(p_len):
        window_count[s[i]] += 1

    result = []

    # Check if first window is anagram
    if window_count == p_count:
        result.append(0)

    # Slide window through string
    for i in range(p_len, len(s)):
        # Add new character (right side)
        window_count[s[i]] += 1

        # Remove old character (left side)
        left_char = s[i - p_len]
        window_count[left_char] -= 1

        # Clean up zero counts
        if window_count[left_char] == 0:
            del window_count[left_char]

        # Check if current window is anagram
        if window_count == p_count:
            result.append(i - p_len + 1)

    return result


# =============================================================================
# SECTION 4: CUSTOM KEYS
# =============================================================================

def longest_consecutive_sequence(nums: List[int]) -> int:
    """
    Find length of longest consecutive sequence.
    Sequence can be in any order but elements must be consecutive.

    How it works:
    - Put all numbers in set for O(1) lookup
    - For each number, check if it's start of sequence
    - If so, count consecutive numbers

    Time: O(n), Space: O(n)

    Args:
        nums: List of integers (may be unsorted)

    Returns:
        Length of longest consecutive sequence

    Example:
        Input: [100, 4, 200, 1, 3, 2]
        Output: 4 (sequence: 1, 2, 3, 4)
    """
    # Edge case: empty array
    if not nums:
        return 0

    # Put all numbers in set for O(1) lookup
    num_set = set(nums)
    max_length = 0

    # Check each number
    for num in num_set:
        # Only start counting if this is the start of a sequence
        # (i.e., num-1 not in set)
        if num - 1 not in num_set:
            # This is start of a sequence
            current = num
            current_length = 1

            # Count consecutive numbers
            while current + 1 in num_set:
                current += 1
                current_length += 1

            # Update maximum
            max_length = max(max_length, current_length)

    return max_length


def custom_key_example():
    """
    Demonstrate custom key usage in hashing.
    Useful for multi-dimensional problems.
    """
    # Example 1: Position as key
    # Grid problems often use (row, col) tuples
    positions = {(0, 0): "start", (1, 1): "middle", (2, 2): "end"}

    # Example 2: Frequency pattern as key
    # Group strings by frequency signature
    strings = ["abc", "aabc", "bcaa", "xyz"]
    freq_pattern = defaultdict(list)

    for s in strings:
        # Key: tuple of sorted (count, char) pairs
        # Or use tuple(Counter(s).values()) sorted
        key = tuple(sorted(Counter(s).values()))
        freq_pattern[key].append(s)

    print("Frequency pattern groups:", dict(freq_pattern))


# =============================================================================
# SECTION 5: ADDITIONAL HASHING PATTERNS
# =============================================================================

def intersection_arrays(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Find intersection of two arrays (unique elements).

    How it works:
    - Convert both to sets
    - Use intersection or set operation

    Time: O(n + m), Space: O(n + m)

    Args:
        nums1: First array
        nums2: Second array

    Returns:
        List of common elements
    """
    # Convert to sets for O(1) lookup
    set1 = set(nums1)
    set2 = set(nums2)

    # Return intersection
    return list(set1.intersection(set2))


def first_unique_character(s: str) -> int:
    """
    Find index of first non-repeating character.

    How it works:
    - Count frequency of all characters
    - Iterate through string to find first with count 1

    Time: O(n), Space: O(1) - fixed alphabet

    Args:
        s: Input string

    Returns:
        Index of first unique character, or -1 if none
    """
    # Count all characters
    count = Counter(s)

    # Find first character with count 1
    for i, c in enumerate(s):
        if count[c] == 1:
            return i

    return -1


def isomorphic_strings(s: str, t: str) -> bool:
    """
    Check if two strings are isomorphic.
    Characters can be replaced to get other string.

    How it works:
    - Map characters from s to t
    - Also check reverse mapping to avoid multiple chars mapping to same

    Time: O(n), Space: O(n)

    Example:
        Input: s = "egg", t = "add"
        Output: True
    """
    if len(s) != len(t):
        return False

    # Maps character from s to t and reverse
    s_to_t = {}
    t_to_s = {}

    for c1, c2 in zip(s, t):
        # Check forward mapping
        if c1 in s_to_t:
            if s_to_t[c1] != c2:
                return False
        else:
            s_to_t[c1] = c2

        # Check reverse mapping
        if c2 in t_to_s:
            if t_to_s[c2] != c1:
                return False
        else:
            t_to_s[c2] = c1

    return True


def subarray_sum_divisible_by_k(nums: List[int], k: int) -> int:
    """
    Count subarrays where sum is divisible by k.

    How it works:
    - Use prefix sums and modulo
    - If two prefix sums have same remainder, subarray between them is divisible

    Time: O(n), Space: O(k)

    Args:
        nums: List of integers
        k: Divisor

    Returns:
        Count of subarrays with sum divisible by k
    """
    # Count occurrences of each remainder
    remainder_count = Counter()
    remainder_count[0] = 1  # Subarray starting at index 0

    prefix = 0
    count = 0

    for num in nums:
        prefix += num

        # Handle negative numbers: normalize remainder
        remainder = prefix % k
        if remainder < 0:
            remainder += k

        # Add to count
        count += remainder_count[remainder]
        remainder_count[remainder] += 1

    return count


# =============================================================================
# TEST FUNCTIONS
# =============================================================================

def run_tests():
    """Run test cases for all implementations."""

    # Test contains_duplicate
    result = contains_duplicate([1, 2, 3, 1])
    print(f"Contains Duplicate: {result}")  # True

    # Test two_sum_indices
    result = two_sum_indices([2, 7, 11, 15], 9)
    print(f"Two Sum Indices: {result}")  # [0, 1]

    # Test is_anagram
    result = is_anagram("anagram", "nagaram")
    print(f"Is Anagram: {result}")  # True

    # Test group_anagrams
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(f"Group Anagrams: {result}")  # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    # Test longest_consecutive_sequence
    result = longest_consecutive_sequence([100, 4, 200, 1, 3, 2])
    print(f"Longest Consecutive: {result}")  # 4

    # Test top_k_frequent
    result = top_k_frequent([1, 1, 1, 2, 2, 3], 2)
    print(f"Top K Frequent: {result}")  # [1, 2]

    # Test first_unique_character
    result = first_unique_character("loveleetcode")
    print(f"First Unique Char: {result}")  # 2


if __name__ == "__main__":
    run_tests()
