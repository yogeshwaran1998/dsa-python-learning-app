"""
Hash Tables - Implementation and Examples
==========================================
Comprehensive Python implementations for hash table problems
commonly asked in FAANG interviews.
"""

from typing import List, Dict, Set, Tuple, Optional
from collections import defaultdict, Counter


# =============================================================================
# SECTION 1: FREQUENCY COUNTER PATTERN
# =============================================================================

def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Find indices of two numbers that add up to target.

    Time: O(n), Space: O(n)
    """
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return []


def three_sum(nums: List[int]) -> List[List[int]]:
    """
    Find all unique triplets that sum to zero.

    Time: O(n²), Space: O(n) - excluding output
    """
    result = []
    nums.sort()

    for i in range(len(nums) - 2):
        # Skip duplicates
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Two pointer approach for remaining
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1

                # Skip duplicates
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif total < 0:
                left += 1
            else:
                right -= 1

    return result


def four_sum(nums: List[int], target: int) -> List[List[int]]:
    """
    Find all unique quadruplets that sum to target.

    Time: O(n³), Space: O(n) - excluding output
    """
    result = []
    nums.sort()

    for i in range(len(nums) - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, len(nums) - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            left, right = j + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]

                if total == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < target:
                    left += 1
                else:
                    right -= 1

    return result


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    Find k most frequent elements.

    Time: O(n), Space: O(n)
    """
    # Count frequencies
    freq = Counter(nums)

    # Use bucket sort - index = frequency
    bucket = [[] for _ in range(len(nums) + 1)]

    for num, count in freq.items():
        bucket[count].append(num)

    # Get top k from highest frequency
    result = []
    for count in range(len(nums), 0, -1):
        for num in bucket[count]:
            result.append(num)
            if len(result) == k:
                return result

    return result


def top_k_frequent_heap(nums: List[int], k: int) -> List[int]:
    """
    Find k most frequent elements using heap.

    Time: O(n log k), Space: O(n)
    """
    import heapq

    freq = Counter(nums)

    # Use min-heap of size k
    heap = []

    for num, count in freq.items():
        heapq.heappush(heap, (count, num))
        if len(heap) > k:
            heapq.heappop(heap)

    return [num for count, num in sorted(heap, reverse=True)]


# =============================================================================
# SECTION 2: ANAGRAM PATTERNS
# =============================================================================

