import React from 'react';
import { Link } from 'react-router-dom';
import ThemeToggle from '../../components/ThemeToggle';
import { useAuth } from '../../contexts/AuthContext';
import { useProgress } from '../../hooks/useProgress';

// Total number of topics
const PYTHON_TOPICS_COUNT = 26;
const DSA_TOPICS_COUNT = 20;

/**
 * Home - Landing page for the DSA Learning App
 * Features:
 * - Welcome message
 * - Two large cards for "Python Fundamentals" and "Data Structures & Algorithms"
 * - Progress tracking (requires login)
 * - Auth UI (login/logout)
 */
const Home = () => {
  const { user, logout, isAuthenticated } = useAuth();
  const { getProgress, pythonCount, dsaCount, resetProgress, loading } = useProgress();

  const pythonProgress = getProgress('python', PYTHON_TOPICS_COUNT);
  const dsaProgress = getProgress('dsa', DSA_TOPICS_COUNT);

  const handleLogout = async () => {
    try {
      await logout();
    } catch (error) {
      console.error('Logout error:', error);
    }
  };

  const topics = [
    {
      id: 'python',
      title: 'Python Fundamentals',
      description: 'Master Python basics, data types, control flow, functions, and essential patterns for competitive programming.',
      icon: (
        <svg xmlns="http://www.w3.org/2000/svg" className="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
          <path strokeLinecap="round" strokeLinejoin="round" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4" />
        </svg>
      ),
      color: 'emerald',
      topics: ['Syntax & Data Types', 'Control Flow', 'Functions', 'Comprehensions', 'OOP Basics', 'Problem Solving'],
      pathPrefix: 'python'
    },
    {
      id: 'dsa',
      title: 'Data Structures & Algorithms',
      description: 'Learn essential data structures and algorithms to ace technical interviews at top tech companies.',
      icon: (
        <svg xmlns="http://www.w3.org/2000/svg" className="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
          <path strokeLinecap="round" strokeLinejoin="round" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z" />
        </svg>
      ),
      color: 'primary',
      topics: ['Arrays & Strings', 'Two Pointers', 'Linked Lists', 'Stacks & Queues', 'Trees & Graphs', 'Dynamic Programming'],
      pathPrefix: 'dsa'
    }
  ];

  const colorClasses = {
    emerald: {
      bg: 'bg-emerald-50 dark:bg-emerald-950',
      border: 'border-emerald-200 dark:border-emerald-800',
      text: 'text-emerald-700 dark:text-emerald-400',
      hover: 'hover:border-emerald-400 dark:hover:border-emerald-600',
      icon: 'bg-emerald-100 dark:bg-emerald-900 text-emerald-600 dark:text-emerald-400',
      progress: 'bg-emerald-500'
    },
    primary: {
      bg: 'bg-blue-50 dark:bg-blue-950',
      border: 'border-blue-200 dark:border-blue-800',
      text: 'text-blue-700 dark:text-blue-400',
      hover: 'hover:border-blue-400 dark:hover:border-blue-600',
      icon: 'bg-blue-100 dark:bg-blue-900 text-blue-600 dark:text-blue-400',
      progress: 'bg-blue-500'
    }
  };

  return (
    <div className="min-h-screen bg-primary p-6 md:p-12">
      {/* Header with Theme Toggle and Auth */}
      <div className="max-w-6xl mx-auto mb-8 flex justify-end items-center gap-4">
        {isAuthenticated ? (
          <div className="flex items-center gap-4">
            <span className="text-sm text-gray-600 dark:text-gray-400 hidden sm:block">
              {user?.email}
            </span>
            <button
              onClick={handleLogout}
              className="px-4 py-2 text-sm font-medium text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white bg-gray-100 dark:bg-gray-700 hover:bg-gray-200 dark:hover:bg-gray-600 rounded-lg transition-colors"
            >
              Logout
            </button>
          </div>
        ) : (
          <div className="flex items-center gap-2">
            <Link
              to="/login"
              className="px-4 py-2 text-sm font-medium text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white"
            >
              Login
            </Link>
            <Link
              to="/register"
              className="px-4 py-2 text-sm font-medium text-white bg-blue-600 hover:bg-blue-700 rounded-lg transition-colors"
            >
              Sign Up
            </Link>
          </div>
        )}
        <ThemeToggle />
      </div>

      <div className="max-w-6xl mx-auto">
        {/* Welcome Section */}
        <div className="text-center mb-12">
          <h1 className="text-4xl md:text-5xl font-bold text-primary mb-4">
            Welcome to DSA Learning
          </h1>
          <p className="text-lg text-secondary max-w-2xl mx-auto">
            Master Python fundamentals and Data Structures & Algorithms with interactive
            lessons, code examples, and hands-on practice.
          </p>
        </div>

        {/* Progress Section - Only show when logged in */}
        {isAuthenticated && !loading ? (
          <div className="mb-10 p-6 rounded-xl bg-card border border-default">
            <div className="flex items-center justify-between mb-4">
              <h3 className="text-lg font-semibold text-primary">Your Progress</h3>
              {(pythonCount > 0 || dsaCount > 0) && (
                <button
                  onClick={() => {
                    if (window.confirm('Are you sure you want to reset all progress?')) {
                      resetProgress();
                    }
                  }}
                  className="text-xs text-gray-500 hover:text-red-500 dark:text-gray-400 dark:hover:text-red-400"
                >
                  Reset Progress
                </button>
              )}
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div>
                <div className="flex justify-between mb-2">
                  <span className="text-sm font-medium text-secondary">Python Fundamentals</span>
                  <span className="text-sm font-medium text-emerald-600 dark:text-emerald-400">
                    {pythonCount}/{PYTHON_TOPICS_COUNT} ({pythonProgress}%)
                  </span>
                </div>
                <div className="w-full h-2 bg-tertiary rounded-full overflow-hidden">
                  <div
                    className="h-full bg-emerald-500 rounded-full transition-all duration-500"
                    style={{ width: `${pythonProgress}%` }}
                  />
                </div>
              </div>
              <div>
                <div className="flex justify-between mb-2">
                  <span className="text-sm font-medium text-secondary">Data Structures & Algorithms</span>
                  <span className="text-sm font-medium text-blue-600 dark:text-blue-400">
                    {dsaCount}/{DSA_TOPICS_COUNT} ({dsaProgress}%)
                  </span>
                </div>
                <div className="w-full h-2 bg-tertiary rounded-full overflow-hidden">
                  <div
                    className="h-full bg-blue-500 rounded-full transition-all duration-500"
                    style={{ width: `${dsaProgress}%` }}
                  />
                </div>
              </div>
            </div>
          </div>
        ) : !isAuthenticated ? (
          /* Login prompt when not authenticated */
          <div className="mb-10 p-6 rounded-xl bg-card border border-default text-center">
            <div className="flex items-center justify-center gap-2 mb-2">
              <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                <path strokeLinecap="round" strokeLinejoin="round" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
              </svg>
              <span className="text-gray-600 dark:text-gray-400">Login to track your progress</span>
            </div>
            <p className="text-sm text-gray-500 dark:text-gray-500">
              Create an account to save your learning progress and access it from any device.
            </p>
          </div>
        ) : null}

        {/* Topic Cards */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          {topics.map((topic) => {
            const colors = colorClasses[topic.color];
            return (
              <Link
                key={topic.id}
                to={`/${topic.pathPrefix}`}
                className={`block p-8 rounded-2xl border-2 ${colors.bg} ${colors.border} ${colors.hover}
                  transition-all duration-300 hover:shadow-xl hover:scale-[1.02] group`}
              >
                {/* Card Header */}
                <div className="flex items-start justify-between mb-6">
                  <div className={`p-4 rounded-xl ${colors.icon} group-hover:scale-110 transition-transform`}>
                    {topic.icon}
                  </div>
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    className={`h-6 w-6 ${colors.text} group-hover:translate-x-1 transition-transform`}
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                    strokeWidth={2}
                  >
                    <path strokeLinecap="round" strokeLinejoin="round" d="M9 5l7 7-7 7" />
                  </svg>
                </div>

                {/* Card Content */}
                <h2 className={`text-2xl font-bold ${colors.text} mb-3`}>
                  {topic.title}
                </h2>
                <p className="text-secondary mb-6 leading-relaxed">
                  {topic.description}
                </p>

                {/* Topics List */}
                <div className="flex flex-wrap gap-2 mb-4">
                  {topic.topics.map((item, index) => (
                    <span
                      key={index}
                      className="px-3 py-1 text-xs font-medium rounded-full bg-tertiary text-secondary"
                    >
                      {item}
                    </span>
                  ))}
                </div>

                {/* Start Button */}
                <div className={`mt-4 pt-4 border-t border-default flex items-center justify-between`}>
                  <span className={`text-sm font-semibold ${colors.text}`}>
                    Start Learning
                  </span>
                  <span className={`text-sm ${colors.text}`}>
                    {topic.id === 'python' ? '26 Topics' : '20 Topics'}
                  </span>
                </div>
              </Link>
            );
          })}
        </div>

        {/* Features Section */}
        <div className="mt-16 grid grid-cols-1 md:grid-cols-3 gap-6">
          {[
            {
              icon: (
                <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                  <path strokeLinecap="round" strokeLinejoin="round" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
                </svg>
              ),
              title: 'Theory',
              description: 'Clear explanations of concepts with examples'
            },
            {
              icon: (
                <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                  <path strokeLinecap="round" strokeLinejoin="round" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4" />
                </svg>
              ),
              title: 'Code',
              description: 'Working Python implementations'
            },
            {
              icon: (
                <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                  <path strokeLinecap="round" strokeLinejoin="round" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                </svg>
              ),
              title: 'Track Progress',
              description: 'Save your learning progress'
            }
          ].map((feature, index) => (
            <div
              key={index}
              className="p-6 rounded-xl bg-card border border-default text-center"
            >
              <div className="inline-flex p-3 rounded-xl bg-primary-100 dark:bg-primary-900 text-primary-600 dark:text-primary-400 mb-4">
                {feature.icon}
              </div>
              <h3 className="text-lg font-semibold text-primary mb-2">{feature.title}</h3>
              <p className="text-sm text-secondary">{feature.description}</p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default Home;
