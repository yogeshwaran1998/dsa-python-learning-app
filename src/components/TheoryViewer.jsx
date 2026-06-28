import { useEffect } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import rehypeRaw from 'rehype-raw';
import rehypeSlug from 'rehype-slug';
import rehypePrism from 'rehype-prism-plus';

/**
 * TheoryViewer - renders a topic's markdown theory.
 *
 * - `remark-gfm` for tables, task lists, strikethrough, autolinks.
 * - `rehype-slug` adds GitHub-style ids to headings so the in-document Table of
 *   Contents links (e.g. `#common-patterns`) resolve reliably — no hand-rolled
 *   slugger that can drift from the anchors the markdown itself generates.
 * - `rehype-prism-plus` syntax-highlights fenced code blocks (token styles come
 *   from the Prism theme imported by CodeViewer).
 * - `rehype-raw` lets the (trusted, in-repo) markdown embed curated HTML/SVG for
 *   styled diagrams, which are styled by the `.dsa-diagram*` classes in
 *   index.css. Content is authored by us, so raw HTML is safe here.
 */
const smoothScrollToId = (id) => {
  const el = document.getElementById(id);
  if (el) {
    el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    return true;
  }
  return false;
};

const TheoryViewer = ({ content, title }) => {
  // On mount, honor a hash already present in the URL.
  useEffect(() => {
    const hash = window.location.hash;
    if (hash && hash.length > 1) {
      const id = decodeURIComponent(hash.substring(1));
      const t = setTimeout(() => smoothScrollToId(id), 100);
      return () => clearTimeout(t);
    }
  }, [content]);

  const headingClasses = {
    h1: 'text-2xl font-bold text-gray-900 dark:text-white border-b border-gray-300 dark:border-gray-600 pb-2 mb-4 mt-6 scroll-mt-24',
    h2: 'text-xl font-semibold text-gray-800 dark:text-gray-100 mt-6 mb-3 scroll-mt-24',
    h3: 'text-lg font-medium text-gray-700 dark:text-gray-200 mt-4 mb-2 scroll-mt-24',
    h4: 'text-base font-medium text-gray-700 dark:text-gray-200 mt-3 mb-2 scroll-mt-24',
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
          rehypePlugins={[rehypeRaw, rehypeSlug, [rehypePrism, { ignoreMissing: true }]]}
          components={{
            // Headings keep the id rehype-slug injects (spread via ...props) so
            // TOC anchors resolve.
            h1: ({ children, ...props }) => <h1 {...props} className={headingClasses.h1}>{children}</h1>,
            h2: ({ children, ...props }) => <h2 {...props} className={headingClasses.h2}>{children}</h2>,
            h3: ({ children, ...props }) => <h3 {...props} className={headingClasses.h3}>{children}</h3>,
            h4: ({ children, ...props }) => <h4 {...props} className={headingClasses.h4}>{children}</h4>,
            p: ({ children }) => (
              <p className="text-gray-600 dark:text-gray-300 leading-relaxed mb-4">{children}</p>
            ),
            // Internal anchors smooth-scroll; external links open in a new tab.
            a: ({ href, children }) => {
              if (href && href.startsWith('#') && href.length > 1) {
                const targetId = decodeURIComponent(href.substring(1));
                return (
                  <a
                    href={href}
                    onClick={(e) => {
                      if (smoothScrollToId(targetId)) e.preventDefault();
                    }}
                    className="text-blue-600 dark:text-blue-400 hover:underline cursor-pointer"
                  >
                    {children}
                  </a>
                );
              }
              return (
                <a href={href} target="_blank" rel="noopener noreferrer" className="text-blue-600 dark:text-blue-400 hover:underline">
                  {children}
                </a>
              );
            },
            ul: ({ children }) => (
              <ul className="list-disc pl-6 text-gray-600 dark:text-gray-300 mb-4 space-y-1">{children}</ul>
            ),
            ol: ({ children }) => (
              <ol className="list-decimal pl-6 text-gray-600 dark:text-gray-300 mb-4 space-y-1">{children}</ol>
            ),
            li: ({ children }) => <li className="text-gray-600 dark:text-gray-300 mb-1">{children}</li>,
            // Inline vs. block code. Block code is either tagged (rehype-prism
            // adds a `language-*` class) OR an untagged fenced block (ASCII
            // diagrams, example I/O) — which still spans multiple lines. Only
            // genuinely inline code (no class, single line) gets pill styling;
            // everything else flows through the <pre> path so it stays
            // monospace and aligned.
            code: ({ className, children, ...props }) => {
              const isInline = !className && !String(children).includes('\n');
              if (isInline) {
                return (
                  <code className="bg-gray-100 dark:bg-gray-700 px-1.5 py-0.5 rounded text-sm font-mono text-pink-600 dark:text-pink-400">
                    {children}
                  </code>
                );
              }
              return <code className={className} {...props}>{children}</code>;
            },
            // leading-5 keeps box-drawing diagrams connected vertically.
            pre: ({ children }) => (
              <pre className="bg-[#1e1e1e] text-gray-300 p-4 rounded-lg overflow-x-auto mb-4 text-sm font-mono leading-5">
                {children}
              </pre>
            ),
            blockquote: ({ children }) => (
              <blockquote className="border-l-4 border-blue-500 pl-4 italic text-gray-600 dark:text-gray-400 my-4">
                {children}
              </blockquote>
            ),
            table: ({ children }) => (
              <div className="overflow-x-auto mb-4">
                <table className="w-full border-collapse border border-gray-300 dark:border-gray-600">{children}</table>
              </div>
            ),
            thead: ({ children }) => <thead className="bg-gray-100 dark:bg-gray-700">{children}</thead>,
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
            hr: () => <hr className="border-gray-300 dark:border-gray-600 my-6" />,
            strong: ({ children }) => <strong className="font-semibold text-gray-900 dark:text-white">{children}</strong>,
            em: ({ children }) => <em className="italic text-gray-700 dark:text-gray-300">{children}</em>,
          }}
        >
          {content}
        </ReactMarkdown>
      </div>
    </div>
  );
};

export default TheoryViewer;