def is_anagram(s: str, t: str) -> bool:
    """
    Check if two strings are anagrams.

    Time: O(n), Space: O(1) - assuming fixed alphabet
    """
    if len(s) != len(t):
        return False

    count = [0] * 26  # For lowercase letters

    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1

    return all(c == 0 for c in count)


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    Group anagrams together.

    Time: O(n * k), Space: O(n * k)
    where k = average string length
    """
    anagrams = defaultdict(list)

    for s in strs:
        # Sort characters as key
        key = ''.join(sorted(s))
        anagrams[key].append(s)

    return list(anagrams.values())


def group_anagrams_count(strs: List[str]) -> List[List[str]]:
    """
    Group anagrams using character count (faster for long strings).

    Time: O(n * k), Space: O(n * k)
    """
    anagrams = defaultdict(list)

    for s in strs:
        # Count characters
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1

        # Use tuple as key (immutable)
        key = tuple(count)
        anagrams[key].append(s)

    return list(anagrams.values())


def valid_anagram_group(strs: List[str]) -> List[List[List[str]]]:
    """
    Group valid anagrams from list.
    Words in same group must be anagrams of each other.

    Time: O(n * k log k), Space: O(n * k)
    """
    groups = defaultdict(list)

    for s in strs:
        key = ''.join(sorted(s))
        groups[key].append(s)

    # Filter groups where all words are anagrams
    result = []
    for group in groups.values():
        # Check if any pair in group is valid anagram
        is_valid = True
        for i in range(len(group)):
            for j in range(i + 1, len(group)):
                if not is_anagram(group[i], group[j]):
                    is_valid = False
                    break
            if not is_valid:
                break

        if is_valid and len(group) > 1:
            result.append(group)

    return result


# =============================================================================
# SECTION 3: SUBARRAY SUM PATTERNS
# =============================================================================

def subarray_sum_equals_k(nums: List[int], k: int) -> int:
    """
    Count continuous subarrays that sum to k.

    Time: O(n), Space: O(n)
    """
    count = 0
    prefix_sum = 0
    sum_freq = {0: 1}

    for num in nums:
        prefix_sum += num

        # If (prefix - k) exists, we found subarray
        if prefix_sum - k in sum_freq:
            count += sum_freq[prefix_sum - k]

        sum_freq[prefix_sum] = sum_freq.get(prefix_sum, 0) + 1

    return count


def subarray_sum_equals_k_divisible(nums: List[int], k: int) -> int:
    """
    Count subarrays where sum is divisible by k.

    Time: O(n), Space: O(k)
    """
    count = 0
    prefix_sum = 0
    remainder_freq = [0] * k
    remainder_freq[0] = 1

    for num in nums:
        prefix_sum += num
        remainder = prefix_sum % k
        if remainder < 0:
            remainder += k

        count += remainder_freq[remainder]
        remainder_freq[remainder] += 1

    return count


def number_of_submatrices_that_sum_to_target(
    matrix: List[List[int]], target: int
) -> int:
    """
    Count submatrices that sum to target.

    Time: O(n² * m), Space: O(m)

    Fix top and bottom rows, use prefix sum for columns.
    """
    if not matrix:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    count = 0

    # Fix top row
    for top in range(rows):
        col_sum = [0] * cols

        # Fix bottom row
        for bottom in range(top, rows):
            # Add current row to column sums
            for col in range(cols):
                col_sum[col] += matrix[bottom][col]

            # Count subarrays with sum = target
            prefix = 0
            freq = {0: 1}

            for val in col_sum:
                prefix += val
                if prefix - target in freq:
                    count += freq[prefix - target]
                freq[prefix] = freq.get(prefix, 0) + 1

    return count


# =============================================================================
# SECTION 4: LONGEST SUBSEQUENCE PATTERNS
# =============================================================================

def longest_consecutive_sequence(nums: List[int]) -> int:
    """
    Find length of longest consecutive sequence.

    Time: O(n), Space: O(n)
    """
    if not nums:
        return 0

    num_set = set(nums)
    max_length = 0

    for num in num_set:
        # Only start from smallest in sequence
        if num - 1 not in num_set:
            current = num
            length = 1

            while current + 1 in num_set:
                current += 1
                length += 1

            max_length = max(max_length, length)

    return max_length


def longest_consecutive_sequence_union_find(nums: List[int]) -> int:
    """
    Find longest consecutive sequence using Union-Find.

    Time: O(n * α(n)), Space: O(n)
    """
    if not nums:
        return 0

    parent = {}
    size = {}
    max_length = 1

    def find(x):
        if x not in parent:
            parent[x] = x
            size[x] = 1

        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        nonlocal max_length
        rx, ry = find(x), find(y)
        if rx == ry:
            return

        if size[rx] < size[ry]:
            rx, ry = ry, rx

        parent[ry] = rx
        size[rx] += size[ry]
        max_length = max(max_length, size[rx])

    for num in nums:
        if num not in parent:
            parent[num] = num
            size[num] = 1

            if num - 1 in parent:
                union(num, num - 1)
            if num + 1 in parent:
                union(num, num + 1)

    return max_length


# =============================================================================
# SECTION 5: HASH SET OPERATIONS
# =============================================================================

def contains_duplicate(nums: List[int]) -> bool:
    """
    Check if array contains duplicates.

    Time: O(n), Space: O(n)
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


def contains_duplicate_nearby(nums: List[int], k: int) -> bool:
    """
    Check if duplicate exists within k distance.

    Time: O(n), Space: O(k)
    """
    seen = set()

    for i, num in enumerate(nums):
        if num in seen:
            return True

        seen.add(num)

        if i >= k:
            seen.remove(nums[i - k])

    return False


def happy_number(n: int) -> bool:
    """
    Check if number is happy (sum of squares of digits = 1).

    Time: O(log n), Space: O(log n)
    """
    def get_next(x):
        total = 0
        while x > 0:
            digit = x % 10
            total += digit * digit
            x //= 10
        return total

    # Use Floyd's cycle detection
    slow = get_next(n)
    fast = get_next(get_next(n))

    while slow != fast and fast != 1:
        slow = get_next(slow)
        fast = get_next(get_next(fast))

    return fast == 1


