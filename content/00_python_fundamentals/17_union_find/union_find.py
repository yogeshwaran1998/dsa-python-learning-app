"""
Union Find (Disjoint Set Union) Pattern - Implementation and Examples
=====================================================================
Comprehensive Python implementations of Union Find patterns
commonly asked in FAANG interviews.

Topics covered:
1. Basic Union Find implementation
2. Path compression
3. Union by rank/size
4. Connected components problems
"""

from typing import List, Dict, Optional


# =============================================================================
# SECTION 1: BASIC UNION FIND
# =============================================================================

class UnionFind:
    """
    Union Find (Disjoint Set Union) data structure.

    Supports:
    - find(x): Find root/representative of set containing x
    - union(x, y): Merge sets containing x and y
    - connected(x, y): Check if x and y are in same set

    With path compression and union by rank:
    - Time complexity is almost O(1) amortized
    - Specifically O(alpha(n)) where alpha is inverse Ackermann
    """

    def __init__(self, n: int):
        """
        Initialize Union Find with n elements.
        Each element starts as its own parent (root).

        How it works:
        - parent[i] = i means i is its own root
        - rank[i] = 0 tracks tree depth for union by rank

        Time: O(n), Space: O(n)

        Args:
            n: Number of elements (0 to n-1)
        """
        # Parent array: each element is initially its own parent
        self.parent = list(range(n))

        # Rank/size array for union by rank optimization
        # Higher rank means deeper tree
        self.rank = [0] * n

        # Optional: track size of each component
        self.size = [1] * n

    def find(self, x: int) -> int:
        """
        Find root/representative of set containing x.

        How it works (with path compression):
        - If x is not its own parent, recursively find root
        - During return, make each node point directly to root
        - This flattens the tree for faster future lookups

        Time: O(alpha(n)) ~ O(1) amortized

        Args:
            x: Element to find root for

        Returns:
            Root element of the set containing x

        Example:
            parent = [0, 1, 2, 3]
            find(2) -> 2
            After union(0,2): parent = [2, 1, 2, 3]
            find(0) -> 2 (with path compression: parent[0] = 2)
        """
        # Base case: x is its own parent (root)
        # Path compression: make parent[x] point directly to root
        if self.parent[x] != x:
            # Recursively find root and compress path
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def find_iterative(self, x: int) -> int:
        """
        Iterative version of find (same complexity).
        Useful for very deep trees to avoid stack overflow.
        """
        root = x

        # Find root
        while root != self.parent[root]:
            root = self.parent[root]

        # Path compression: make all nodes point to root
        while x != root:
            next_x = self.parent[x]
            self.parent[x] = root
            x = next_x

        return root

    def union(self, x: int, y: int) -> None:
        """
        Merge sets containing x and y.

        How it works (with union by rank):
        - Find roots of both elements
        - If same root, already in same set
        - Attach smaller rank tree under larger rank tree
        - This keeps tree balanced

        Time: O(alpha(n)) ~ O(1) amortized

        Args:
            x: First element
            y: Second element
        """
        # Find roots of both elements
        root_x = self.find(x)
        root_y = self.find(y)

        # Already in same set - nothing to do
        if root_x == root_y:
            return

        # Union by rank: attach smaller tree under larger
        if self.rank[root_x] < self.rank[root_y]:
            # root_x has smaller rank, attach under root_y
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        elif self.rank[root_x] > self.rank[root_y]:
            # root_y has smaller rank, attach under root_x
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        else:
            # Same rank - choose one and increment its rank
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
            self.rank[root_x] += 1

    def connected(self, x: int, y: int) -> bool:
        """
        Check if x and y are in the same set.

        How it works:
        - Find roots of both elements
        - If same root, they're connected

        Time: O(alpha(n)) ~ O(1)

        Args:
            x: First element
            y: Second element

        Returns:
            True if x and y are in same set
        """
        return self.find(x) == self.find(y)

    def get_component_size(self, x: int) -> int:
        """
        Get size of component containing x.
        """
        return self.size[self.find(x)]

    def get_number_of_components(self) -> int:
        """
        Get total number of components.

        How it works:
        - Count unique roots

        Time: O(n)
        """
        # Use set to get unique roots
        roots = set()
        for i in range(len(self.parent)):
            roots.add(self.find(i))
        return len(roots)


# =============================================================================
# SECTION 2: CONNECTED COMPONENTS PROBLEMS
# =============================================================================

def number_of_components(n: int, edges: List[List[int]]) -> int:
    """
    Find number of connected components in undirected graph.

    How it works:
    - Initialize UnionFind with n nodes
    - For each edge, union the two nodes
    - Count unique roots

    Time: O(n + m) where m = number of edges, Space: O(n)

    Args:
        n: Number of nodes (0 to n-1)
        edges: List of edges [u, v]

    Returns:
        Number of connected components

    Example:
        Input: n = 5, edges = [[0,1], [1,2], [3,4]]
        Output: 2 (components: {0,1,2} and {3,4})
    """
    # Create UnionFind with n nodes
    uf = UnionFind(n)

    # Process each edge
    for u, v in edges:
        uf.union(u, v)

    # Count connected components
    return uf.get_number_of_components()


