import React, { useEffect } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';

/**
 * TheoryViewer - A component to display markdown theory content
 * Features:
 * - Uses react-markdown to render .md files
 * - Light background styling with book icon
 * - Proper markdown styling similar to VS Code
 * - Table of contents with smooth scrolling
 * - Responsive design
 */
/**
 * Helper function to generate consistent IDs from heading text
 * This ensures TOC links match the heading IDs
 */
const generateId = (children) => {
  // Convert to string if it's a React node
  const text = String(children);
  // Remove special characters, replace spaces with hyphens, lowercase
  return text.toLowerCase().replace(/\s+/g, '-').replace(/[^a-z0-9\-]/g, '');
};

const TheoryViewer = ({ content, title }) => {

  // Handle URL hash on initial load
  useEffect(() => {
    const hash = window.location.hash;
    if (hash) {
      const targetId = hash.substring(1);
      // Small delay to ensure content is rendered
      setTimeout(() => {
        const element = document.getElementById(targetId);
        if (element) {
          element.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      }, 100);
    }
  }, []);

  // Handle TOC link clicks for smooth scrolling
  const handleTocClick = (e, targetId) => {
    e.preventDefault();
    console.log('Attempting to scroll to:', targetId);
    const element = document.getElementById(targetId);
    if (element) {
      console.log('Found element, scrolling...');
      element.scrollIntoView({ behavior: 'smooth', block: 'start' });
    } else {
      console.log('Element not found:', targetId);
      // Try with different ID formats
      const variations = [
        targetId,
        targetId.replace(/-/g, ''),
        targetId.replace(/-/g, ' '),
      ];
      for (const variation of variations) {
        const el = document.getElementById(variation);
        if (el) {
          console.log('Found with variation:', variation);
          el.scrollIntoView({ behavior: 'smooth', block: 'start' });
          return;
        }
      }
    }
  };

  return (
    <div className="theory-viewer h-full overflow-auto">
      {/* Header with book icon */}
      <div className="flex items-center gap-3 mb-6 pb-4 border-b border-gray-200 dark:border-gray-700">
        <div className="flex-shrink-0 w-10 h-10 rounded-lg bg-blue-100 dark:bg-blue-900 flex items-center justify-center">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            className="h-5 w-5 text-blue-600 dark:text-blue-400"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
            strokeWidth={2}
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"
            />
          </svg>
        </div>
        <div>
          <h2 className="text-xl font-semibold text-gray-900 dark:text-white">{title || 'Theory'}</h2>
          <p className="text-sm text-gray-500 dark:text-gray-400">Conceptual explanation and concepts</p>
        </div>
      </div>

      {/* Markdown content with proper styling */}
      <div className="bg-white dark:bg-gray-800 rounded-xl p-6 border border-gray-200 dark:border-gray-700">
        <ReactMarkdown
          remarkPlugins={[remarkGfm]}
          components={{
            // Headings with IDs for TOC linking - using consistent ID generation
            h1: ({ children, ...props }) => {
              const id = generateId(children);
              return (
                <h1
                  id={id}
                  className="text-2xl font-bold text-gray-900 dark:text-white border-b border-gray-300 dark:border-gray-600 pb-2 mb-4 mt-6"
                >
                  {children}
                </h1>
              );
            },
            h2: ({ children, ...props }) => {
              const id = generateId(children);
              return (
                <h2
                  id={id}
                  className="text-xl font-semibold text-gray-800 dark:text-gray-100 mt-6 mb-3"
                >
                  {children}
                </h2>
              );
            },
            h3: ({ children, ...props }) => {
              const id = generateId(children);
              return (
                <h3
                  id={id}
                  className="text-lg font-medium text-gray-700 dark:text-gray-200 mt-4 mb-2"
                >
                  {children}
                </h3>
              );
            },
            h4: ({ children, ...props }) => {
              const id = generateId(children);
              return (
                <h4
                  id={id}
                  className="text-base font-medium text-gray-700 dark:text-gray-200 mt-3 mb-2"
                >
                  {children}
                </h4>
              );
            },
            // Paragraphs
            p: ({ children }) => (
              <p className="text-gray-600 dark:text-gray-300 leading-relaxed mb-4">
                {children}
              </p>
            ),
            // Links - scroll to section within page
            a: ({ href, children, ...props }) => {
              // Check if it's an internal anchor link
              if (href && href.startsWith('#') && href.length > 1) {
                // TOC link - smooth scroll
                const targetId = href.substring(1);
                return (
                  <a
                    href={href}
                    onClick={(e) => handleTocClick(e, targetId)}
                    className="text-blue-600 dark:text-blue-400 hover:underline cursor-pointer"
                  >
                    {children}
                  </a>
                );
              }

              // External links - open in new tab
              return (
                <a
                  href={href}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-blue-600 dark:text-blue-400 hover:underline"
                >
                  {children}
                </a>
              );
            },
            // Unordered lists
            ul: ({ children }) => (
              <ul className="list-disc pl-6 text-gray-600 dark:text-gray-300 mb-4 space-y-1">
                {children}
              </ul>
            ),
            // Ordered lists
            ol: ({ children }) => (
              <ol className="list-decimal pl-6 text-gray-600 dark:text-gray-300 mb-4 space-y-1">
                {children}
              </ol>
            ),
            // List items
            li: ({ children }) => (
              <li className="text-gray-600 dark:text-gray-300 mb-1">
                {children}
              </li>
            ),
            // Inline code
            code: ({ inline, className, children }) => {
              if (inline) {
                return (
                  <code className="bg-gray-100 dark:bg-gray-700 px-1.5 py-0.5 rounded text-sm font-mono text-pink-600 dark:text-pink-400">
                    {children}
                  </code>
                );
              }
              return (
                <code className={className}>
                  {children}
                </code>
              );
            },
            // Code blocks
            pre: ({ children }) => (
              <pre className="bg-[#1e1e1e] text-gray-300 p-4 rounded-lg overflow-x-auto mb-4 text-sm font-mono">
                {children}
              </pre>
            ),
            // Blockquotes
            blockquote: ({ children }) => (
              <blockquote className="border-l-4 border-blue-500 pl-4 italic text-gray-600 dark:text-gray-400 my-4">
                {children}
              </blockquote>
            ),
            // Tables
            table: ({ children }) => (
              <div className="overflow-x-auto mb-4">
                <table className="w-full border-collapse border border-gray-300 dark:border-gray-600">
                  {children}
                </table>
              </div>
            ),
            thead: ({ children }) => (
              <thead className="bg-gray-100 dark:bg-gray-700">
                {children}
              </thead>
            ),
            th: ({ children }) => (
              <th className="border border-gray-300 dark:border-gray-600 px-4 py-2 text-left text-gray-700 dark:text-gray-200 font-semibold">
                {children}
              </th>
            ),
            td: ({ children }) => (
              <td className="border border-gray-300 dark:border-gray-600 px-4 py-2 text-gray-600 dark:text-gray-300">
                {children}
              </td>
            ),
            // Horizontal rule
            hr: () => <hr className="border-gray-300 dark:border-gray-600 my-6" />,
            // Strong and emphasis
            strong: ({ children }) => (
              <strong className="font-semibold text-gray-900 dark:text-white">
                {children}
              </strong>
            ),
            em: ({ children }) => (
              <em className="italic text-gray-700 dark:text-gray-300">
                {children}
              </em>
            ),
          }}
        >
          {content}
        </ReactMarkdown>
      </div>
    </div>
  );
};

export default TheoryViewer;
