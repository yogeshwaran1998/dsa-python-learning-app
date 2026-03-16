// Utility functions to load .md and .py content files
// Uses fetch for loading content in development mode

const DSA_BASE_PATH = '/../..';

// Cache for loaded content
const contentCache = new Map();

/**
 * Fetch content from a file path
 * @param {string} path - Relative path to the file
 * @returns {Promise<string>} - File content
 */
async function fetchContent(path) {
  // Check cache first
  if (contentCache.has(path)) {
    return contentCache.get(path);
  }

  try {
    // In Vite dev mode, we need to use the public folder or fetch from the file system
    // For relative paths, we'll try to fetch using the full path from the app root
    const fullPath = `${DSA_BASE_PATH}${path}`;
    const response = await fetch(fullPath);

    if (!response.ok) {
      throw new Error(`Failed to fetch ${path}: ${response.statusText}`);
    }

    const content = await response.text();
    contentCache.set(path, content);
    return content;
  } catch (error) {
    console.error(`Error loading content from ${path}:`, error);
    throw error;
  }
}

/**
 * Load markdown content for a topic
 * @param {string} mdPath - Path to the .md file
 * @returns {Promise<string>} - Markdown content
 */
export async function loadMarkdown(mdPath) {
  return fetchContent(mdPath);
}

/**
 * Load Python code content for a topic
 * @param {string} pyPath - Path to the .py file
 * @returns {Promise<string>} - Python code content
 */
export async function loadPythonCode(pyPath) {
  return fetchContent(pyPath);
}

/**
 * Load both markdown and Python content for a topic
 * @param {Object} topic - Topic object with mdFile and pyFile
 * @param {string} basePath - Base path to the topic folder
 * @returns {Promise<{md: string, py: string}>} - Object with both contents
 */
export async function loadTopicContent(topic, basePath) {
  const mdPath = `${basePath}/${topic.mdFile}`;
  const pyPath = `${basePath}/${topic.pyFile}`;

  const [mdContent, pyContent] = await Promise.all([
    loadMarkdown(mdPath),
    loadPythonCode(pyPath),
  ]);

  return {
    md: mdContent,
    py: pyContent,
  };
}

/**
 * Load Python topic content
 * @param {Object} topic - Python topic object
 * @returns {Promise<{md: string, py: string}>} - Object with both contents
 */
export async function loadPythonTopicContent(topic) {
  const basePath = `../../00_python_fundamentals/${topic.folder}`;
  return loadTopicContent(topic, basePath);
}

/**
 * Load DSA topic content
 * @param {Object} topic - DSA topic object
 * @returns {Promise<{md: string, py: string}>} - Object with both contents
 */
export async function loadDSATopicContent(topic) {
  const basePath = `../../${topic.folder}`;
  return loadTopicContent(topic, basePath);
}

/**
 * Clear the content cache
 */
export function clearContentCache() {
  contentCache.clear();
}

/**
 * Check if a topic's content is cached
 * @param {string} path - Path to check
 * @returns {boolean}
 */
export function isContentCached(path) {
  return contentCache.has(path);
}

export default {
  loadMarkdown,
  loadPythonCode,
  loadTopicContent,
  loadPythonTopicContent,
  loadDSATopicContent,
  clearContentCache,
  isContentCached,
};
