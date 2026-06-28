"""
Greedy Algorithms - Implementation and Examples
============================================
Comprehensive Python implementations for greedy algorithm problems
commonly asked in FAANG interviews.
"""

from typing import List, Tuple


# =============================================================================
# SECTION 1: ACTIVITY SELECTION
# =============================================================================

def activity_selection(activities: List[Tuple[int, int]]) -> int:
    """
    Maximum number of non-overlapping activities.

    Time: O(n log n), Space: O(1)
    """
    if not activities:
        return 0

    activities.sort(key=lambda x: x[1])
    count = 1
    end = activities[0][1]

    for start, finish in activities[1:]:
        if start >= end:
            count += 1
            end = finish

    return count


def activity_selection_all(activities: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """Return the selected activities."""
    if not activities:
        return []

    activities.sort(key=lambda x: x[1])
    result = [activities[0]]
    end = activities[0][1]

    for start, finish in activities[1:]:
        if start >= end:
            result.append((start, finish))
            end = finish

    return result


# =============================================================================
# SECTION 2: JUMP GAME
# =============================================================================

def can_reach_end(nums: List[int]) -> bool:
    """
    Can we reach the last index?

    Time: O(n), Space: O(1)
    """
    max_reach = 0

    for i, jump in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + jump)

    return True


def min_jumps(nums: List[int]) -> int:
    """
    Minimum jumps to reach end.

    Time: O(n), Space: O(1)
    """
    if len(nums) <= 1:
        return 0

    jumps = 0
    current_end = 0
    max_reach = 0

    for i in range(len(nums) - 1):
        max_reach = max(max_reach, i + nums[i])

        if i == current_end:
            jumps += 1
            current_end = max_reach

    return jumps


# =============================================================================
# SECTION 3: HUFFMAN CODING (Concept)
# =============================================================================

import heapq
from collections import defaultdict


class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def huffman_encoding(data: str) -> Tuple[dict, str]:
    """
    Huffman coding for data compression.

    Time: O(n log n), Space: O(n)
    """
    if not data:
        return {}, ""

    # Build frequency table
    freq = defaultdict(int)
    for char in data:
        freq[char] += 1

    # Build min heap
    heap = [HuffmanNode(char, f) for char, f in freq.items()]
    heapq.heapify(heap)

    # Build Huffman tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        parent = HuffmanNode(None, left.freq + right.freq)
        parent.left = left
        parent.right = right
        heapq.heappush(heap, parent)

    # Generate codes
    codes = {}

    def generate_codes(node, code=""):
        if node is None:
            return
        if node.char is not None:
            codes[node.char] = code
            return
        generate_codes(node.left, code + "0")
        generate_codes(node.right, code + "1")

    root = heap[0]
    generate_codes(root)

    # Encode
    encoded = "".join(codes[char] for char in data)

    return codes, encoded


# =============================================================================
# SECTION 4: GAS STATION
# =============================================================================

def can_complete_circuit(gas: List[int], cost: List[int]) -> int:
    """
    Find starting station where circular trip is possible.

    Time: O(n), Space: O(1)
    """
    if sum(gas) < sum(cost):
        return -1

    total = 0
    start = 0

    for i in range(len(gas)):
        total += gas[i] - cost[i]

        if total < 0:
            start = i + 1
            total = 0

    return start


# =============================================================================
# SECTION 5: PARTITION LABELS
# =============================================================================

def partition_labels(s: str) -> List[int]:
    """
    Partition string so each character appears in one part.

    Time: O(n), Space: O(1)
    """
    last = {c: i for i, c in enumerate(s)}

    result = []
    start = end = 0

    for i, c in enumerate(s):
        end = max(end, last[c])

        if i == end:
            result.append(end - start + 1)
            start = i + 1

    return result


# =============================================================================
# SECTION 6: MAXIMUM SUBARRAY (KADANE)
# =============================================================================

def max_subarray_sum(nums: List[int]) -> int:
    """
    Maximum sum of contiguous subarray (Kadane's).

    Time: O(n), Space: O(1)
    """
    max_sum = nums[0]
    current = nums[0]

    for num in nums[1:]:
        current = max(num, current + num)
        max_sum = max(max_sum, current)

    return max_sum


def max_subarray_sum_indices(nums: List[int]) -> Tuple[int, int, int]:
    """Return (max_sum, start, end)."""
    max_sum = nums[0]
    current = nums[0]
    start = 0
    end = 0
    temp_start = 0

    for i in range(1, len(nums)):
        current = max(nums[i], current + nums[i])

        if current < nums[i]:
            temp_start = i

        if current > max_sum:
            max_sum = current
            start = temp_start
            end = i

    return max_sum, start, end


# =============================================================================
# SECTION 7: MOUNTAIN/INTERVAL PROBLEMS
# =============================================================================

def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """Merge overlapping intervals. Time: O(n log n)"""
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


def insert_interval(intervals: List[List[int]], new: List[int]) -> List[List[int]]:
    """Insert interval into sorted intervals. Time: O(n)"""
    merged = []
    i = 0
    n = len(intervals)
    start, end = new

    while i < n and intervals[i][1] < start:
        merged.append(intervals[i])
        i += 1

    while i < n and intervals[i][0] <= end:
        start = min(start, intervals[i][0])
        end = max(end, intervals[i][1])
        i += 1

    merged.append([start, end])
    merged.extend(intervals[i:])

    return merged


# =============================================================================
# SECTION 8: TESTING
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("GREEDY ALGORITHMS - TEST DEMO")
    print("=" * 60)

    # Activity Selection
    print("\n--- Activity Selection ---")
    activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10)]
    print(f"Activities: {activities}")
    print(f"Max non-overlapping: {activity_selection(activities)}")

    # Jump Game
    print("\n--- Jump Game ---")
    nums = [2, 3, 1, 1, 4]
    print(f"Can reach end of {nums}: {can_reach_end(nums)}")
    print(f"Min jumps in {nums}: {min_jumps(nums)}")

    # Max Subarray
    print("\n--- Max Subarray (Kadane) ---")
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = max_subarray_sum(nums)
    print(f"Max sum in {nums}: {result}")

    # Partition Labels
    print("\n--- Partition Labels ---")
    s = "ababcbacadefegdehijhklij"
    print(f"Partitions of '{s}': {partition_labels(s)}")

    # Merge Intervals
    print("\n--- Merge Intervals ---")
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(f"Merged {intervals}: {merge_intervals(intervals)}")

    # Gas Station
    print("\n--- Gas Station ---")
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    print(f"Start station: {can_complete_circuit(gas, cost)}")

    # Huffman Coding
    print("\n--- Huffman Coding ---")
    data = "hello world"
    codes, encoded = huffman_encoding(data)
    print(f"Data: '{data}'")
    print(f"Codes: {codes}")
    print(f"Encoded: {encoded}")

    print("\n" + "=" * 60)
    print("All tests completed!")
    print("=" * 60)
