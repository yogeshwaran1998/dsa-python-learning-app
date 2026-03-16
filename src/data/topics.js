// Topic data file mapping all 46 topics (26 Python + 20 DSA)
// Paths are relative to the DSA files at /Users/yogesh/Downloads/DSA/

const DSA_BASE_PATH = '../../..';

// Python Topics (26) - from 00_python_fundamentals folder
export const pythonTopics = [
  {
    id: 'syntax-datatypes',
    title: 'Syntax & Data Types',
    folder: '01_syntax_datatypes',
    mdFile: 'syntax_datatypes.md',
    pyFile: 'syntax_datatypes.py',
    category: 'Fundamentals',
  },
  {
    id: 'operators',
    title: 'Operators',
    folder: '02_operators',
    mdFile: 'operators.md',
    pyFile: 'operators.py',
    category: 'Fundamentals',
  },
  {
    id: 'control-flow',
    title: 'Control Flow',
    folder: '03_control_flow',
    mdFile: 'control_flow.md',
    pyFile: 'control_flow.py',
    category: 'Fundamentals',
  },
  {
    id: 'lists',
    title: 'Lists',
    folder: '04_lists',
    mdFile: 'lists.md',
    pyFile: 'lists.py',
    category: 'Data Structures',
  },
  {
    id: 'dictionaries',
    title: 'Dictionaries',
    folder: '05_dictionaries',
    mdFile: 'dictionaries.md',
    pyFile: 'dictionaries.py',
    category: 'Data Structures',
  },
  {
    id: 'sets',
    title: 'Sets',
    folder: '06_sets',
    mdFile: 'sets.md',
    pyFile: 'sets.py',
    category: 'Data Structures',
  },
  {
    id: 'tuples',
    title: 'Tuples',
    folder: '07_tuples',
    mdFile: 'tuples.md',
    pyFile: 'tuples.py',
    category: 'Data Structures',
  },
  {
    id: 'comprehensions',
    title: 'Comprehensions',
    folder: '08_comprehensions',
    mdFile: 'comprehensions.md',
    pyFile: 'comprehensions.py',
    category: 'Advanced',
  },
  {
    id: 'builtin-functions',
    title: 'Builtin Functions',
    folder: '09_builtin_functions',
    mdFile: 'builtin_functions.md',
    pyFile: 'builtin_functions.py',
    category: 'Advanced',
  },
  {
    id: 'functions',
    title: 'Functions',
    folder: '10_functions',
    mdFile: 'functions.md',
    pyFile: 'functions.py',
    category: 'Advanced',
  },
  {
    id: 'two-pointers',
    title: 'Two Pointers',
    folder: '11_two_pointers',
    mdFile: 'two_pointers.md',
    pyFile: 'two_pointers.py',
    category: 'Patterns',
  },
  {
    id: 'sliding-window',
    title: 'Sliding Window',
    folder: '12_sliding_window',
    mdFile: 'sliding_window.md',
    pyFile: 'sliding_window.py',
    category: 'Patterns',
  },
  {
    id: 'prefix-sums',
    title: 'Prefix Sums',
    folder: '13_prefix_sums',
    mdFile: 'prefix_sums.md',
    pyFile: 'prefix_sums.py',
    category: 'Patterns',
  },
  {
    id: 'hashing-patterns',
    title: 'Hashing Patterns',
    folder: '14_hashing_patterns',
    mdFile: 'hashing_patterns.md',
    pyFile: 'hashing_patterns.py',
    category: 'Patterns',
  },
  {
    id: 'bfs-dfs',
    title: 'BFS & DFS',
    folder: '15_bfs_dfs',
    mdFile: 'bfs_dfs.md',
    pyFile: 'bfs_dfs.py',
    category: 'Patterns',
  },
  {
    id: 'binary-search',
    title: 'Binary Search',
    folder: '16_binary_search',
    mdFile: 'binary_search.md',
    pyFile: 'binary_search.py',
    category: 'Algorithms',
  },
  {
    id: 'union-find',
    title: 'Union Find',
    folder: '17_union_find',
    mdFile: 'union_find.md',
    pyFile: 'union_find.py',
    category: 'Algorithms',
  },
  {
    id: 'heaps',
    title: 'Heaps',
    folder: '18_heaps',
    mdFile: 'heaps.md',
    pyFile: 'heaps.py',
    category: 'Data Structures',
  },
  {
    id: 'oop-basics',
    title: 'OOP Basics',
    folder: '19_oop_basics',
    mdFile: 'oop_basics.md',
    pyFile: 'oop_basics.py',
    category: 'Advanced',
  },
  {
    id: 'io-performance',
    title: 'IO & Performance',
    folder: '20_io_performance',
    mdFile: 'io_performance.md',
    pyFile: 'io_performance.py',
    category: 'Advanced',
  },
  {
    id: 'complexity',
    title: 'Complexity Analysis',
    folder: '21_complexity',
    mdFile: 'complexity.md',
    pyFile: 'complexity.py',
    category: 'Fundamentals',
  },
  {
    id: 'python-idioms',
    title: 'Python Idioms',
    folder: '22_python_idioms',
    mdFile: 'python_idioms.md',
    pyFile: 'python_idioms.py',
    category: 'Advanced',
  },
  {
    id: 'itertools',
    title: 'Itertools',
    folder: '23_itertools',
    mdFile: 'itertools.md',
    pyFile: 'itertools.py',
    category: 'Advanced',
  },
  {
    id: 'common-pitfalls',
    title: 'Common Pitfalls',
    folder: '24_common_pitfalls',
    mdFile: 'common_pitfalls.md',
    pyFile: 'common_pitfalls.py',
    category: 'Advanced',
  },
  {
    id: 'problem-solving',
    title: 'Problem Solving',
    folder: '25_problem_solving',
    mdFile: 'problem_solving.md',
    pyFile: 'problem_solving.py',
    category: 'Advanced',
  },
  {
    id: 'leetcode-patterns',
    title: 'LeetCode Patterns',
    folder: '26_leetcode_patterns',
    mdFile: 'leetcode_patterns.md',
    pyFile: 'leetcode_patterns.py',
    category: 'Patterns',
  },
];

