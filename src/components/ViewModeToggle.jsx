/**
 * Segmented toggle for switching between Split / Theory-only / Code-only view modes
 * on tablet and desktop. Hidden on mobile (the existing Theory/Code tabs handle that).
 *
 * Props:
 *   value   — current mode: 'split' | 'theory' | 'code'
 *   onChange — callback(mode: string)
 *   accent  — 'blue' (DSA, default) | 'emerald' (Python)
 */
export default function ViewModeToggle({ value, onChange, accent = 'blue' }) {
  const activeText  = accent === 'emerald' ? 'text-emerald-600 dark:text-emerald-400' : 'text-blue-600 dark:text-blue-400';

  const segments = [
    {
      id: 'split',
      label: 'Split',
      ariaLabel: 'Split view — Theory and Code side by side',
      icon: (
        // Two-column layout icon
        <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
          <path strokeLinecap="round" strokeLinejoin="round" d="M9 4H5a1 1 0 00-1 1v14a1 1 0 001 1h4M15 4h4a1 1 0 011 1v14a1 1 0 01-1 1h-4M12 4v16" />
        </svg>
      ),
    },
    {
      id: 'theory',
      label: 'Theory',
      ariaLabel: 'Theory-only view',
      icon: (
        // Book icon — same path used in TheoryViewer header
        <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
          <path strokeLinecap="round" strokeLinejoin="round" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
        </svg>
      ),
    },
    {
      id: 'code',
      label: 'Code',
      ariaLabel: 'Code-only view',
      icon: (
        // Terminal/code icon — same path used in CodeViewer header
        <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
          <path strokeLinecap="round" strokeLinejoin="round" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4" />
        </svg>
      ),
    },
  ];

  return (
    <div
      role="group"
      aria-label="View mode"
      className="inline-flex items-center rounded-lg bg-gray-100 dark:bg-gray-800 p-1 gap-0.5"
    >
      {segments.map((seg) => {
        const isActive = value === seg.id;
        return (
          <button
            key={seg.id}
            onClick={() => onChange(seg.id)}
            aria-pressed={isActive}
            aria-label={seg.ariaLabel}
            className={`flex items-center gap-1.5 px-3 py-1.5 text-sm font-medium rounded-md transition-all duration-150 ${
              isActive
                ? `bg-white dark:bg-gray-700 shadow-sm ${activeText}`
                : 'text-gray-500 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white'
            }`}
          >
            {seg.icon}
            <span className="hidden lg:inline">{seg.label}</span>
          </button>
        );
      })}
    </div>
  );
}
