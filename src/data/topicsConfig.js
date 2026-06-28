// Single source of truth for all learning topics.
//
// Every topic carries everything the app needs:
//   - id:       folder name, also the route param and progress-tracking key
//   - title:    display name
//   - mdFile:   theory markdown file inside the topic folder
//   - pyFile:   Python implementation file inside the topic folder
//   - category: grouping used by the list pages
//
// Content is served from /content/<base>/<id>/<file>. See contentBasePath().
// When adding/renaming a topic, edit ONLY this file and add the matching files
// under the corresponding source folder at the repo root.

export const pythonTopics = [
  { id: '01_syntax_datatypes', title: 'Syntax & Data Types', mdFile: 'syntax_datatypes.md', pyFile: 'syntax_datatypes.py', category: 'Fundamentals' },
  { id: '02_operators', title: 'Operators', mdFile: 'operators.md', pyFile: 'operators.py', category: 'Fundamentals' },
  { id: '03_control_flow', title: 'Control Flow', mdFile: 'control_flow.md', pyFile: 'control_flow.py', category: 'Fundamentals' },
  { id: '04_lists', title: 'Lists', mdFile: 'lists.md', pyFile: 'lists.py', category: 'Data Structures' },
  { id: '05_dictionaries', title: 'Dictionaries', mdFile: 'dictionaries.md', pyFile: 'dictionaries.py', category: 'Data Structures' },
  { id: '06_sets', title: 'Sets', mdFile: 'sets.md', pyFile: 'sets.py', category: 'Data Structures' },
  { id: '07_tuples', title: 'Tuples', mdFile: 'tuples.md', pyFile: 'tuples.py', category: 'Data Structures' },
  { id: '08_comprehensions', title: 'Comprehensions', mdFile: 'comprehensions.md', pyFile: 'comprehensions.py', category: 'Advanced Features' },
  { id: '09_builtin_functions', title: 'Builtin Functions', mdFile: 'builtin_functions.md', pyFile: 'builtin_functions.py', category: 'Advanced Features' },
  { id: '10_functions', title: 'Functions', mdFile: 'functions.md', pyFile: 'functions.py', category: 'Advanced Features' },
  { id: '11_two_pointers', title: 'Two Pointers', mdFile: 'two_pointers.md', pyFile: 'two_pointers.py', category: 'Patterns' },
  { id: '12_sliding_window', title: 'Sliding Window', mdFile: 'sliding_window.md', pyFile: 'sliding_window.py', category: 'Patterns' },
  { id: '13_prefix_sums', title: 'Prefix Sums', mdFile: 'prefix_sums.md', pyFile: 'prefix_sums.py', category: 'Patterns' },
  { id: '14_hashing_patterns', title: 'Hashing Patterns', mdFile: 'hashing_patterns.md', pyFile: 'hashing_patterns.py', category: 'Patterns' },
  { id: '15_bfs_dfs', title: 'BFS & DFS', mdFile: 'bfs_dfs.md', pyFile: 'bfs_dfs.py', category: 'Patterns' },
  { id: '16_binary_search', title: 'Binary Search', mdFile: 'binary_search.md', pyFile: 'binary_search.py', category: 'Patterns' },
  { id: '17_union_find', title: 'Union Find', mdFile: 'union_find.md', pyFile: 'union_find.py', category: 'Patterns' },
  { id: '18_heaps', title: 'Heaps', mdFile: 'heaps.md', pyFile: 'heaps.py', category: 'Patterns' },
  { id: '19_oop_basics', title: 'OOP Basics', mdFile: 'oop_basics.md', pyFile: 'oop_basics.py', category: 'Additional' },
  { id: '20_io_performance', title: 'I/O Performance', mdFile: 'io_performance.md', pyFile: 'io_performance.py', category: 'Additional' },
  { id: '21_complexity', title: 'Complexity', mdFile: 'complexity.md', pyFile: 'complexity.py', category: 'Additional' },
  { id: '22_python_idioms', title: 'Python Idioms', mdFile: 'python_idioms.md', pyFile: 'python_idioms.py', category: 'Additional' },
  { id: '23_itertools', title: 'Itertools', mdFile: 'itertools.md', pyFile: 'itertools.py', category: 'Additional' },
  { id: '24_common_pitfalls', title: 'Common Pitfalls', mdFile: 'common_pitfalls.md', pyFile: 'common_pitfalls.py', category: 'Additional' },
  { id: '25_problem_solving', title: 'Problem Solving', mdFile: 'problem_solving.md', pyFile: 'problem_solving.py', category: 'Additional' },
  { id: '26_leetcode_patterns', title: 'LeetCode Patterns', mdFile: 'leetcode_patterns.md', pyFile: 'leetcode_patterns.py', category: 'Additional' },
];

