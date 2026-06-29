import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import TheoryViewer from '../../components/TheoryViewer';
import CodeViewer from '../../components/CodeViewer';
import TableOfContents from '../../components/TableOfContents';
import ThemeToggle from '../../components/ThemeToggle';
import UserMenu from '../../components/UserMenu';
import ViewModeToggle from '../../components/ViewModeToggle';
import { useProgress } from '../../hooks/useProgress';
import { useAuth } from '../../contexts/AuthContext';
import { getTopics, contentBasePath } from '../../data/topicsConfig';

const TopicDetail = ({ type = 'dsa' }) => {
  const { topicId } = useParams();
  const topicIdentifier = topicId;

  const [theoryContent, setTheoryContent] = useState('');
  const [codeContent, setCodeContent] = useState('');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [activeTab, setActiveTab] = useState('theory');
  const [isMobile, setIsMobile] = useState(false);
  const [viewMode, setViewMode] = useState(() => localStorage.getItem('topicViewMode') || 'split');

  // Progress tracking
  const { isCompleted, markCompleted, markIncomplete, loading: progressLoading } = useProgress();

  // Auth
  const { isAuthenticated: isAuth } = useAuth();

  const topics = getTopics(type);
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

  // Persist view mode preference across topics and sessions
  useEffect(() => {
    localStorage.setItem('topicViewMode', viewMode);
  }, [viewMode]);

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
        const basePath = `${contentBasePath(type)}/${currentTopic.id}`;

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
          <div className="flex items-center justify-between gap-3">
            <div className="flex items-center space-x-2 sm:space-x-4 min-w-0">
              <Link
                to={type === 'python' ? '/python' : '/dsa'}
                className="flex items-center text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white shrink-0"
              >
                <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                  <path strokeLinecap="round" strokeLinejoin="round" d="M15 19l-7-7 7-7" />
                </svg>
                Back
              </Link>
              <div className="h-6 w-px bg-gray-300 dark:bg-gray-600 shrink-0" />
              <h1 className="text-xl font-bold text-gray-900 dark:text-white truncate">
                {currentTopic.title}
              </h1>
            </div>
            <div className="flex items-center gap-2 sm:gap-4 shrink-0">
              <span className="text-sm text-gray-500 dark:text-gray-400 whitespace-nowrap shrink-0">
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
                  className={`flex items-center gap-1.5 px-3 py-1.5 text-sm font-medium rounded-lg transition-colors shrink-0 ${
                    isCurrentCompleted
                      ? 'bg-green-100 dark:bg-green-900 text-green-700 dark:text-green-300 hover:bg-green-200 dark:hover:bg-green-800'
                      : 'bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-600'
                  }`}
                >
                  {isCurrentCompleted ? (
                    <>
                      <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                        <path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7" />
                      </svg>
                      <span className="hidden sm:inline">Completed</span>
                    </>
                  ) : (
                    <>
                      <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                        <path strokeLinecap="round" strokeLinejoin="round" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                      </svg>
                      <span className="hidden sm:inline">Mark Complete</span>
                    </>
                  )}
                </button>
              )}

              {/* Auth UI */}
              <UserMenu />
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
          <>
            {/* View mode toolbar — tablet/desktop only */}
            {!isMobile && (
              <div className="flex justify-end mb-4">
                <ViewModeToggle
                  value={viewMode}
                  onChange={setViewMode}
                  accent={type === 'python' ? 'emerald' : 'blue'}
                />
              </div>
            )}

            <div className={
              isMobile
                ? 'block'
                : viewMode === 'theory'
                  ? 'grid xl:grid-cols-[200px_1fr] gap-6'
                  : viewMode === 'code'
                    ? 'grid grid-cols-1 gap-6'
                    : 'grid grid-cols-2 xl:grid-cols-[200px_1fr_1fr] gap-6'
            }>
              {/* Table of Contents — desktop XL only; hidden in code-only mode */}
              {!isMobile && viewMode !== 'code' && (
                <div className="hidden xl:block">
                  <TableOfContents
                    containerId="theory-content"
                    contentKey={currentTopic.id}
                    accent={type === 'python' ? 'emerald' : 'blue'}
                  />
                </div>
              )}

              {/* Theory Panel */}
              <div
                id="theory-content"
                className={`min-w-0 ${
                  (isMobile && activeTab !== 'theory') || (!isMobile && viewMode === 'code')
                    ? 'hidden'
                    : ''
                }`}
              >
                <TheoryViewer content={theoryContent} />
              </div>

              {/* Code Panel */}
              <div
                className={`min-w-0 ${
                  (isMobile && activeTab !== 'code') || (!isMobile && viewMode === 'theory')
                    ? 'hidden'
                    : ''
                }`}
              >
                <CodeViewer code={codeContent} />
              </div>
            </div>
          </>
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