// DSA Topics (20) - from main DSA folder
export const dsaTopics = [
  {
    id: 'arrays-strings',
    title: 'Arrays & Strings',
    folder: '01_arrays_strings',
    mdFile: 'arrays_strings.md',
    pyFile: 'arrays_strings.py',
    category: 'Fundamentals',
  },
  {
    id: 'two-pointers-sliding-window',
    title: 'Two Pointers & Sliding Window',
    folder: '02_two_pointers_sliding_window',
    mdFile: 'two_pointers_sliding_window.md',
    pyFile: 'two_pointers_sliding_window.py',
    category: 'Patterns',
  },
  {
    id: 'linked-lists',
    title: 'Linked Lists',
    folder: '03_linked_lists',
    mdFile: 'linked_lists.md',
    pyFile: 'linked_lists.py',
    category: 'Data Structures',
  },
  {
    id: 'stacks',
    title: 'Stacks',
    folder: '04_stacks',
    mdFile: 'stacks.md',
    pyFile: 'stacks.py',
    category: 'Data Structures',
  },
  {
    id: 'queues',
    title: 'Queues',
    folder: '05_queues',
    mdFile: 'queues.md',
    pyFile: 'queues.py',
    category: 'Data Structures',
  },
  {
    id: 'hash-tables',
    title: 'Hash Tables',
    folder: '06_hash_tables',
    mdFile: 'hash_tables.md',
    pyFile: 'hash_tables.py',
    category: 'Data Structures',
  },
  {
    id: 'sets',
    title: 'Sets',
    folder: '07_sets',
    mdFile: 'sets.md',
    pyFile: 'sets.py',
    category: 'Data Structures',
  },
  {
    id: 'sorting',
    title: 'Sorting',
    folder: '08_sorting',
    mdFile: 'sorting.md',
    pyFile: 'sorting.py',
    category: 'Algorithms',
  },
  {
    id: 'searching',
    title: 'Searching',
    folder: '09_searching',
    mdFile: 'searching.md',
    pyFile: 'searching.py',
    category: 'Algorithms',
  },
  {
    id: 'recursion',
    title: 'Recursion',
    folder: '10_recursion',
    mdFile: 'recursion.md',
    pyFile: 'recursion.py',
    category: 'Algorithms',
  },
  {
    id: 'binary-trees',
    title: 'Binary Trees',
    folder: '11_binary_trees',
    mdFile: 'binary_trees.md',
    pyFile: 'binary_trees.py',
    category: 'Data Structures',
  },
  {
    id: 'bst',
    title: 'Binary Search Trees',
    folder: '12_bst',
    mdFile: 'bst.md',
    pyFile: 'bst.py',
    category: 'Data Structures',
  },
  {
    id: 'tries',
    title: 'Tries',
    folder: '13_tries',
    mdFile: 'tries.md',
    pyFile: 'tries.py',
    category: 'Data Structures',
  },
  {
    id: 'graphs',
    title: 'Graphs',
    folder: '14_graphs',
    mdFile: 'graphs_intro.md',
    pyFile: 'graphs.py',
    category: 'Data Structures',
  },
  {
    id: 'heaps',
    title: 'Heaps',
    folder: '15_heaps',
    mdFile: 'heaps.md',
    pyFile: 'heaps.py',
    category: 'Data Structures',
  },
  {
    id: 'union-find',
    title: 'Union Find',
    folder: '16_union_find',
    mdFile: 'union_find.md',
    pyFile: 'union_find.py',
    category: 'Data Structures',
  },
  {
    id: 'dp',
    title: 'Dynamic Programming',
    folder: '17_dp',
    mdFile: 'dp.md',
    pyFile: 'algorithms_comprehensive.py',
    category: 'Algorithms',
  },
  {
    id: 'greedy',
    title: 'Greedy Algorithms',
    folder: '18_greedy',
    mdFile: 'greedy.md',
    pyFile: 'greedy.py',
    category: 'Algorithms',
  },
  {
    id: 'bit-manipulation',
    title: 'Bit Manipulation',
    folder: '19_bit_manipulation',
    mdFile: 'bit_manipulation.md',
    pyFile: 'bit_manipulation.py',
    category: 'Advanced',
  },
  {
    id: 'patterns',
    title: 'Problem Patterns',
    folder: '20_patterns',
    mdFile: 'patterns_summary.md',
    pyFile: 'patterns.py',
    category: 'Patterns',
  },
];