export const dsaTopics = [
  { id: '01_arrays_strings', title: 'Arrays & Strings', mdFile: 'arrays_strings.md', pyFile: 'arrays_strings.py', category: 'Fundamentals' },
  { id: '02_two_pointers_sliding_window', title: 'Two Pointers & Sliding Window', mdFile: 'two_pointers_sliding_window.md', pyFile: 'two_pointers_sliding_window.py', category: 'Fundamentals' },
  { id: '03_linked_lists', title: 'Linked Lists', mdFile: 'linked_lists.md', pyFile: 'linked_lists.py', category: 'Data Structures' },
  { id: '04_stacks', title: 'Stacks', mdFile: 'stacks.md', pyFile: 'stacks.py', category: 'Data Structures' },
  { id: '05_queues', title: 'Queues', mdFile: 'queues.md', pyFile: 'queues.py', category: 'Data Structures' },
  { id: '06_hash_tables', title: 'Hash Tables', mdFile: 'hash_tables.md', pyFile: 'hash_tables.py', category: 'Data Structures' },
  { id: '07_sets', title: 'Sets', mdFile: 'sets.md', pyFile: 'sets.py', category: 'Data Structures' },
  { id: '08_sorting', title: 'Sorting', mdFile: 'sorting.md', pyFile: 'sorting.py', category: 'Algorithms' },
  { id: '09_searching', title: 'Searching', mdFile: 'searching.md', pyFile: 'searching.py', category: 'Algorithms' },
  { id: '10_recursion', title: 'Recursion', mdFile: 'recursion.md', pyFile: 'recursion.py', category: 'Algorithms' },
  { id: '11_binary_trees', title: 'Binary Trees', mdFile: 'binary_trees.md', pyFile: 'binary_trees.py', category: 'Data Structures' },
  { id: '12_bst', title: 'Binary Search Trees', mdFile: 'bst.md', pyFile: 'bst.py', category: 'Data Structures' },
  { id: '13_tries', title: 'Tries', mdFile: 'tries.md', pyFile: 'tries.py', category: 'Data Structures' },
  { id: '14_graphs', title: 'Graphs', mdFile: 'graphs_intro.md', pyFile: 'graphs.py', category: 'Data Structures' },
  { id: '15_heaps', title: 'Heaps', mdFile: 'heaps.md', pyFile: 'heaps.py', category: 'Data Structures' },
  { id: '16_union_find', title: 'Union Find', mdFile: 'union_find.md', pyFile: 'union_find.py', category: 'Data Structures' },
  { id: '17_dp', title: 'Dynamic Programming', mdFile: 'dp.md', pyFile: 'algorithms_comprehensive.py', category: 'Advanced' },
  { id: '18_greedy', title: 'Greedy', mdFile: 'greedy.md', pyFile: 'greedy.py', category: 'Algorithms' },
  { id: '19_bit_manipulation', title: 'Bit Manipulation', mdFile: 'bit_manipulation.md', pyFile: 'bit_manipulation.py', category: 'Algorithms' },
  { id: '20_patterns', title: 'Patterns', mdFile: 'patterns_summary.md', pyFile: 'patterns.py', category: 'Patterns' },
];

// Ordered category lists used by the list pages.
export const pythonCategories = ['Fundamentals', 'Data Structures', 'Advanced Features', 'Patterns', 'Additional'];
export const dsaCategories = ['Fundamentals', 'Data Structures', 'Algorithms', 'Patterns', 'Advanced'];

export const PYTHON_TOPICS_COUNT = pythonTopics.length;
export const DSA_TOPICS_COUNT = dsaTopics.length;

/** Topic list for a track ('python' | 'dsa'). */
export function getTopics(type) {
  return type === 'python' ? pythonTopics : dsaTopics;
}

/** Public base path where a track's content is served from. */
export function contentBasePath(type) {
  return type === 'python' ? '/content/00_python_fundamentals' : '/content';
}
