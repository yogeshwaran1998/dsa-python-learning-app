"""
Graphs - Implementation and Examples
===================================
Comprehensive Python implementations for graph problems
commonly asked in FAANG interviews.
"""

from typing import List, Optional, Set, Tuple, Dict
from collections import deque, defaultdict
import heapq


# =============================================================================
# SECTION 1: GRAPH NODE AND REPRESENTATION
# =============================================================================

class GraphNode:
    """Node for graph representation."""

    def __init__(self, val: int = 0, neighbors: List['GraphNode'] = None):
        self.val = val
        self.neighbors = neighbors or []


# =============================================================================
# SECTION 2: BFS (BREADTH-FIRST SEARCH)
# =============================================================================

def bfs(graph: Dict[int, List[int]], start: int) -> List[int]:
    """
    BFS traversal from start node.

    Time: O(V + E), Space: O(V)
    """
    visited = {start}
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


def bfs_matrix(grid: List[List[int]], start: Tuple[int, int]) -> List[Tuple[int, int]]:
    """BFS on 2D grid."""
    if not grid or not grid[0]:
        return []

    rows, cols = len(grid), len(grid[0])
    visited = set([start])
    queue = deque([start])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    result = []

    while queue:
        row, col = queue.popleft()
        result.append((row, col))

        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc))

    return result


