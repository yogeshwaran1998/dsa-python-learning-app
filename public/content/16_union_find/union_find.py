"""
Union-Find - Implementation and Examples
======================================
Comprehensive Python implementations for Union-Find problems
commonly asked in FAANG interviews.
"""

from typing import List, Tuple


# =============================================================================
# SECTION 1: BASIC UNION-FIND
# =============================================================================

class UnionFind:
    """
    Union-Find with path compression and union by rank.

    Time: O(α(n)) amortized per operation
    Space: O(n)
    """

    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        """Find with path compression."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        """Union by rank. Returns True if merged."""
        px, py = self.find(x), self.find(y)
        if px == py:
            return False

        if self.rank[px] < self.rank[py]:
            px, py = py, px

        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1

        return True

    def connected(self, x: int, y: int) -> bool:
        """Check if x and y are in same set."""
        return self.find(x) == self.find(y)

    def count(self) -> int:
        """Count number of components."""
        return len(set(self.find(i) for i in range(len(self.parent))))


# =============================================================================
# SECTION 2: KRUSKAL'S MST
# =============================================================================

def kruskal_mst(n: int, edges: List[List[int]]) -> int:
    """
    Find minimum spanning tree weight using Kruskal's.

    Time: O(E log E), Space: O(V + E)
    """
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])

    uf = UnionFind(n)
    mst_weight = 0
    edges_used = 0

    for u, v, w in edges:
        if uf.union(u, v):
            mst_weight += w
            edges_used += 1
            if edges_used == n - 1:
                break

    return mst_weight if edges_used == n - 1 else -1


# =============================================================================
# SECTION 3: CYCLE DETECTION
# =============================================================================

def has_cycle(vertices: int, edges: List[List[int]]) -> bool:
    """
    Detect cycle in undirected graph.

    Time: O(E * α(V)), Space: O(V)
    """
    uf = UnionFind(vertices)

    for u, v in edges:
        if not uf.union(u, v):
            return True

    return False


def has_cycle_directed(vertices: int, edges: List[List[int]]) -> bool:
    """
    Detect cycle in directed graph using Union-Find variant.

    Note: Standard UF doesn't work well for directed.
    Use DFS instead for directed graphs.
    """
    from collections import defaultdict

    graph = defaultdict(list)
    in_degree = [0] * vertices

    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    # Kahn's algorithm
    queue = [i for i in range(vertices) if in_degree[i] == 0]
    count = 0

    while queue:
        node = queue.pop()
        count += 1

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return count != vertices


# =============================================================================
# SECTION 4: GRID CONNECTIVITY
# =============================================================================

def num_islands(grid: List[List[int]]) -> int:
    """
    Count islands using Union-Find.

    Time: O(m * n * α(m * n)), Space: O(m * n)
    """
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    uf = UnionFind(rows * cols)
    islands = sum(sum(row) for row in grid)

    def get_idx(r, c):
        return r * cols + c

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                continue

            # Check right neighbor
            if c + 1 < cols and grid[r][c + 1] == 1:
                if uf.union(get_idx(r, c), get_idx(r, c + 1)):
                    islands -= 1

            # Check down neighbor
            if r + 1 < rows and grid[r + 1][c] == 1:
                if uf.union(get_idx(r, c), get_idx(r + 1, c)):
                    islands -= 1

    return islands


def friend_circles(friendships: List[List[int]]) -> int:
    """
    Number of friend circles.

    Time: O(n² * α(n)), Space: O(n)
    """
    n = len(friendships)
    uf = UnionFind(n)

    for i in range(n):
        for j in range(n):
            if friendships[i][j] == 1:
                uf.union(i, j)

    return uf.count()


# =============================================================================
# SECTION 5: TESTING AND DEMO
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("UNION-FIND ALGORITHMS - TEST DEMO")
    print("=" * 60)

    # Test basic Union-Find
    print("\n--- Basic Operations ---")
    uf = UnionFind(5)
    uf.union(0, 1)
    uf.union(1, 2)
    print(f"Connected 0-2: {uf.connected(0, 2)}")
    print(f"Connected 0-4: {uf.connected(0, 4)}")
    print(f"Components: {uf.count()}")

    # Test Kruskal's MST
    print("\n--- Kruskal's MST ---")
    n = 4
    edges = [[0, 1, 10], [0, 2, 6], [0, 3, 5], [1, 3, 15], [2, 3, 4]]
    weight = kruskal_mst(n, edges)
    print(f"MST weight: {weight}")

    # Test Cycle Detection
    print("\n--- Cycle Detection ---")
    edges = [[0, 1], [1, 2], [2, 0]]
    print(f"Has cycle: {has_cycle(3, edges)}")

    # Test Number of Islands
    print("\n--- Number of Islands ---")
    grid = [[1, 1, 0], [0, 1, 0], [1, 1, 0]]
    print(f"Islands: {num_islands(grid)}")

    # Test Friend Circles
    print("\n--- Friend Circles ---")
    friends = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print(f"Circles: {friend_circles(friends)}")

    print("\n" + "=" * 60)
    print("All tests completed!")
    print("=" * 60)
