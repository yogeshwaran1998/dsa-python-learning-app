"""
Problem-Solving Patterns - Quick Reference
==========================================
Common patterns for FAANG interview preparation.
"""

# =============================================================================
# PATTERN 1: TWO POINTERS
# =============================================================================

"""
Use when: Working with sorted arrays, finding pairs
Time: O(n), Space: O(1)

Example problems:
- Pair with target sum in sorted array
- Remove duplicates in-place
- Partition array
- Container with most water
"""

# Template:
def two_pointers_template(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        # Process
        if condition_met:
            return result
        elif arr[left] + arr[right] < target:
            left += 1
        else:
            right -= 1


# =============================================================================
# PATTERN 2: SLIDING WINDOW
# =============================================================================

"""
Use when: Subarray/substring problems
Time: O(n), Space: O(1) or O(k)

Example problems:
- Maximum sum of k elements
- Longest substring with k distinct
- Minimum window substring
"""

# Fixed window:
def fixed_window(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum, window_sum)
    return max_sum

# Variable window:
def variable_window(arr, target):
    left = 0
    current = 0
    min_len = float('inf')
    for right in range(len(arr)):
        current += arr[right]
        while current >= target:
            min_len = min(min_len, right - left + 1)
            current -= arr[left]
            left += 1
    return min_len


# =============================================================================
# PATTERN 3: BINARY SEARCH
# =============================================================================

"""
Use when: Sorted data, monotonic functions
Time: O(log n), Space: O(1)

Example problems:
- Find element in sorted array
- Find boundary (first true)
- Search in rotated array
- Square root
"""

def binary_search(arr, target):
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


# =============================================================================
# PATTERN 4: FAST & SLOW POINTERS
# =============================================================================

"""
Use when: Linked list cycle, finding middle
Time: O(n), Space: O(1)

Example problems:
- Detect cycle
- Find middle
- Find nth from end
"""

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


# =============================================================================
# PATTERN 5: BFS (Breadth-First Search)
# =============================================================================

"""
Use when: Level-order traversal, shortest path (unweighted)
Time: O(V + E), Space: O(V)

Example problems:
- Level order tree traversal
- Shortest path in grid
- Number of islands
"""

from collections import deque

def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


# =============================================================================
# PATTERN 6: DFS (Depth-First Search)
# =============================================================================

"""
Use when: Tree/graph traversal, backtracking
Time: O(V + E), Space: O(V)

Example problems:
- Tree path sums
- Subsets/permutations
- Topological sort
"""

def dfs(graph, node, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


# =============================================================================
# PATTERN 7: MONOTONIC STACK
# =============================================================================

"""
Use when: Next greater/smaller element
Time: O(n), Space: O(n)

Example problems:
- Next greater element
- Daily temperatures
- Largest rectangle in histogram
"""

def next_greater(arr):
    result = [-1] * len(arr)
    stack = []
    for i in range(len(arr)):
        while stack and arr[i] > arr[stack[-1]]:
            idx = stack.pop()
            result[idx] = arr[i]
        stack.append(i)
    return result


# =============================================================================
# PATTERN 8: HEAP / PRIORITY QUEUE
# =============================================================================

"""
Use when: Top K elements, merging sorted
Time: O(n log k), Space: O(k)

Example problems:
- K largest elements
- Merge k sorted lists
- Median of data stream
"""

import heapq

def top_k(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return sorted(heap, reverse=True)


# =============================================================================
# PATTERN 9: DYNAMIC PROGRAMMING
# =============================================================================

"""
Use when: Optimization with overlapping subproblems
Time: O(n²) or O(n*k), Space: varies

Example problems:
- Fibonacci
- Longest subsequence
- Knapsack
- Grid paths
"""

# 1D DP:
def fib_dp(n):
    if n <= 1: return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# 2D DP:
def grid_paths(m, n):
    dp = [[1] * n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]


# =============================================================================
# PATTERN 10: UNION-FIND
# =============================================================================

"""
Use when: Cycle detection, connected components
Time: O(α(n)), Space: O(V)

Example problems:
- Number of islands
- Kruskal's MST
- Friend circles
"""

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py: return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True


# =============================================================================
# QUICK DECISION GUIDE
# =============================================================================

def choose_pattern(problem_type):
    patterns = {
        "sorted_array_pair": "Two Pointers",
        "subarray_sum": "Sliding Window",
        "sorted_search": "Binary Search",
        "linked_list_cycle": "Fast & Slow",
        "shortest_path": "BFS",
        "tree_paths": "DFS",
        "next_element": "Monotonic Stack",
        "top_k": "Heap",
        "optimization": "DP",
        "connected": "Union-Find",
    }
    return patterns.get(problem_type, "Unknown")


# =============================================================================
# TESTING
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("PATTERNS QUICK REFERENCE")
    print("=" * 60)

    print("\nPattern -> Use When:")
    print("Two Pointers -> Sorted array, pairs")
    print("Sliding Window -> Subarray problems")
    print("Binary Search -> Sorted data")
    print("Fast-Slow -> Linked list cycle")
    print("BFS -> Shortest path, level-order")
    print("DFS -> Tree paths, backtracking")
    print("Monotonic Stack -> Next element problems")
    print("Heap -> Top K problems")
    print("DP -> Optimization problems")
    print("Union-Find -> Connected components")

    print("\n" + "=" * 60)
    print("All patterns ready for interview!")
    print("=" * 60)