def number_of_islands(grid: List[List[str]]) -> int:
    """
    Count number of islands using BFS.

    Time: O(m * n), Space: O(m * n)
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    islands = 0

    def bfs_island(r, c):
        queue = deque([(r, c)])
        grid[r][c] = '0'

        while queue:
            row, col = queue.popleft()
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                    grid[nr][nc] = '0'
                    queue.append((nr, nc))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                islands += 1
                bfs_island(r, c)

    return islands


def flood_fill(image: List[List[int]], sr: int, sc: int,
               newColor: int) -> List[List[int]]:
    """
    Flood fill algorithm (BFS).

    Time: O(m * n), Space: O(m * n)
    """
    if not image:
        return image

    rows, cols = len(image), len(image[0])
    original = image[sr][sc]
    if original == newColor:
        return image

    queue = deque([(sr, sc)])
    image[sr][sc] = newColor

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        r, c = queue.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == original:
                image[nr][nc] = newColor
                queue.append((nr, nc))

    return image


# =============================================================================
# SECTION 3: DFS (DEPTH-FIRST SEARCH)
# =============================================================================

def dfs(graph: Dict[int, List[int]], start: int) -> List[int]:
    """
    DFS traversal from start node.

    Time: O(V + E), Space: O(V)
    """
    visited = set()
    result = []

    def dfs_helper(node):
        if node in visited:
            return

        visited.add(node)
        result.append(node)

        for neighbor in graph.get(node, []):
            dfs_helper(neighbor)

    dfs_helper(start)
    return result


def dfs_iterative(graph: Dict[int, List[int]], start: int) -> List[int]:
    """DFS using explicit stack."""
    visited = set()
    stack = [start]
    result = []

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        result.append(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                stack.append(neighbor)

    return result


def clone_graph(node: Optional[GraphNode]) -> Optional[GraphNode]:
    """
    Clone undirected graph.

    Time: O(V + E), Space: O(V)
    """
    if not node:
        return None

    # BFS to create all nodes
    old_to_new = {}

    def dfs_clone(node):
        if node in old_to_new:
            return old_to_new[node]

        new_node = GraphNode(node.val)
        old_to_new[node] = new_node

        for neighbor in node.neighbors:
            new_node.neighbors.append(dfs_clone(neighbor))

        return new_node

    return dfs_clone(node)


def number_of_provinces(is_connected: List[List[int]]) -> int:
    """
    Find number of connected components using DFS.

    Time: O(n²), Space: O(n)
    """
    n = len(is_connected)
    visited = set()
    provinces = 0

    def dfs(city):
        visited.add(city)
        for neighbor in range(n):
            if is_connected[city][neighbor] and neighbor not in visited:
                dfs(neighbor)

    for i in range(n):
        if i not in visited:
            provinces += 1
            dfs(i)

    return provinces


# =============================================================================
# SECTION 4: SHORTEST PATH - BFS
# =============================================================================

def shortest_path(grid: List[List[int]], start: Tuple[int, int],
                  target: Tuple[int, int]) -> int:
    """
    Find shortest path in unweighted grid.

    Time: O(m * n), Space: O(m * n)
    """
    if not grid:
        return -1

    rows, cols = len(grid), len(grid[0])

    if grid[start[0]][start[1]] == 1 or grid[target[0]][target[1]] == 1:
        return -1

    queue = deque([(start[0], start[1], 0)])
    visited = {start}

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        r, c, dist = queue.popleft()

        if (r, c) == target:
            return dist

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols and
                    (nr, nc) not in visited and grid[nr][nc] == 0):
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))

    return -1


def ladder_length(begin_word: str, end_word: str,
                  word_list: List[str]) -> int:
    """
    Word ladder - shortest transformation sequence.

    Time: O(N * L * 26), Space: O(N * L)
    """
    word_set = set(word_list)
    if end_word not in word_set:
        return 0

    queue = deque([(begin_word, 1)])
    visited = {begin_word}

    while queue:
        word, level = queue.popleft()

        if word == end_word:
            return level

        # Try all possible single character changes
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + c + word[i + 1:]

                if new_word in word_set and new_word not in visited:
                    visited.add(new_word)
                    queue.append((new_word, level + 1))

    return 0


# =============================================================================
# SECTION 5: DIJKSTRA'S ALGORITHM
# =============================================================================

def dijkstra(graph: Dict[int, List[Tuple[int, int]]], start: int) -> Dict[int, int]:
    """
    Find shortest paths from start to all nodes.

    Time: O((V + E) log V), Space: O(V)
    """
    dist = {start: 0}
    pq = [(0, start)]

    while pq:
        d, node = heapq.heappop(pq)

        if d > dist.get(node, float('inf')):
            continue

        for neighbor, weight in graph.get(node, []):
            new_dist = d + weight

            if new_dist < dist.get(neighbor, float('inf')):
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return dist


def network_delay_time(times: List[List[int]], n: int, k: int) -> int:
    """
    Find time for signal to reach all nodes.

    Time: O(E log V), Space: O(V + E)
    """
    graph = defaultdict(list)

    for u, v, w in times:
        graph[u].append((v, w))

    dist = {k: 0}
    pq = [(0, k)]

    while pq:
        time, node = heapq.heappop(pq)

        if time > dist.get(node, float('inf')):
            continue

        for neighbor, w in graph[node]:
            new_time = time + w
            if new_time < dist.get(neighbor, float('inf')):
                dist[neighbor] = new_time
                heapq.heappush(pq, (new_time, neighbor))

    if len(dist) == n:
        return max(dist.values())

    return -1


def minimum_effort_path(heights: List[List[int]]) -> int:
    """
    Find minimum effort path using Dijkstra.

    Time: O(m * n log(m * n)), Space: O(m * n)
    """
    rows, cols = len(heights), len(heights[0])

    def neighbors(r, c):
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                yield nr, nc

    dist = {(0, 0): 0}
    pq = [(0, 0, 0)]

    while pq:
        effort, r, c = heapq.heappop(pq)

        if (r, c) == (rows - 1, cols - 1):
            return effort

        if effort > dist.get((r, c), float('inf')):
            continue

        for nr, nc in neighbors(r, c):
            new_effort = max(effort, abs(heights[r][c] - heights[nr][nc]))
            if new_effort < dist.get((nr, nc), float('inf')):
                dist[(nr, nc)] = new_effort
                heapq.heappush(pq, (new_effort, nr, nc))

    return -1


# =============================================================================
# SECTION 6: BELLMAN-FORD
# =============================================================================

def bellman_ford(vertices: int, edges: List[List[int]], source: int) -> List[int]:
    """
    Bellman-Ford for shortest paths (handles negative weights).

    Time: O(V * E), Space: O(V)
    """
    dist = [float('inf')] * vertices
    dist[source] = 0

    # Relax edges V-1 times
    for _ in range(vertices - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Check for negative cycles
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            return []  # Negative cycle detected

    return dist


# =============================================================================
# SECTION 7: TOPOLOGICAL SORT
# =============================================================================

def topological_sort_kahn(n: int, prerequisites: List[List[int]]) -> List[int]:
    """
    Topological sort using Kahn's algorithm.

    Time: O(V + E), Space: O(V)
    """
    graph = defaultdict(list)
    in_degree = [0] * n

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1

    queue = deque([i for i in range(n) if in_degree[i] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return result if len(result) == n else []


def can_finish_all_courses(n: int, prerequisites: List[List[int]]) -> bool:
    """Check if all courses can be finished."""
    return len(topological_sort_kahn(n, prerequisites)) == n


def find_order(n: int, prerequisites: List[List[int]]) -> List[int]:
    """Find valid course order."""
    return topological_sort_kahn(n, prerequisites)


# =============================================================================
# SECTION 8: UNION-FIND (DISJOINT SET)
# =============================================================================

class UnionFind:
    """Union-Find (Disjoint Set Union)."""

    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        px, py = self.find(x), self.find(y)
        if px == py:
            return

        # Union by rank
        if self.rank[px] < self.rank[py]:
            px, py = py, px

        self.parent[py] = px

        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1


def number_of_connected_components(n: int, edges: List[List[int]]) -> int:
    """
    Find number of connected components using Union-Find.

    Time: O(n + E * α(n)), Space: O(n)
    """
    uf = UnionFind(n)

    for u, v in edges:
        uf.union(u, v)

    return len(set(uf.find(i) for i in range(n)))


def regions_by_slashes(grid: List[str]) -> int:
    """
    Find regions formed by slashes.

    Time: O(n² * α(n)), Space: O(n²)
    """
    n = len(grid)
    uf = UnionFind(4 * n * n)

    def index(i, j, k):
        return 4 * (i * n + j) + k

    for i in range(n):
        for j in range(n):
            if i > 0:
                uf.union(index(i, j, 0), index(i - 1, j, 1))
            if i < n - 1:
                uf.union(index(i, j, 1), index(i + 1, j, 0))
            if j > 0:
                uf.union(index(i, j, 2), index(i, j - 1, 3))
            if j < n - 1:
                uf.union(index(i, j, 3), index(i, j + 1, 2))

            if grid[i][j] == '/':
                uf.union(index(i, j, 0), index(i, j, 2))
                uf.union(index(i, j, 1), index(i, j, 3))
            elif grid[i][j] == '\\':
                uf.union(index(i, j, 0), index(i, j, 3))
                uf.union(index(i, j, 1), index(i, j, 2))
            else:
                uf.union(index(i, j, 0), index(i, j, 1))
                uf.union(index(i, j, 1), index(i, j, 2))
                uf.union(index(i, j, 2), index(i, j, 3))

    return len(set(uf.find(i) for i in range(4 * n * n)))


# =============================================================================
# SECTION 9: TESTING AND DEMO
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("GRAPH ALGORITHMS - TEST DEMO")
    print("=" * 60)

    # Test BFS
    print("\n--- BFS ---")
    graph = {
        1: [2, 3],
        2: [1, 4],
        3: [1, 4, 5],
        4: [2, 3],
        5: [3]
    }
    print(f"BFS from 1: {bfs(graph, 1)}")

    # Test Number of Islands
    print("\n--- Number of Islands ---")
    grid = [
        ["1", "1", "1"],
        ["0", "1", "0"],
        ["1", "1", "1"]
    ]
    print(f"Islands: {number_of_islands([row[:] for row in grid])}")

    # Test Flood Fill
    print("\n--- Flood Fill ---")
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    result = flood_fill(image, 1, 1, 2)
    print(f"Flood fill result: {result}")

    # Test Number of Provinces
    print("\n--- Number of Provinces ---")
    is_connected = [
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 1]
    ]
    print(f"Provinces: {number_of_provinces(is_connected)}")

    # Test Dijkstra
    print("\n--- Dijkstra ---")
    dijkstra_graph = {
        0: [(1, 4), (2, 1)],
        1: [(0, 4), (2, 2), (3, 1)],
        2: [(0, 1), (1, 2), (3, 5)],
        3: [(1, 1), (2, 5)]
    }
    print(f"Shortest from 0: {dijkstra(dijkstra_graph, 0)}")

    # Test Course Schedule
    print("\n--- Course Schedule ---")
    n = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    print(f"Can finish: {can_finish_all_courses(n, prerequisites)}")
    print(f"Order: {find_order(n, prerequisites)}")

    # Test Word Ladder
    print("\n--- Word Ladder ---")
    begin = "hit"
    end = "cog"
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    result = ladder_length(begin, end, words)
    print(f"Ladder length: {result}")

    # Test Union-Find
    print("\n--- Union-Find ---")
    edges = [[0, 1], [1, 2], [3, 4]]
    print(f"Components (5 nodes): {number_of_connected_components(5, edges)}")

    print("\n" + "=" * 60)
    print("All tests completed!")
    print("=" * 60)
