// localStorage progress tracking for topic completion

const STORAGE_KEY = 'dsa_learning_progress';

/**
 * Get the current progress from localStorage
 * @returns {Object} - Progress object with completed topic IDs
 */
export function getProgress() {
  try {
    const stored = localStorage.getItem(STORAGE_KEY);
    if (stored) {
      return JSON.parse(stored);
    }
  } catch (error) {
    console.error('Error reading progress from localStorage:', error);
  }
  return { completedTopics: [] };
}

/**
 * Save progress to localStorage
 * @param {Object} progress - Progress object to save
 */
function saveProgress(progress) {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(progress));
  } catch (error) {
    console.error('Error saving progress to localStorage:', error);
  }
}

/**
 * Check if a topic is completed
 * @param {string} topicId - The topic ID to check
 * @returns {boolean} - True if the topic is completed
 */
export function isTopicCompleted(topicId) {
  const progress = getProgress();
  return progress.completedTopics.includes(topicId);
}

/**
 * Mark a topic as completed
 * @param {string} topicId - The topic ID to mark as completed
 */
export function markTopicCompleted(topicId) {
  const progress = getProgress();
  if (!progress.completedTopics.includes(topicId)) {
    progress.completedTopics.push(topicId);
    saveProgress(progress);
  }
}

/**
 * Mark a topic as not completed (undo)
 * @param {string} topicId - The topic ID to mark as not completed
 */
export function markTopicIncomplete(topicId) {
  const progress = getProgress();
  progress.completedTopics = progress.completedTopics.filter((id) => id !== topicId);
  saveProgress(progress);
}

/**
 * Toggle topic completion status
 * @param {string} topicId - The topic ID to toggle
 * @returns {boolean} - New completion status
 */
export function toggleTopicCompletion(topicId) {
  if (isTopicCompleted(topicId)) {
    markTopicIncomplete(topicId);
    return false;
  } else {
    markTopicCompleted(topicId);
    return true;
  }
}

/**
 * Get the count of completed topics
 * @returns {number} - Number of completed topics
 */
export function getCompletedCount() {
  const progress = getProgress();
  return progress.completedTopics.length;
}

/**
 * Get completion percentage for a category
 * @param {string[]} topicIds - Array of topic IDs in the category
 * @returns {number} - Percentage completed (0-100)
 */
export function getCategoryCompletionPercentage(topicIds) {
  const completed = topicIds.filter((id) => isTopicCompleted(id)).length;
  return topicIds.length > 0 ? Math.round((completed / topicIds.length) * 100) : 0;
}

/**
 * Reset all progress
 */
export function resetProgress() {
  localStorage.removeItem(STORAGE_KEY);
}

/**
 * Get all completed topic IDs
 * @returns {string[]} - Array of completed topic IDs
 */
export function getCompletedTopics() {
  const progress = getProgress();
  return progress.completedTopics;
}

export default {
  getProgress,
  isTopicCompleted,
  markTopicCompleted,
  markTopicIncomplete,
  toggleTopicCompletion,
  getCompletedCount,
  getCategoryCompletionPercentage,
  resetProgress,
  getCompletedTopics,
};
