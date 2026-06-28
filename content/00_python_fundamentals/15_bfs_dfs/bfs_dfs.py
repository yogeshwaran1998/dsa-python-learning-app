"""
BFS and DFS Patterns - Implementation and Examples
================================================
Comprehensive Python implementations of BFS and DFS patterns
commonly asked in FAANG interviews.

Topics covered:
1. Recursive and iterative DFS
2. BFS with deque
3. Graph traversal
4. Tree traversals
"""

from typing import List, Optional, Set, Dict
from collections import deque, defaultdict


# =============================================================================
# SECTION 1: GRAPH NODE DEFINITION
# =============================================================================

class GraphNode:
    """
    Definition for a graph node in adjacency list representation.
    """

    def __init__(self, val: int = 0, neighbors: List['GraphNode'] = None):
        """
        Initialize graph node.

        Args:
            val: Value of the node
            neighbors: List of neighboring nodes
        """
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class TreeNode:
    """
    Definition for a binary tree node.
    """

    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        """
        Initialize tree node.

        Args:
            val: Value of the node
            left: Left child
            right: Right child
        """
        self.val = val
        self.left = left
        self.right = right


# =============================================================================
# SECTION 2: RECURSIVE DFS
# =============================================================================

def dfs_recursive(graph: Dict[int, List[int]], start: int, visited: Set[int]) -> None:
    """
    Perform depth-first search recursively.

    How it works:
    - Mark current node as visited
    - Process the node
    - Recursively visit all unvisited neighbors
    - This goes deep before exploring other branches

    Time: O(V + E), Space: O(V) for recursion stack

    Args:
        graph: Adjacency list representation
        start: Starting node
        visited: Set to track visited nodes
    """
    # Base case: if already visited, return
    if start in visited:
        return

    # Mark current node as visited
    visited.add(start)

    # Process the node (print in this case)
    print(f"Visited: {start}")

    # Recursively visit all neighbors
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)


def dfs_recursive_return(graph: Dict[int, List[int]], start: int) -> List[int]:
    """
    DFS that returns visited nodes in order.

    Time: O(V + E), Space: O(V)

    Args:
        graph: Adjacency list
        start: Starting node

    Returns:
        List of visited nodes in DFS order
    """
    visited = set()
    result = []

    def dfs(node: int):
        if node in visited:
            return

        visited.add(node)
        result.append(node)

        for neighbor in graph.get(node, []):
            dfs(neighbor)

    dfs(start)
    return result


def number_of_islands(grid: List[List[str]]) -> int:
    """
    Count number of islands in 2D grid.
    An island is surrounded by water and is formed by connecting adjacent lands.

    How it works:
    - Iterate through each cell
    - When we find unvisited land ('1'), start DFS
    - Mark all connected land as visited
    - Increment island count

    Time: O(m * n), Space: O(m * n) for visited set

    Args:
        grid: 2D grid of '1's (land) and '0's (water)

    Returns:
        Number of islands

    Example:
        Input: [['1','1','0'],['0','1','0'],['1','1','0']]
        Output: 1
    """
    if not grid or not grid[0]:
        return 0

    # Get dimensions
    rows = len(grid)
    cols = len(grid[0])

    # Set to track visited cells
    visited = set()

    # Directions for 4-connectivity (up, down, left, right)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def dfs(row: int, col: int) -> None:
        """
        Perform DFS to mark all connected land cells.
        """
        # Check bounds and if it's land
        if (row, col) in visited or grid[row][col] == '0':
            return

        # Mark as visited
        visited.add((row, col))

        # Explore all 4 neighbors
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            # Check bounds
            if 0 <= new_row < rows and 0 <= new_col < cols:
                if grid[new_row][new_col] == '1':
                    dfs(new_row, new_col)

    # Count islands
    island_count = 0

    # Iterate through each cell
    for i in range(rows):
        for j in range(cols):
            # If unvisited land found, start DFS
            if grid[i][j] == '1' and (i, j) not in visited:
                dfs(i, j)
                island_count += 1

    return island_count


