import { useState, useEffect } from 'react';

/**
 * TableOfContents — a sticky, scroll-spy outline for the theory pane.
 *
 * Instead of re-deriving heading slugs (which risks drifting from what
 * rehype-slug actually rendered), it reads the real h2/h3 ids out of the DOM
 * inside `containerId`, then uses an IntersectionObserver to highlight the
 * section currently in view. Re-runs whenever `contentKey` changes.
 *
 * @param {string} containerId - id of the element wrapping the rendered markdown
 * @param {string} contentKey  - changes when the topic content changes
 * @param {string} accent      - 'blue' (DSA) or 'emerald' (Python)
 */
const TableOfContents = ({ containerId, contentKey, accent = 'blue' }) => {
  const [headings, setHeadings] = useState([]);
  const [activeId, setActiveId] = useState(null);

  useEffect(() => {
    const container = document.getElementById(containerId);
    if (!container) return;

    const nodes = Array.from(container.querySelectorAll('h2[id], h3[id]'));
    const collected = nodes.map((el) => ({
      id: el.id,
      text: el.textContent,
      level: Number(el.tagName.substring(1)),
    }));
    // Reading the rendered DOM is exactly the external-system sync this effect
    // exists for; setting state from it here is intentional.
    // eslint-disable-next-line react-hooks/set-state-in-effect
    setHeadings(collected);
    setActiveId(collected[0]?.id ?? null);

    if (nodes.length === 0) return;

    // Mark the topmost heading currently within the upper part of the viewport.
    const observer = new IntersectionObserver(
      (entries) => {
        const visible = entries
          .filter((e) => e.isIntersecting)
          .sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top);
        if (visible[0]) setActiveId(visible[0].target.id);
      },
      { rootMargin: '0px 0px -70% 0px', threshold: [0, 1] }
    );

    nodes.forEach((n) => observer.observe(n));
    return () => observer.disconnect();
  }, [containerId, contentKey]);

  if (headings.length < 2) return null;

  const activeText = accent === 'emerald' ? 'text-emerald-600 dark:text-emerald-400' : 'text-blue-600 dark:text-blue-400';
  const activeBorder = accent === 'emerald' ? 'border-emerald-500' : 'border-blue-500';

  const handleClick = (e, id) => {
    e.preventDefault();
    const el = document.getElementById(id);
    if (el) {
      el.scrollIntoView({ behavior: 'smooth', block: 'start' });
      setActiveId(id);
    }
  };

  return (
    <nav aria-label="On this page" className="sticky top-32 max-h-[calc(100vh-10rem)] overflow-y-auto">
      <p className="text-xs font-semibold uppercase tracking-wider text-gray-400 dark:text-gray-500 mb-3 px-3">
        On this page
      </p>
      <ul className="space-y-0.5 border-l border-gray-200 dark:border-gray-700">
        {headings.map((h) => {
          const isActive = h.id === activeId;
          return (
            <li key={h.id}>
              <a
                href={`#${h.id}`}
                onClick={(e) => handleClick(e, h.id)}
                className={`block py-1 pr-2 text-sm transition-colors border-l-2 -ml-px ${
                  h.level === 3 ? 'pl-6' : 'pl-3'
                } ${
                  isActive
                    ? `${activeText} ${activeBorder} font-medium`
                    : 'text-gray-500 dark:text-gray-400 border-transparent hover:text-gray-900 dark:hover:text-gray-200'
                }`}
                aria-current={isActive ? 'location' : undefined}
              >
                {h.text}
              </a>
            </li>
          );
        })}
      </ul>
    </nav>
  );
};

export default TableOfContents;
