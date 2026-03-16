import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import TheoryViewer from '../../components/TheoryViewer';
import CodeViewer from '../../components/CodeViewer';
import ThemeToggle from '../../components/ThemeToggle';
import { useProgress } from '../../hooks/useProgress';
import { useAuth } from '../../contexts/AuthContext';

// Python Topics - using folder names as IDs
const pythonTopics = [
  { id: '01_syntax_datatypes', title: 'Syntax & Data Types', mdFile: 'syntax_datatypes.md', pyFile: 'syntax_datatypes.py' },
  { id: '02_operators', title: 'Operators', mdFile: 'operators.md', pyFile: 'operators.py' },
  { id: '03_control_flow', title: 'Control Flow', mdFile: 'control_flow.md', pyFile: 'control_flow.py' },
  { id: '04_lists', title: 'Lists', mdFile: 'lists.md', pyFile: 'lists.py' },
  { id: '05_dictionaries', title: 'Dictionaries', mdFile: 'dictionaries.md', pyFile: 'dictionaries.py' },
  { id: '06_sets', title: 'Sets', mdFile: 'sets.md', pyFile: 'sets.py' },
  { id: '07_tuples', title: 'Tuples', mdFile: 'tuples.md', pyFile: 'tuples.py' },
  { id: '08_comprehensions', title: 'Comprehensions', mdFile: 'comprehensions.md', pyFile: 'comprehensions.py' },
  { id: '09_builtin_functions', title: 'Builtin Functions', mdFile: 'builtin_functions.md', pyFile: 'builtin_functions.py' },
  { id: '10_functions', title: 'Functions', mdFile: 'functions.md', pyFile: 'functions.py' },
  { id: '11_two_pointers', title: 'Two Pointers', mdFile: 'two_pointers.md', pyFile: 'two_pointers.py' },
  { id: '12_sliding_window', title: 'Sliding Window', mdFile: 'sliding_window.md', pyFile: 'sliding_window.py' },
  { id: '13_prefix_sums', title: 'Prefix Sums', mdFile: 'prefix_sums.md', pyFile: 'prefix_sums.py' },
  { id: '14_hashing_patterns', title: 'Hashing Patterns', mdFile: 'hashing_patterns.md', pyFile: 'hashing_patterns.py' },
  { id: '15_bfs_dfs', title: 'BFS & DFS', mdFile: 'bfs_dfs.md', pyFile: 'bfs_dfs.py' },
  { id: '16_binary_search', title: 'Binary Search', mdFile: 'binary_search.md', pyFile: 'binary_search.py' },
  { id: '17_union_find', title: 'Union Find', mdFile: 'union_find.md', pyFile: 'union_find.py' },
  { id: '18_heaps', title: 'Heaps', mdFile: 'heaps.md', pyFile: 'heaps.py' },
  { id: '19_oop_basics', title: 'OOP Basics', mdFile: 'oop_basics.md', pyFile: 'oop_basics.py' },
  { id: '20_io_performance', title: 'I/O Performance', mdFile: 'io_performance.md', pyFile: 'io_performance.py' },
  { id: '21_complexity', title: 'Complexity', mdFile: 'complexity.md', pyFile: 'complexity.py' },
  { id: '22_python_idioms', title: 'Python Idioms', mdFile: 'python_idioms.md', pyFile: 'python_idioms.py' },
  { id: '23_itertools', title: 'Itertools', mdFile: 'itertools.md', pyFile: 'itertools.py' },
  { id: '24_common_pitfalls', title: 'Common Pitfalls', mdFile: 'common_pitfalls.md', pyFile: 'common_pitfalls.py' },
  { id: '25_problem_solving', title: 'Problem Solving', mdFile: 'problem_solving.md', pyFile: 'problem_solving.py' },
  { id: '26_leetcode_patterns', title: 'LeetCode Patterns', mdFile: 'leetcode_patterns.md', pyFile: 'leetcode_patterns.py' },
];