def count_provinces(is_connected: List[List[int]]) -> int:
    """
    Count provinces (connected components) in matrix form.
    Province is a group of directly or indirectly connected cities.

    How it works:
    - Convert adjacency matrix to edge list
    - Use UnionFind to count components

    Time: O(n^2) for matrix, Space: O(n)

    Args:
        is_connected: n x n matrix where is_connected[i][j] = 1 if connected

    Returns:
        Number of provinces
    """
    n = len(is_connected)
    uf = UnionFind(n)

    # Process matrix - only need upper triangle to avoid duplicates
    for i in range(n):
        for j in range(i + 1, n):
            if is_connected[i][j] == 1:
                uf.union(i, j)

    return uf.get_number_of_components()


def is_graph_valid_tree(n: int, edges: List[List[int]]) -> bool:
    """
    Determine if edges form a valid tree.

    How it works:
    - Valid tree if: connected AND no cycles
    - Equivalent to: n nodes and n-1 edges, and connected

    Time: O(n + m), Space: O(n)

    Args:
        n: Number of nodes
        edges: List of edges

    Returns:
        True if edges form a valid tree
    """
    # Tree must have exactly n-1 edges
    if len(edges) != n - 1:
        return False

    # Create UnionFind
    uf = UnionFind(n)

    # Process edges and check for cycle
    for u, v in edges:
        # If already connected, adding this edge creates cycle
        if uf.connected(u, v):
            return False
        uf.union(u, v)

    # Must be fully connected
    return uf.get_number_of_components() == 1


# =============================================================================
# SECTION 3: CYCLE DETECTION
# =============================================================================

def find_redundant_connection(edges: List[List[int]]) -> List[int]:
    """
    Find the edge that creates a cycle in the graph.
    Process edges in order - first edge that creates cycle is redundant.

    How it works:
    - Use UnionFind to detect cycles
    - If edge connects two nodes already connected, it's redundant

    Time: O(n), Space: O(n)

    Args:
        edges: List of edges in order

    Returns:
        Edge that creates cycle [u, v]

    Example:
        Input: [[1,2], [1,3], [2,3]]
        Output: [2, 3] (adding this creates cycle)
    """
    # n nodes, n-1 edges initially valid, nth edge is redundant
    n = len(edges)
    uf = UnionFind(n)

    # Process each edge
    for u, v in edges:
        # Convert to 0-indexed
        u -= 1
        v -= 1

        # If already connected, this edge creates cycle
        if uf.connected(u, v):
            return [u + 1, v + 1]

        # Otherwise, union them
        uf.union(u, v)

    # Should never reach here for valid input
    return []


def find_redundant_connection_2(edges: List[List[int]]) -> List[List[int]]:
    """
    Find all edges that can be removed to make graph acyclic.
    Returns all edges that create cycles when processed last.

    Time: O(n), Space: O(n)
    """
    n = len(edges) + 1
    uf = UnionFind(n)
    result = []

    for u, v in edges:
        u -= 1
        v -= 1

        if uf.connected(u, v):
            result.append([u + 1, v + 1])
        else:
            uf.union(u, v)

    return result


# =============================================================================
# SECTION 4: KRUSKAL'S ALGORITHM (MST)
# =============================================================================

def kruskal_mst(n: int, edges: List[List[int]]) -> int:
    """
    Find minimum spanning tree weight using Kruskal's algorithm.
    MST connects all nodes with minimum total edge weight.

    How it works:
    - Sort edges by weight
    - Use UnionFind to avoid cycles
    - Add edge if it connects different components

    Time: O(m log m) for sorting, Space: O(n)

    Args:
        n: Number of nodes
        edges: List of [weight, u, v]

    Returns:
        Weight of minimum spanning tree
    """
    # Sort edges by weight
    edges.sort(key=lambda x: x[0])

    uf = UnionFind(n)
    mst_weight = 0
    edges_used = 0

    for weight, u, v in edges:
        # Skip if would create cycle
        if uf.connected(u, v):
            continue

        # Add edge to MST
        uf.union(u, v)
        mst_weight += weight
        edges_used += 1

        # Stop when we have n-1 edges (MST complete)
        if edges_used == n - 1:
            break

    return mst_weight


# =============================================================================
# SECTION 5: DYNAMIC CONNECTIVITY PROBLEMS
# =============================================================================