def max_area_of_island(grid: List[List[int]]) -> int:
    """
    Find maximum area of an island.
    Area is number of cells in the island.

    Time: O(m * n), Space: O(m * n)

    Args:
        grid: 2D grid

    Returns:
        Maximum area of any island
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def dfs(row: int, col: int) -> int:
        """
        Return area of island starting from (row, col).
        """
        if (row, col) in visited or grid[row][col] == 0:
            return 0

        visited.add((row, col))
        area = 1

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < rows and 0 <= new_col < cols:
                area += dfs(new_row, new_col)

        return area

    max_area = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1 and (i, j) not in visited:
                max_area = max(max_area, dfs(i, j))

    return max_area


# =============================================================================
# SECTION 3: ITERATIVE DFS (USING STACK)
# =============================================================================

def dfs_iterative(graph: Dict[int, List[int]], start: int) -> List[int]:
    """
    Perform DFS using stack (iterative approach).

    How it works:
    - Use stack for DFS
    - Push start node onto stack
    - Pop from stack, visit if not visited
    - Push all unvisited neighbors

    Time: O(V + E), Space: O(V)

    Args:
        graph: Adjacency list
        start: Starting node

    Returns:
        List of visited nodes in DFS order
    """
    # Use list as stack
    stack = [start]
    visited = set()
    result = []

    while stack:
        # Pop from stack (LIFO gives depth-first)
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        result.append(node)

        # Add neighbors to stack (in reverse for consistent order)
        for neighbor in reversed(graph.get(node, [])):
            if neighbor not in visited:
                stack.append(neighbor)

    return result


def pacific_atlantic(matrix: List[List[int]]) -> List[List[int]]:
    """
    Find cells that can reach both Pacific and Atlantic oceans.
    Pacific is top and left edges, Atlantic is bottom and right edges.

    How it works:
    - Start from ocean edges and do DFS
    - Find cells that can reach both oceans

    Time: O(m * n), Space: O(m * n)

    Args:
        matrix: Height matrix

    Returns:
        List of [row, col] that can reach both oceans
    """
    if not matrix or not matrix[0]:
        return []

    rows, cols = len(matrix), len(matrix[0])

    # Track cells that can reach each ocean
    pacific = set()
    atlantic = set()

    # DFS from Pacific (top row and left column)
    def dfs(row: int, col: int, visited: Set):
        visited.add((row, col))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                # Can only flow to equal or higher cells
                if matrix[nr][nc] >= matrix[row][col]:
                    dfs(nr, nc, visited)

    # Start from Pacific edges
    for c in range(cols):
        dfs(0, c, pacific)
    for r in range(rows):
        dfs(r, 0, pacific)

    # Start from Atlantic edges
    for c in range(cols):
        dfs(rows - 1, c, atlantic)
    for r in range(rows):
        dfs(r, cols - 1, atlantic)

    # Find intersection
    return list(pacific.intersection(atlantic))


# =============================================================================
# SECTION 4: BFS WITH DEQUE
# =============================================================================

def bfs_shortest_path(graph: Dict[int, List[int]], start: int, end: int) -> int:
    """
    Find shortest path from start to end using BFS.

    How it works:
    - Use queue for BFS
    - Track distance from start
    - First time we reach end, that's shortest path

    Time: O(V + E), Space: O(V)

    Args:
        graph: Adjacency list
        start: Starting node
        end: Target node

    Returns:
        Shortest distance, or -1 if no path exists
    """
    if start == end:
        return 0

    # Use deque for O(1) popleft
    queue = deque([start])
    visited = {start}
    distance = 0

    while queue:
        # Process current level (all nodes at current distance)
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()

            # Explore neighbors
            for neighbor in graph.get(node, []):
                if neighbor == end:
                    return distance + 1

                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        distance += 1

    # No path found
    return -1


def bfs_level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Perform level-order traversal of binary tree.
    Returns list of levels, each level is list of node values.

    How it works:
    - Use BFS with queue
    - Track number of nodes at each level
    - Process level by level

    Time: O(n), Space: O(w) where w is max width

    Args:
        root: Root of binary tree

    Returns:
        List of levels, each level is list of node values
    """
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        # Get number of nodes at current level
        level_size = len(queue)
        level = []

        # Process all nodes at current level
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            # Add children to queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result