// DSA Topics - using folder names as IDs
const dsaTopics = [
  { id: '01_arrays_strings', title: 'Arrays & Strings', mdFile: 'arrays_strings.md', pyFile: 'arrays_strings.py' },
  { id: '02_two_pointers_sliding_window', title: 'Two Pointers & Sliding Window', mdFile: 'two_pointers_sliding_window.md', pyFile: 'two_pointers_sliding_window.py' },
  { id: '03_linked_lists', title: 'Linked Lists', mdFile: 'linked_lists.md', pyFile: 'linked_lists.py' },
  { id: '04_stacks', title: 'Stacks', mdFile: 'stacks.md', pyFile: 'stacks.py' },
  { id: '05_queues', title: 'Queues', mdFile: 'queues.md', pyFile: 'queues.py' },
  { id: '06_hash_tables', title: 'Hash Tables', mdFile: 'hash_tables.md', pyFile: 'hash_tables.py' },
  { id: '07_sets', title: 'Sets', mdFile: 'sets.md', pyFile: 'sets.py' },
  { id: '08_sorting', title: 'Sorting', mdFile: 'sorting.md', pyFile: 'sorting.py' },
  { id: '09_searching', title: 'Searching', mdFile: 'searching.md', pyFile: 'searching.py' },
  { id: '10_recursion', title: 'Recursion', mdFile: 'recursion.md', pyFile: 'recursion.py' },
  { id: '11_binary_trees', title: 'Binary Trees', mdFile: 'binary_trees.md', pyFile: 'binary_trees.py' },
  { id: '12_bst', title: 'Binary Search Trees', mdFile: 'bst.md', pyFile: 'bst.py' },
  { id: '13_tries', title: 'Tries', mdFile: 'tries.md', pyFile: 'tries.py' },
  { id: '14_graphs', title: 'Graphs', mdFile: 'graphs_intro.md', pyFile: 'graphs.py' },
  { id: '15_heaps', title: 'Heaps', mdFile: 'heaps.md', pyFile: 'heaps.py' },
  { id: '16_union_find', title: 'Union Find', mdFile: 'union_find.md', pyFile: 'union_find.py' },
  { id: '17_dp', title: 'Dynamic Programming', mdFile: 'dp.md', pyFile: 'algorithms_comprehensive.py' },
  { id: '18_greedy', title: 'Greedy', mdFile: 'greedy.md', pyFile: 'greedy.py' },
  { id: '19_bit_manipulation', title: 'Bit Manipulation', mdFile: 'bit_manipulation.md', pyFile: 'bit_manipulation.py' },
  { id: '20_patterns', title: 'Patterns', mdFile: 'patterns_summary.md', pyFile: 'patterns.py' },
];

