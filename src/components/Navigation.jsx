import { useState } from 'react'

// Python Fundamentals topics (26 topics)
const pythonTopics = [
  { id: 'py-1', title: 'Variables and Data Types' },
  { id: 'py-2', title: 'Operators' },
  { id: 'py-3', title: 'Control Flow - If/Else' },
  { id: 'py-4', title: 'Loops - For and While' },
  { id: 'py-5', title: 'Functions' },
  { id: 'py-6', title: 'Scope and Namespaces' },
  { id: 'py-7', title: 'Lists' },
  { id: 'py-8', title: 'Tuples' },
  { id: 'py-9', title: 'Dictionaries' },
  { id: 'py-10', title: 'Sets' },
  { id: 'py-11', title: 'Strings' },
  { id: 'py-12', title: 'String Formatting' },
  { id: 'py-13', title: 'File I/O' },
  { id: 'py-14', title: 'Exception Handling' },
  { id: 'py-15', title: 'List Comprehensions' },
  { id: 'py-16', title: 'Lambda Functions' },
  { id: 'py-17', title: 'Map, Filter, Reduce' },
  { id: 'py-18', title: 'Modules and Imports' },
  { id: 'py-19', title: 'Classes and Objects' },
  { id: 'py-20', title: 'Inheritance' },
  { id: 'py-21', title: 'Polymorphism' },
  { id: 'py-22', title: 'Encapsulation' },
  { id: 'py-23', title: 'Decorators' },
  { id: 'py-24', title: 'Generators' },
  { id: 'py-25', title: 'Iterators' },
  { id: 'py-26', title: 'Working with JSON' },
]

// DSA topics (20 topics)
const dsaTopics = [
  { id: 'dsa-1', title: 'Arrays' },
  { id: 'dsa-2', title: 'Strings' },
  { id: 'dsa-3', title: 'Two Pointers' },
  { id: 'dsa-4', title: 'Sliding Window' },
  { id: 'dsa-5', title: 'Linked Lists' },
  { id: 'dsa-6', title: 'Stacks' },
  { id: 'dsa-7', title: 'Queues' },
  { id: 'dsa-8', title: 'Hash Tables' },
  { id: 'dsa-9', title: 'Sets' },
  { id: 'dsa-10', title: 'Sorting Algorithms' },
  { id: 'dsa-11', title: 'Searching Algorithms' },
  { id: 'dsa-12', title: 'Recursion' },
  { id: 'dsa-13', title: 'Binary Trees' },
  { id: 'dsa-14', title: 'Binary Search Trees' },
  { id: 'dsa-15', title: 'Tries' },
  { id: 'dsa-16', title: 'Graphs' },
  { id: 'dsa-17', title: 'Heaps' },
  { id: 'dsa-18', title: 'Union Find' },
  { id: 'dsa-19', title: 'Dynamic Programming' },
  { id: 'dsa-20', title: 'Bit Manipulation' },
]

// Chevron icon for accordion
const ChevronIcon = ({ isOpen }) => (
  <svg
    xmlns="http://www.w3.org/2000/svg"
    fill="none"
    viewBox="0 0 24 24"
    strokeWidth={2}
    stroke="currentColor"
    className={`w-4 h-4 transition-transform duration-200 ${isOpen ? 'rotate-180' : ''}`}
  >
    <path strokeLinecap="round" strokeLinejoin="round" d="m19.5 8.25-7.5 7.5-7.5-7.5" />
  </svg>
)

// Menu icon
const MenuIcon = () => (
  <svg
    xmlns="http://www.w3.org/2000/svg"
    fill="none"
    viewBox="0 0 24 24"
    strokeWidth={1.5}
    stroke="currentColor"
    className="w-6 h-6"
  >
    <path strokeLinecap="round" strokeLinejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" />
  </svg>
)

// Close icon
const CloseIcon = () => (
  <svg
    xmlns="http://www.w3.org/2000/svg"
    fill="none"
    viewBox="0 0 24 24"
    strokeWidth={1.5}
    stroke="currentColor"
    className="w-6 h-6"
  >
    <path strokeLinecap="round" strokeLinejoin="round" d="M6 18 18 6M6 6l12 12" />
  </svg>
)

