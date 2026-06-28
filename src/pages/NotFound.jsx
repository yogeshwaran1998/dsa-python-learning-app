import { Link } from 'react-router-dom';
import ThemeToggle from '../components/ThemeToggle';

/** Friendly 404 for any unmatched route. */
const NotFound = () => (
  <div className="min-h-screen bg-gray-50 dark:bg-gray-900 flex flex-col items-center justify-center p-6 text-center">
    <div className="absolute top-6 right-6">
      <ThemeToggle />
    </div>
    <p className="text-6xl font-extrabold text-blue-600 dark:text-blue-400 mb-4">404</p>
    <h1 className="text-2xl font-bold text-gray-900 dark:text-white mb-2">Page not found</h1>
    <p className="text-gray-600 dark:text-gray-400 mb-6 max-w-md">
      The page you're looking for doesn't exist or may have moved.
    </p>
    <Link
      to="/"
      className="px-5 py-2.5 text-sm font-medium text-white bg-blue-600 hover:bg-blue-700 rounded-lg transition-colors"
    >
      Back to home
    </Link>
  </div>
);

export default NotFound;