def intersection_of_arrays(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Find intersection of two arrays (unique elements).

    Time: O(n + m), Space: O(n + m)
    """
    set1 = set(nums1)
    set2 = set(nums2)

    return list(set1.intersection(set2))


# =============================================================================
# SECTION 6: CUSTOM HASH IMPLEMENTATION
# =============================================================================

class HashMap:
    """
    Custom hash map implementation using chaining.

    Time: O(1) average, Space: O(n)
    """

    def __init__(self, size: int = 100):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key) -> int:
        return hash(key) % self.size

    def put(self, key, value) -> None:
        index = self._hash(key)
        bucket = self.buckets[index]

        # Update if key exists
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        # Add new key-value pair
        bucket.append((key, value))

    def get(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return v

        return None

    def remove(self, key) -> None:
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return


class CustomKey:
    """
    Custom object as dictionary key requires __hash__ and __eq__.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"CustomKey({self.x}, {self.y})"


# =============================================================================
# SECTION 7: SLIDING WINDOW WITH HASH
# =============================================================================

def count_subarrays_with_k_distinct(nums: List[int], k: int) -> int:
    """
    Count subarrays with exactly k distinct integers.

    Time: O(n), Space: O(k)

    Formula: atMostK(k) - atMostK(k-1)
    """
    def at_most_k(k):
        if k == 0:
            return 0

        count = 0
        freq = defaultdict(int)
        distinct = 0
        left = 0

        for right in range(len(nums)):
            if freq[nums[right]] == 0:
                distinct += 1
            freq[nums[right]] += 1

            while distinct > k:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    distinct -= 1
                left += 1

            count += right - left + 1

        return count

    return at_most_k(k) - at_most_k(k - 1)


def fruit_into_baskets(fruits: List[int]) -> int:
    """
    Find max fruits in two baskets (similar to k=2 distinct).

    Time: O(n), Space: O(1)
    """
    freq = defaultdict(int)
    left = 0
    max_count = 0

    for right, fruit in enumerate(fruits):
        freq[fruit] += 1

        while len(freq) > 2:
            freq[fruits[left]] -= 1
            if freq[fruits[left]] == 0:
                del freq[fruits[left]]
            left += 1

        max_count = max(max_count, right - left + 1)

    return max_count


def length_of_longest_substring_k_distinct(s: str, k: int) -> int:
    """
    Find length of longest substring with at most k distinct chars.

    Time: O(n), Space: O(k)
    """
    if k == 0:
        return 0

    char_count = {}
    left = 0
    max_length = 0

    for right, char in enumerate(s):
        char_count[char] = char_count.get(char, 0) + 1

        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length


# =============================================================================
# SECTION 8: TESTING AND DEMO
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("HASH TABLE ALGORITHMS - TEST DEMO")
    print("=" * 60)

    # Test Two Sum
    print("\n--- Two Sum ---")
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print(f"Two sum for {nums} with target {target}: {result}")

    # Test Three Sum
    print("\n--- Three Sum ---")
    nums = [-1, 0, 1, 2, -1, -4]
    result = three_sum(nums)
    print(f"Three sum for {nums}:")
    for triplet in result:
        print(f"  {triplet}")

    # Test Group Anagrams
    print("\n--- Group Anagrams ---")
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = group_anagrams(strs)
    print(f"Group anagrams of {strs}:")
    for group in result:
        print(f"  {group}")

    # Test Top K Frequent
    print("\n--- Top K Frequent ---")
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    result = top_k_frequent(nums, k)
    print(f"Top {k} frequent in {nums}: {result}")

    # Test Subarray Sum
    print("\n--- Subarray Sum Equals K ---")
    nums = [1, 1, 1]
    k = 2
    result = subarray_sum_equals_k(nums, k)
    print(f"Subarrays with sum={k} in {nums}: {result}")

    # Test Longest Consecutive
    print("\n--- Longest Consecutive Sequence ---")
    nums = [100, 4, 200, 1, 3, 2]
    result = longest_consecutive_sequence(nums)
    print(f"Longest consecutive in {nums}: {result}")

    # Test Contains Duplicate
    print("\n--- Contains Duplicate ---")
    nums1 = [1, 2, 3, 1]
    nums2 = [1, 2, 3, 4]
    print(f"{nums1} has duplicate: {contains_duplicate(nums1)}")
    print(f"{nums2} has duplicate: {contains_duplicate(nums2)}")

    # Test Is Anagram
    print("\n--- Is Anagram ---")
    s, t = "anagram", "nagaram"
    print(f"'{s}' and '{t}' are anagrams: {is_anagram(s, t)}")

    # Test Count Subarrays with K Distinct
    print("\n--- Count Subarrays with K Distinct ---")
    nums = [1, 2, 1, 2, 3]
    k = 2
    result = count_subarrays_with_k_distinct(nums, k)
    print(f"Subarrays with exactly {k} distinct in {nums}: {result}")

    # Test Fruit into Baskets
    print("\n--- Fruit Into Baskets ---")
    fruits = [1, 2, 1, 2, 3, 3]
    result = fruit_into_baskets(fruits)
    print(f"Max fruits in 2 baskets: {result}")

    print("\n" + "=" * 60)
    print("All tests completed!")
    print("=" * 60)