export default function Navigation({ currentTopic, onTopicSelect }) {
  const [isOpen, setIsOpen] = useState({
    python: true,
    dsa: true,
  })
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false)

  const toggleSection = (section) => {
    setIsOpen((prev) => ({
      ...prev,
      [section]: !prev[section],
    }))
  }

  const handleTopicClick = (topicId) => {
    onTopicSelect(topicId)
    // Close mobile menu when a topic is selected
    setIsMobileMenuOpen(false)
  }

  const renderTopicList = (topics, category) => (
    <ul className="space-y-1">
      {topics.map((topic, index) => (
        <li key={topic.id}>
          <button
            onClick={() => handleTopicClick(topic.id)}
            className={`w-full text-left px-3 py-2 rounded-lg text-sm transition-colors duration-150 flex items-center gap-2 ${
              currentTopic === topic.id
                ? 'bg-blue-600 text-white'
                : 'text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700'
            }`}
          >
            <span className="text-xs font-mono text-gray-500 dark:text-gray-400 w-6">
              {index + 1}.
            </span>
            <span>{topic.title}</span>
          </button>
        </li>
      ))}
    </ul>
  )

  const sidebarContent = (
    <nav className="p-4 space-y-4">
      {/* Python Fundamentals Section */}
      <div>
        <button
          onClick={() => toggleSection('python')}
          className="flex items-center justify-between w-full px-3 py-2 text-sm font-semibold text-gray-900 dark:text-gray-100 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-lg transition-colors"
        >
          <span>Python Fundamentals</span>
          <span className="text-xs bg-gray-200 dark:bg-gray-600 px-2 py-0.5 rounded-full">
            26
          </span>
          <ChevronIcon isOpen={isOpen.python} />
        </button>
        {isOpen.python && (
          <div className="mt-1 ml-2 border-l-2 border-gray-200 dark:border-gray-700 pl-2">
            {renderTopicList(pythonTopics, 'python')}
          </div>
        )}
      </div>

      {/* DSA Section */}
      <div>
        <button
          onClick={() => toggleSection('dsa')}
          className="flex items-center justify-between w-full px-3 py-2 text-sm font-semibold text-gray-900 dark:text-gray-100 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-lg transition-colors"
        >
          <span>DSA</span>
          <span className="text-xs bg-gray-200 dark:bg-gray-600 px-2 py-0.5 rounded-full">
            20
          </span>
          <ChevronIcon isOpen={isOpen.dsa} />
        </button>
        {isOpen.dsa && (
          <div className="mt-1 ml-2 border-l-2 border-gray-200 dark:border-gray-700 pl-2">
            {renderTopicList(dsaTopics, 'dsa')}
          </div>
        )}
      </div>
    </nav>
  )

  return (
    <>
      {/* Mobile hamburger button */}
      <button
        onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
        className="lg:hidden fixed top-16 left-4 z-50 p-2 rounded-lg bg-white dark:bg-gray-800 shadow-lg text-gray-700 dark:text-gray-200"
        aria-label="Toggle navigation menu"
      >
        {isMobileMenuOpen ? <CloseIcon /> : <MenuIcon />}
      </button>

      {/* Mobile overlay */}
      {isMobileMenuOpen && (
        <div
          className="lg:hidden fixed inset-0 bg-black/50 z-30"
          onClick={() => setIsMobileMenuOpen(false)}
        />
      )}

      {/* Sidebar - Desktop */}
      <aside className="hidden lg:block w-64 h-screen sticky top-0 bg-white dark:bg-gray-900 border-r border-gray-200 dark:border-gray-700 overflow-y-auto">
        {sidebarContent}
      </aside>

      {/* Sidebar - Mobile */}
      <aside
        className={`lg:hidden fixed inset-y-0 left-0 w-64 bg-white dark:bg-gray-900 border-r border-gray-200 dark:border-gray-700 z-40 transform transition-transform duration-300 ${
          isMobileMenuOpen ? 'translate-x-0' : '-translate-x-full'
        }`}
      >
        {sidebarContent}
      </aside>
    </>
  )
}
