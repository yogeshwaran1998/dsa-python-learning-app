import { useState, useEffect, useMemo, useRef, useCallback } from 'react';
import { useNavigate } from 'react-router-dom';
import { pythonTopics, dsaTopics } from '../data/topicsConfig';

/**
 * CommandPalette — a ⌘K / Ctrl+K searchable launcher across every topic.
 *
 * - Opens on ⌘K / Ctrl+K (and closes on Escape).
 * - Fuzzy-ish substring match over topic title + track.
 * - Full keyboard nav: ↑/↓ to move, Enter to open, Esc to dismiss.
 */
const SEARCH_INDEX = [
  ...pythonTopics.map((t) => ({ ...t, track: 'python', label: 'Python', path: `/python/${t.id}` })),
  ...dsaTopics.map((t) => ({ ...t, track: 'dsa', label: 'DSA', path: `/dsa/${t.id}` })),
];

const CommandPalette = () => {
  const navigate = useNavigate();
  const [open, setOpen] = useState(false);
  const [query, setQuery] = useState('');
  const [activeIndex, setActiveIndex] = useState(0);
  const inputRef = useRef(null);
  const listRef = useRef(null);

  const results = useMemo(() => {
    const q = query.trim().toLowerCase();
    if (!q) return SEARCH_INDEX;
    return SEARCH_INDEX.filter(
      (t) => t.title.toLowerCase().includes(q) || t.label.toLowerCase().includes(q) || t.category.toLowerCase().includes(q)
    );
  }, [query]);

  const close = useCallback(() => {
    setOpen(false);
    setQuery('');
    setActiveIndex(0);
  }, []);

  // Global hotkey: ⌘K / Ctrl+K toggles the palette.
  useEffect(() => {
    const onKeyDown = (e) => {
      if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {
        e.preventDefault();
        setOpen((v) => {
          if (v) close();
          return !v;
        });
      } else if (e.key === 'Escape' && open) {
        close();
      }
    };
    const onOpenRequest = () => setOpen(true);
    window.addEventListener('keydown', onKeyDown);
    window.addEventListener('open-command-palette', onOpenRequest);
    return () => {
      window.removeEventListener('keydown', onKeyDown);
      window.removeEventListener('open-command-palette', onOpenRequest);
    };
  }, [open, close]);

  // Focus the input on open (no state writes — close() already resets state).
  useEffect(() => {
    if (open) requestAnimationFrame(() => inputRef.current?.focus());
  }, [open]);

  // activeIndex can momentarily exceed a freshly-filtered result list; clamp at
  // read time rather than chasing it with another effect.
  const clampedIndex = results.length ? Math.min(activeIndex, results.length - 1) : 0;

  const select = (item) => {
    if (!item) return;
    navigate(item.path);
    close();
  };

  const onInputKeyDown = (e) => {
    if (e.key === 'ArrowDown') {
      e.preventDefault();
      setActiveIndex(Math.min(clampedIndex + 1, results.length - 1));
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      setActiveIndex(Math.max(clampedIndex - 1, 0));
    } else if (e.key === 'Enter') {
      e.preventDefault();
      select(results[clampedIndex]);
    }
  };

  // Keep the active row visible while arrowing.
  useEffect(() => {
    const el = listRef.current?.querySelector(`[data-index="${clampedIndex}"]`);
    el?.scrollIntoView({ block: 'nearest' });
  }, [clampedIndex]);

  if (!open) return null;

  return (
    <div
      className="fixed inset-0 z-[1000] flex items-start justify-center px-4 pt-[12vh] bg-black/50 backdrop-blur-sm"
      onClick={close}
      role="dialog"
      aria-modal="true"
      aria-label="Search topics"
    >
      <div
        className="w-full max-w-xl bg-white dark:bg-gray-900 rounded-2xl shadow-2xl border border-gray-200 dark:border-gray-700 overflow-hidden"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Search input */}
        <div className="flex items-center gap-3 px-4 border-b border-gray-200 dark:border-gray-700">
          <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 text-gray-400 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
            <path strokeLinecap="round" strokeLinejoin="round" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
          </svg>
          <input
            ref={inputRef}
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onKeyDown={onInputKeyDown}
            placeholder="Search Python & DSA topics…"
            className="flex-1 py-4 bg-transparent text-gray-900 dark:text-white placeholder-gray-400 outline-none text-base"
            aria-label="Search topics"
          />
          <kbd className="hidden sm:block text-xs text-gray-400 border border-gray-300 dark:border-gray-600 rounded px-1.5 py-0.5">Esc</kbd>
        </div>

        {/* Results */}
        <ul ref={listRef} className="max-h-80 overflow-y-auto py-2">
          {results.length === 0 ? (
            <li className="px-4 py-8 text-center text-sm text-gray-500 dark:text-gray-400">
              No topics match “{query}”.
            </li>
          ) : (
            results.map((item, index) => {
              const isActive = index === clampedIndex;
              const accent = item.track === 'python' ? 'text-emerald-600 dark:text-emerald-400' : 'text-blue-600 dark:text-blue-400';
              const badge = item.track === 'python'
                ? 'bg-emerald-100 dark:bg-emerald-900/50 text-emerald-700 dark:text-emerald-300'
                : 'bg-blue-100 dark:bg-blue-900/50 text-blue-700 dark:text-blue-300';
              return (
                <li key={item.path} data-index={index}>
                  <button
                    type="button"
                    onMouseEnter={() => setActiveIndex(index)}
                    onClick={() => select(item)}
                    className={`w-full flex items-center justify-between gap-3 px-4 py-2.5 text-left transition-colors ${
                      isActive ? 'bg-gray-100 dark:bg-gray-800' : ''
                    }`}
                  >
                    <span className="flex items-center gap-3 min-w-0">
                      <span className={`text-xs font-semibold px-2 py-0.5 rounded-full flex-shrink-0 ${badge}`}>{item.label}</span>
                      <span className="truncate text-sm font-medium text-gray-900 dark:text-white">{item.title}</span>
                    </span>
                    <span className={`text-xs flex-shrink-0 ${isActive ? accent : 'text-gray-400'}`}>{item.category}</span>
                  </button>
                </li>
              );
            })
          )}
        </ul>

        {/* Footer hints */}
        <div className="flex items-center justify-between px-4 py-2 border-t border-gray-200 dark:border-gray-700 text-xs text-gray-400">
          <span className="flex items-center gap-1.5">
            <kbd className="border border-gray-300 dark:border-gray-600 rounded px-1">↑</kbd>
            <kbd className="border border-gray-300 dark:border-gray-600 rounded px-1">↓</kbd>
            to navigate
          </span>
          <span className="flex items-center gap-1.5">
            <kbd className="border border-gray-300 dark:border-gray-600 rounded px-1">↵</kbd>
            to open
          </span>
        </div>
      </div>
    </div>
  );
};

export default CommandPalette;
