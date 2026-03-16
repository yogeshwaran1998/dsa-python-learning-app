export default function TopicCard({
  topicNumber,
  title,
  description,
  category = 'python',
  onClick,
  isActive = false,
}) {
  // Category-specific colors
  const categoryStyles = {
    python: {
      bgLight: 'bg-blue-50',
      bgDark: 'dark:bg-blue-900/20',
      borderLight: 'border-blue-200',
      borderDark: 'dark:border-blue-800',
      textLight: 'text-blue-600',
      textDark: 'dark:text-blue-400',
      hoverLight: 'hover:border-blue-400 hover:bg-blue-50',
      hoverDark: 'dark:hover:border-blue-600 dark:hover:bg-blue-900/30',
    },
    dsa: {
      bgLight: 'bg-green-50',
      bgDark: 'dark:bg-green-900/20',
      borderLight: 'border-green-200',
      borderDark: 'dark:border-green-800',
      textLight: 'text-green-600',
      textDark: 'dark:text-green-400',
      hoverLight: 'hover:border-green-400 hover:bg-green-50',
      hoverDark: 'dark:hover:border-green-600 dark:hover:bg-green-900/30',
    },
  }

  const styles = categoryStyles[category] || categoryStyles.python

  return (
    <button
      onClick={onClick}
      className={`w-full text-left p-4 rounded-xl border-2 transition-all duration-200 cursor-pointer
        ${styles.bgLight} ${styles.bgDark}
        ${styles.borderLight} ${styles.borderDark}
        ${styles.hoverLight} ${styles.hoverDark}
        ${isActive ? 'ring-2 ring-blue-500 ring-offset-2 dark:ring-offset-gray-900' : ''}
        group
      `}
    >
      <div className="flex items-start gap-4">
        {/* Topic Number Badge */}
        <div
          className={`flex-shrink-0 w-10 h-10 rounded-lg flex items-center justify-center font-mono font-bold text-sm
            ${styles.bgLight} ${styles.bgDark}
            ${styles.textLight} ${styles.textDark}
          `}
        >
          {topicNumber}
        </div>

        {/* Content */}
        <div className="flex-1 min-w-0">
          <h3 className="font-semibold text-gray-900 dark:text-gray-100 group-hover:text-blue-600 dark:group-hover:text-blue-400 transition-colors">
            {title}
          </h3>
          {description && (
            <p className="mt-1 text-sm text-gray-600 dark:text-gray-400 line-clamp-2">
              {description}
            </p>
          )}
        </div>

        {/* Arrow Icon */}
        <div className="flex-shrink-0 text-gray-400 dark:text-gray-500 group-hover:text-blue-500 dark:group-hover:text-blue-400 transform group-hover:translate-x-1 transition-all">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            strokeWidth={2}
            stroke="currentColor"
            className="w-5 h-5"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              d="M13.5 4.5 21 12m0 0-7.5 7.5M21 12H3"
            />
          </svg>
        </div>
      </div>
    </button>
  )
}