const TopicDetail = (props) => {
  const { category, id, topicId } = useParams();

  let type;
  if (props.type) {
    type = props.type;
  } else if (category === 'python' || category === 'dsa') {
    type = category;
  } else {
    type = 'dsa';
  }

  const topicIdentifier = topicId || id;

  const [theoryContent, setTheoryContent] = useState('');
  const [codeContent, setCodeContent] = useState('');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [activeTab, setActiveTab] = useState('theory');
  const [isMobile, setIsMobile] = useState(false);

  // Progress tracking
  const { isCompleted, markCompleted, markIncomplete, isAuthenticated, loading: progressLoading } = useProgress();

  // Auth
  const { user, logout, isAuthenticated: isAuth } = useAuth();

  const handleLogout = async () => {
    try {
      await logout();
    } catch (error) {
      console.error('Logout error:', error);
    }
  };

  const topics = type === 'python' ? pythonTopics : dsaTopics;
  const currentIndex = topicIdentifier ? topics.findIndex(t => t.id === topicIdentifier) : -1;
  const currentTopic = currentIndex >= 0 ? topics[currentIndex] : null;

  // This must come AFTER currentTopic is defined
  const isCurrentCompleted = currentTopic ? isCompleted(currentTopic.id, type) : false;


  const prevTopic = currentIndex > 0 ? topics[currentIndex - 1] : null;
  const nextTopic = currentIndex < topics.length - 1 ? topics[currentIndex + 1] : null;

  useEffect(() => {
    const checkMobile = () => {
      setIsMobile(window.innerWidth < 768);
    };
    checkMobile();
    window.addEventListener('resize', checkMobile);
    return () => window.removeEventListener('resize', checkMobile);
  }, []);

  useEffect(() => {
    const loadContent = async () => {
      setLoading(true);
      setError(null);

      if (!currentTopic) {
        setLoading(false);
        return;
      }

      try {
        // Build the path to the content files in public folder
        const basePath = type === 'python'
          ? `/content/00_python_fundamentals/${currentTopic.id}`
          : `/content/${currentTopic.id}`;

        const mdPath = `${basePath}/${currentTopic.mdFile}`;
        const pyPath = `${basePath}/${currentTopic.pyFile}`;

        // Fetch both files in parallel
        const [mdResponse, pyResponse] = await Promise.all([
          fetch(mdPath),
          fetch(pyPath)
        ]);

        let mdContent = '';
        let pyContent = '';

        if (mdResponse.ok) {
          mdContent = await mdResponse.text();
        }

        if (pyResponse.ok) {
          pyContent = await pyResponse.text();
        }

        if (mdContent) {
          setTheoryContent(mdContent);
        } else {
          setTheoryContent(`# ${currentTopic.title}\n\nTheory content not found.`);
        }

        if (pyContent) {
          setCodeContent(pyContent);
        } else {
          setCodeContent(`# ${currentTopic.title}\n\nCode not found.`);
        }
      } catch (err) {
        console.error('Error loading content:', err);
        setError('Failed to load content. Please try again.');
      } finally {
        setLoading(false);
      }
    };

    loadContent();
  }, [type, topicIdentifier, currentTopic]);

  // Show loading while checking for topic or loading content
  if (!topicIdentifier) {
    return (
      <div className="min-h-screen bg-gray-50 dark:bg-gray-900 flex items-center justify-center">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500"></div>
      </div>
    );
  }

  if (!currentTopic) {
    return (
      <div className="min-h-screen bg-gray-50 dark:bg-gray-900 flex items-center justify-center">
        <div className="text-center">
          <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-4">Topic not found</h2>
          <Link to="/" className="text-blue-600 dark:text-blue-400 hover:underline">
            Go back home
          </Link>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
      {/* Header */}
      <div className="bg-white dark:bg-gray-800 border-b border-gray-200 dark:border-gray-700">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-4">
              <Link
                to={type === 'python' ? '/python' : '/dsa'}
                className="flex items-center text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white"
              >
                <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                  <path strokeLinecap="round" strokeLinejoin="round" d="M15 19l-7-7 7-7" />
                </svg>
                Back
              </Link>
              <div className="h-6 w-px bg-gray-300 dark:bg-gray-600" />
              <h1 className="text-xl font-bold text-gray-900 dark:text-white">
                {currentTopic.title}
              </h1>
            </div>
            <div className="flex items-center gap-4">
              <span className="text-sm text-gray-500 dark:text-gray-400">
                {currentIndex + 1} / {topics.length}
              </span>
              {/* Mark as Complete Button - Only show when logged in */}
              {currentTopic && isAuth && (
                <button
                  onClick={async () => {
                    try {
                      if (isCurrentCompleted) {
                        await markIncomplete(currentTopic.id, type);
                      } else {
                        await markCompleted(currentTopic.id, type);
                      }
                    } catch (err) {
                      console.error('Error updating progress:', err);
                    }
                  }}
                  disabled={progressLoading}
                  className={`flex items-center gap-1.5 px-3 py-1.5 text-sm font-medium rounded-lg transition-colors ${
                    isCurrentCompleted
                      ? 'bg-green-100 dark:bg-green-900 text-green-700 dark:text-green-300 hover:bg-green-200 dark:hover:bg-green-800'
                      : 'bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-600'
                  }`}
                >
                  {isCurrentCompleted ? (
                    <>
                      <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                        <path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7" />
                      </svg>
                      Completed
                    </>
                  ) : (
                    <>
                      <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                        <path strokeLinecap="round" strokeLinejoin="round" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                      </svg>
                      Mark Complete
                    </>
                  )}
                </button>
              )}

              {/* Auth UI - Show when logged in */}
              {isAuth ? (
                <div className="flex items-center gap-3">
                  <span className="text-sm text-gray-600 dark:text-gray-400 hidden sm:block">
                    {user?.email}
                  </span>
                  <button
                    onClick={handleLogout}
                    className="px-3 py-1.5 text-sm font-medium text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white bg-gray-100 dark:bg-gray-700 hover:bg-gray-200 dark:hover:bg-gray-600 rounded-lg transition-colors"
                  >
                    Logout
                  </button>
                </div>
              ) : currentTopic ? (
                /* Login/Signup buttons when not authenticated */
                <div className="flex items-center gap-2">
                  <Link
                    to="/login"
                    className="px-3 py-1.5 text-sm font-medium text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white"
                  >
                    Login
                  </Link>
                  <Link
                    to="/register"
                    className={`px-3 py-1.5 text-sm font-medium text-white rounded-lg transition-colors ${type === 'dsa' ? 'bg-blue-600 hover:bg-blue-700' : 'bg-green-600 hover:bg-green-700'}`}
                  >
                    Sign Up
                  </Link>
                </div>
              ) : null}
              <ThemeToggle />
            </div>
          </div>
        </div>
      </div>

      {/* Mobile Tab Navigation */}
      {isMobile && (
        <div className="bg-white dark:bg-gray-800 border-b border-gray-200 dark:border-gray-700">
          <div className="flex">
            <button
              onClick={() => setActiveTab('theory')}
              className={`flex-1 py-3 text-center font-medium ${
                activeTab === 'theory'
                  ? 'text-blue-600 dark:text-blue-400 border-b-2 border-blue-600'
                  : 'text-gray-500 dark:text-gray-400'
              }`}
            >
              Theory
            </button>
            <button
              onClick={() => setActiveTab('code')}
              className={`flex-1 py-3 text-center font-medium ${
                activeTab === 'code'
                  ? 'text-blue-600 dark:text-blue-400 border-b-2 border-blue-600'
                  : 'text-gray-500 dark:text-gray-400'
              }`}
            >
              Code
            </button>
          </div>
        </div>
      )}

      {/* Content */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 mb-16">
        {loading ? (
          <div className="flex items-center justify-center h-64">
            <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500"></div>
          </div>
        ) : error ? (
          <div className="text-center text-red-500 dark:text-red-400">{error}</div>
        ) : (
          <div className={`${isMobile ? 'block' : 'grid grid-cols-2 gap-6'}`}>
            {/* Theory Panel */}
            <div className={`${isMobile && activeTab !== 'theory' ? 'hidden' : ''}`}>
              <TheoryViewer content={theoryContent} />
            </div>

            {/* Code Panel */}
            <div className={`${isMobile && activeTab !== 'code' ? 'hidden' : ''}`}>
              <CodeViewer code={codeContent} />
            </div>
          </div>
        )}
      </div>

      {/* Navigation Footer */}
      <div className="fixed bottom-0 left-0 right-0 bg-white dark:bg-gray-800 border-t border-gray-200 dark:border-gray-700 px-4 py-3">
        <div className="max-w-7xl mx-auto flex justify-between">
          {prevTopic ? (
            <Link
              to={`/${type}/${prevTopic.id}`}
              className="flex items-center text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white"
            >
              <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                <path strokeLinecap="round" strokeLinejoin="round" d="M15 19l-7-7 7-7" />
              </svg>
              {prevTopic.title}
            </Link>
          ) : <div />}

          {nextTopic ? (
            <Link
              to={`/${type}/${nextTopic.id}`}
              className="flex items-center text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white"
            >
              {nextTopic.title}
              <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 ml-1" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                <path strokeLinecap="round" strokeLinejoin="round" d="M9 5l7 7-7 7" />
              </svg>
            </Link>
          ) : <div />}
        </div>
      </div>
    </div>
  );
};

export default TopicDetail;
