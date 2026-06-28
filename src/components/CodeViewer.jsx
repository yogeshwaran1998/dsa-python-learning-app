import { useState, useMemo } from 'react';
import Prism from 'prismjs';
import 'prismjs/components/prism-python';
import 'prismjs/themes/prism-tomorrow.css';

/**
 * CodeViewer - displays code with Prism syntax highlighting, line numbers, a
 * copy button, and click-to-highlight line anchoring.
 *
 * Highlighting is memoized per `code`/`language` change (via useMemo) instead of
 * re-running on every render, and we no longer call the global
 * `Prism.highlightAll()` — each line is tokenized exactly once.
 */
const CodeViewer = ({ code, language = 'python', title }) => {
  const [copied, setCopied] = useState(false);
  const [activeLine, setActiveLine] = useState(null);

  const grammar = Prism.languages[language] || Prism.languages.python;

  // Tokenize once per code change. Per-line so we can render a line-number
  // gutter and anchor individual lines.
  const highlightedLines = useMemo(
    () => code.split('\n').map((line) => Prism.highlight(line || ' ', grammar, language)),
    [code, language, grammar]
  );

  const handleCopy = async () => {
    try {
      await navigator.clipboard.writeText(code);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch (err) {
      console.error('Failed to copy code:', err);
    }
  };

  return (
    <div className="code-viewer h-full overflow-auto">
      {/* Header with terminal icon */}
      <div className="flex items-center justify-between mb-4 pb-4 border-b border-gray-200 dark:border-gray-700">
        <div className="flex items-center gap-3">
          <div className="flex-shrink-0 w-10 h-10 rounded-lg bg-emerald-100 dark:bg-emerald-900 flex items-center justify-center">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              className="h-5 w-5 text-emerald-600 dark:text-emerald-400"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
              strokeWidth={2}
            >
              <path strokeLinecap="round" strokeLinejoin="round" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4" />
            </svg>
          </div>
          <div>
            <h2 className="text-xl font-semibold text-gray-900 dark:text-white">{title || 'Code'}</h2>
            <p className="text-sm text-gray-500 dark:text-gray-400">Python implementation</p>
          </div>
        </div>

        {/* Language badge */}
        <div className="flex items-center gap-2">
          <span className="px-3 py-1 text-xs font-medium rounded-full bg-blue-100 dark:bg-blue-900 text-blue-700 dark:text-blue-300">
            {language.toUpperCase()}
          </span>
        </div>
      </div>

      {/* Code container with dark theme */}
      <div className="rounded-xl overflow-hidden border border-gray-300 dark:border-gray-700 bg-[#1e1e1e]">
        {/* Toolbar with copy button */}
        <div className="flex items-center justify-between px-4 py-2 bg-[#252526] border-b border-[#3c3c3c]">
          <div className="flex items-center gap-2">
            <div className="flex gap-1.5">
              <span className="w-3 h-3 rounded-full bg-red-500"></span>
              <span className="w-3 h-3 rounded-full bg-yellow-500"></span>
              <span className="w-3 h-3 rounded-full bg-green-500"></span>
            </div>
            <span className="ml-2 text-xs text-gray-400 font-mono">main.py</span>
          </div>

          <button
            onClick={handleCopy}
            className="flex items-center gap-1.5 px-3 py-1.5 text-xs font-medium rounded-md bg-[#3c3c3c] hover:bg-[#4a4a4a] text-gray-300 transition-colors duration-200"
          >
            {copied ? (
              <>
                <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 text-green-400" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                  <path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7" />
                </svg>
                <span className="text-green-400">Copied!</span>
              </>
            ) : (
              <>
                <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                  <path strokeLinecap="round" strokeLinejoin="round" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z" />
                </svg>
                <span>Copy</span>
              </>
            )}
          </button>
        </div>

        {/* Code with line numbers */}
        <div className="overflow-x-auto">
          <pre className="p-0 m-0 bg-transparent">
            <code className="block">
              {highlightedLines.map((html, index) => {
                const lineNo = index + 1;
                const isActive = activeLine === lineNo;
                return (
                  <div
                    key={index}
                    className={`flex ${isActive ? 'bg-[#3a3d41]' : 'hover:bg-[#2a2d2e]'}`}
                  >
                    <button
                      type="button"
                      onClick={() => setActiveLine(isActive ? null : lineNo)}
                      className={`flex-shrink-0 w-12 text-right pr-3 select-none text-sm font-mono leading-6 cursor-pointer ${
                        isActive ? 'text-blue-400' : 'text-gray-500 hover:text-gray-300'
                      }`}
                      aria-label={`Toggle highlight on line ${lineNo}`}
                    >
                      {lineNo}
                    </button>
                    <span
                      className="flex-1 text-sm font-mono leading-6 text-gray-300 whitespace-pre"
                      dangerouslySetInnerHTML={{ __html: html }}
                    />
                  </div>
                );
              })}
            </code>
          </pre>
        </div>
      </div>
    </div>
  );
};

export default CodeViewer;