def binary_tree_right_side_view(root: Optional[TreeNode]) -> List[int]:
    """
    Get rightmost nodes at each level (right side view).

    How it works:
    - Use BFS
    - For each level, the last node is the rightmost

    Time: O(n), Space: O(w)

    Args:
        root: Root of binary tree

    Returns:
        List of rightmost node values at each level
    """
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            node = queue.popleft()

            # If last node in level, add to result
            if i == level_size - 1:
                result.append(node.val)

            # Add children
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result


def clone_graph(node: Optional[GraphNode]) -> Optional[GraphNode]:
    """
    Clone (deep copy) an undirected graph.

    How it works:
    - Use BFS/DFS with hashmap
    - Map original node to cloned node
    - First pass: create all nodes
    - Second pass: connect neighbors

    Time: O(V + E), Space: O(V)

    Args:
        node: Starting node of graph

    Returns:
        Deep copy of the graph
    """
    if not node:
        return None

    # Hashmap to map original to clone
    old_to_new = {}

    # BFS to clone all nodes
    queue = deque([node])
    old_to_new[node] = GraphNode(node.val)

    while queue:
        original = queue.popleft()
        cloned = old_to_new[original]

        for neighbor in original.neighbors:
            if neighbor not in old_to_new:
                # Create new node for this neighbor
                old_to_new[neighbor] = GraphNode(neighbor.val)
                queue.append(neighbor)

            # Connect cloned nodes
            cloned.neighbors.append(old_to_new[neighbor])

    return old_to_new[node]


# =============================================================================
# SECTION 5: GRAPH TRAVERSAL PATTERNS
# =============================================================================

def count_connected_components(n: int, edges: List[List[int]]) -> int:
    """
    Count number of connected components in undirected graph.

    How it works:
    - Build adjacency list
    - For each unvisited node, do DFS/BFS to mark all connected nodes
    - Count components

    Time: O(V + E), Space: O(V + E)

    Args:
        n: Number of nodes (0 to n-1)
        edges: List of edges [u, v]

    Returns:
        Number of connected components
    """
    # Build adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    def dfs(node: int):
        """Mark all connected nodes as visited."""
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor)

    components = 0

    # For each node not visited, start DFS and increment count
    for i in range(n):
        if i not in visited:
            dfs(i)
            components += 1

    return components


def is_bipartite(graph: List[List[int]]) -> bool:
    """
    Check if graph is bipartite.
    A graph is bipartite if we can color nodes with 2 colors
    such that no adjacent nodes have same color.

    How it works:
    - Use BFS/DFS to try coloring graph
    - If we encounter conflict, not bipartite

    Time: O(V + E), Space: O(V)

    Args:
        graph: Adjacency list representation

    Returns:
        True if bipartite, False otherwise
    """
    n = len(graph)
    # -1 = uncolored, 0 and 1 are two colors
    color = [-1] * n

    for start in range(n):
        if color[start] != -1:
            continue

        # BFS from uncolored node
        queue = deque([start])
        color[start] = 0

        while queue:
            node = queue.popleft()

            for neighbor in graph[node]:
                if color[neighbor] == -1:
                    # Color with opposite color
                    color[neighbor] = 1 - color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    # Conflict: not bipartite
                    return False

    return True