class NumberOfIslandsUnionFind:
    """
    Use UnionFind to solve Number of Islands problem.
    Efficient when we need to process islands dynamically.
    """

    def __init__(self, grid: List[List[str]]):
        """
        Initialize UnionFind for grid.
        Create a node for each land cell.
        """
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.grid = grid

        # Count number of land cells
        self.count = 0
        for row in range(self.rows):
            for col in range(self.cols):
                if grid[row][col] == '1':
                    self.count += 1

        # Initialize UnionFind with total cells
        # But we only consider land cells
        self.parent = list(range(self.rows * self.cols))
        self.rank = [0] * (self.rows * self.cols)

    def find(self, x: int) -> int:
        """Path compression find."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        """Union by rank."""
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

            # Merge reduces island count
            self.count -= 1

    def get_index(self, row: int, col: int) -> int:
        """Convert 2D coordinates to 1D index."""
        return row * self.cols + col

    def process_grid(self) -> int:
        """
        Process entire grid and return number of islands.

        For each land cell:
        - Mark as visited (convert to '0')
        - Union with all adjacent land cells

        Time: O(m * n), Space: O(m * n)
        """
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] != '1':
                    continue

                # Mark as visited
                self.grid[row][col] = '0'

                # Union with neighbors
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < self.rows and 0 <= nc < self.cols:
                        if self.grid[nr][nc] == '1':
                            self.union(
                                self.get_index(row, col),
                                self.get_index(nr, nc)
                            )

        return self.count


# =============================================================================
# SECTION 6: WEIGHTED UNION FIND
# =============================================================================

class WeightedUnionFind:
    """
    UnionFind that tracks additional information.
    Useful for problems requiring component weights or distances.
    """

    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        # Track minimum distance to any node in component
        self.min_dist = [float('inf')] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int, distance: int) -> None:
        """Union two components with given distance."""
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            # Merge and update min distance
            self.parent[root_y] = root_x
            self.min_dist[root_x] = min(
                self.min_dist[root_x],
                self.min_dist[root_y],
                distance
            )


# =============================================================================
# SECTION 7: PRACTICAL APPLICATIONS
# =============================================================================

def friend_circles(n: int, friends: List[List[int]]) -> int:
    """
    Find number of friend circles.
    friends[i][j] = 1 means i and j are friends.

    Time: O(n^2), Space: O(n)

    Example:
        Input: n = 4, friends = [[1,1,0,0], [1,1,1,0], [0,1,1,0], [0,0,0,1]]
        Output: 2 (circles: {0,1,2} and {3})
    """
    uf = UnionFind(n)

    # Process friendship matrix
    for i in range(n):
        for j in range(i + 1, n):
            if friends[i][j] == 1:
                uf.union(i, j)

    return uf.get_number_of_components()


def longest_consecutive_with_union_find(nums: List[int]) -> int:
    """
    Find longest consecutive sequence using UnionFind.
    (Alternative to hashset approach)

    Time: O(n), Space: O(n)

    Example:
        Input: [100, 4, 200, 1, 3, 2]
        Output: 4 (sequence: 1,2,3,4)
    """
    if not nums:
        return 0

    # Create UnionFind
    n = len(nums)
    uf = UnionFind(n)

    # Map value to index
    value_to_index = {num: i for i, num in enumerate(nums)}

    # Process each number
    for num in nums:
        if num in value_to_index:
            idx = value_to_index[num]

            # Union with num+1 if exists
            if num + 1 in value_to_index:
                uf.union(idx, value_to_index[num + 1])

            # Union with num-1 if exists
            if num - 1 in value_to_index:
                uf.union(idx, value_to_index[num - 1])

    # Find maximum component size
    max_size = 0
    for i in range(n):
        if uf.parent[i] == i:  # root
            max_size = max(max_size, uf.size[i])

    return max_size


# =============================================================================
# TEST FUNCTIONS
# =============================================================================

def run_tests():
    """Run test cases for all implementations."""

    # Test basic UnionFind
    uf = UnionFind(5)
    print("Initial components:", uf.get_number_of_components())  # 5

    # Test unions
    uf.union(0, 1)
    uf.union(2, 3)
    uf.union(0, 2)
    print("After unions:", uf.get_number_of_components())  # 2

    # Test connected
    print("Connected(0,3):", uf.connected(0, 3))  # True
    print("Connected(0,4):", uf.connected(0, 4))  # False

    # Test number of components
    n = 5
    edges = [[0, 1], [1, 2], [3, 4]]
    result = number_of_components(n, edges)
    print(f"Number of Components: {result}")  # 2

    # Test is valid tree
    result = is_graph_valid_tree(5, [[0, 1], [0, 2], [0, 3]])
    print(f"Is Valid Tree: {result}")  # False (not connected)

    # Test redundant connection
    edges = [[1, 2], [1, 3], [2, 3]]
    result = find_redundant_connection(edges)
    print(f"Redundant Connection: {result}")  # [2, 3]

    # Test friend circles
    n = 4
    friends = [
        [1, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 1]
    ]
    result = friend_circles(n, friends)
    print(f"Friend Circles: {result}")  # 2


if __name__ == "__main__":
    run_tests()