// Combined array of all topics
export const allTopics = [...pythonTopics, ...dsaTopics];

// Helper functions to get topics
export const getPythonTopicById = (id) => pythonTopics.find((t) => t.id === id);
export const getDSATopicById = (id) => dsaTopics.find((t) => t.id === id);
export const getTopicById = (id) => allTopics.find((t) => t.id === id);

// Get full paths for content loading
export const getPythonTopicPath = (topic) => ({
  md: `${DSA_BASE_PATH}/00_python_fundamentals/${topic.folder}/${topic.mdFile}`,
  py: `${DSA_BASE_PATH}/00_python_fundamentals/${topic.folder}/${topic.pyFile}`,
});

export const getDSATopicPath = (topic) => ({
  md: `${DSA_BASE_PATH}/${topic.folder}/${topic.mdFile}`,
  py: `${DSA_BASE_PATH}/${topic.folder}/${topic.pyFile}`,
});

// Determine if topic is Python or DSA based on id
export const getTopicSource = (topicId) => {
  const topic = getTopicById(topicId);
  if (!topic) return null;

  const isPython = pythonTopics.some((t) => t.id === topicId);
  return {
    type: isPython ? 'python' : 'dsa',
    paths: isPython ? getPythonTopicPath(topic) : getDSATopicPath(topic),
  };
};

export default allTopics;