def find_order(num_courses: int, prerequisites: List[List[int]]) -> List[int]:
    """
    Find valid course order given prerequisites (topological sort).

    How it works:
    - Build graph and in-degree array
    - Use Kahn's algorithm (BFS)
    - Process nodes with 0 in-degree
    - Reduce in-degree of neighbors

    Time: O(V + E), Space: O(V + E)

    Args:
        num_courses: Number of courses
        prerequisites: [course, prerequisite] pairs

    Returns:
        Order of courses, or empty if not possible
    """
    # Build graph and in-degree
    graph = defaultdict(list)
    in_degree = [0] * num_courses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1

    # Start with courses that have no prerequisites
    queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
    result = []

    while queue:
        course = queue.popleft()
        result.append(course)

        # Reduce in-degree of dependent courses
        for next_course in graph[course]:
            in_degree[next_course] -= 1
            if in_degree[next_course] == 0:
                queue.append(next_course)

    # Check if all courses are taken
    if len(result) == num_courses:
        return result

    # Cycle exists, can't complete all courses
    return []


# =============================================================================
# SECTION 6: ADDITIONAL DFS/BFS PROBLEMS
# =============================================================================

def word_ladder(begin_word: str, end_word: str, word_list: List[str]) -> int:
    """
    Find shortest transformation sequence length.
    Each transformation changes exactly one character.
    Must go through words in word_list.

    How it works:
    - Use BFS to find shortest path
    - Each level represents one transformation step

    Time: O(N * L) where N = word count, L = word length
    Space: O(N * L)

    Args:
        begin_word: Starting word
        end_word: Target word
        word_list: List of valid words

    Returns:
        Length of shortest sequence, or 0 if not possible
    """
    # Convert to set for O(1) lookup
    word_set = set(word_list)

    if end_word not in word_set:
        return 0

    # BFS
    queue = deque([(begin_word, 1)])  # (word, level)
    visited = {begin_word}

    while queue:
        word, level = queue.popleft()

        # Try changing each character
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c == word[i]:
                    continue

                new_word = word[:i] + c + word[i+1:]

                if new_word == end_word:
                    return level + 1

                if new_word in word_set and new_word not in visited:
                    visited.add(new_word)
                    queue.append((new_word, level + 1))

    return 0


def number_of_closed_islands(grid: List[List[int]]) -> int:
    """
    Count number of closed islands (land cells that cannot reach boundary).

    How it works:
    - Similar to number of islands
    - But islands touching boundary are not counted

    Time: O(m * n), Space: O(m * n)

    Args:
        grid: 2D grid

    Returns:
        Number of closed islands
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def dfs(row: int, col: int) -> bool:
        """
        Returns True if this land is closed.
        """
        # If we reach boundary, not closed
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return False

        if (row, col) in visited or grid[row][col] == 0:
            return True

        visited.add((row, col))

        # Check all neighbors
        closed = True
        for dr, dc in directions:
            if not dfs(row + dr, col + dc):
                closed = False

        return closed

    count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1 and (i, j) not in visited:
                if dfs(i, j):
                    count += 1

    return count


# =============================================================================
# TEST FUNCTIONS
# =============================================================================

def run_tests():
    """Run test cases for all implementations."""

    # Test DFS
    graph = {1: [2, 3], 2: [1, 4], 3: [1, 4, 5], 4: [2, 3], 5: [3]}
    result = dfs_recursive_return(graph, 1)
    print(f"DFS: {result}")

    # Test number of islands
    grid = [
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1']
    ]
    result = number_of_islands(grid)
    print(f"Number of Islands: {result}")

    # Test BFS level order
    # Build tree:     1
    #               /   \
    #              2     3
    #             / \   / \
    #            4   5 6   7
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    result = bfs_level_order(root)
    print(f"Level Order: {result}")

    # Test count connected components
    n = 5
    edges = [[0, 1], [1, 2], [3, 4]]
    result = count_connected_components(n, edges)
    print(f"Connected Components: {result}")

    # Test word ladder
    result = word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
    print(f"Word Ladder: {result}")


if __name__ == "__main__":
    run_tests()
