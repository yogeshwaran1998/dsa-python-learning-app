import { useState, useEffect, useCallback } from 'react';
import { doc, getDoc, setDoc, onSnapshot } from 'firebase/firestore';
import { useAuth } from '../contexts/AuthContext';
import { db } from '../lib/firebase';

const PROGRESS_DEFAULTS = {
  completedTopics: {
    python: [],
    dsa: []
  },
  lastUpdated: null
};

/**
 * Custom hook for Firestore-based progress tracking
 * Only works when user is logged in
 */
export function useProgress() {
  const { user, isAuthenticated } = useAuth();
  const [completedTopics, setCompletedTopics] = useState({
    python: [],
    dsa: []
  });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch progress from Firestore when user logs in
  useEffect(() => {
    if (!isAuthenticated || !user) {
      setCompletedTopics(PROGRESS_DEFAULTS.completedTopics);
      setLoading(false);
      return;
    }

    setLoading(true);
    const progressRef = doc(db, 'userProgress', user.uid);

    // Set up real-time listener
    const unsubscribe = onSnapshot(
      progressRef,
      (docSnap) => {
        if (docSnap.exists()) {
          const data = docSnap.data();
          setCompletedTopics(data.completedTopics || PROGRESS_DEFAULTS.completedTopics);
        } else {
          // Create initial progress document if it doesn't exist
          setDoc(progressRef, {
            ...PROGRESS_DEFAULTS,
            lastUpdated: new Date().toISOString()
          });
          setCompletedTopics(PROGRESS_DEFAULTS.completedTopics);
        }
        setLoading(false);
      },
      (err) => {
        console.error('Error fetching progress:', err);
        setError(err.message);
        setLoading(false);
      }
    );

    return () => unsubscribe();
  }, [user, isAuthenticated]);

  // Mark a topic as completed
  const markCompleted = useCallback(async (topicId, type = 'python') => {
    if (!isAuthenticated || !user) {
      throw new Error('Must be logged in to track progress');
    }

    const typeKey = type === 'python' ? 'python' : 'dsa';
    const progressRef = doc(db, 'userProgress', user.uid);

    // Get current progress
    const docSnap = await getDoc(progressRef);
    const currentData = docSnap.exists() ? docSnap.data() : PROGRESS_DEFAULTS;
    const currentTopics = currentData.completedTopics || PROGRESS_DEFAULTS.completedTopics;

    // Only add if not already present
    if (!currentTopics[typeKey].includes(topicId)) {
      const newTopics = {
        ...currentTopics,
        [typeKey]: [...currentTopics[typeKey], topicId]
      };

      await setDoc(progressRef, {
        completedTopics: newTopics,
        lastUpdated: new Date().toISOString()
      });
    }
  }, [user, isAuthenticated]);

  // Mark a topic as not completed (undo)
  const markIncomplete = useCallback(async (topicId, type = 'python') => {
    if (!isAuthenticated || !user) {
      throw new Error('Must be logged in to track progress');
    }

    const typeKey = type === 'python' ? 'python' : 'dsa';
    const progressRef = doc(db, 'userProgress', user.uid);

    const docSnap = await getDoc(progressRef);
    const currentData = docSnap.exists() ? docSnap.data() : PROGRESS_DEFAULTS;
    const currentTopics = currentData.completedTopics || PROGRESS_DEFAULTS.completedTopics;

    const newTopics = {
      ...currentTopics,
      [typeKey]: currentTopics[typeKey].filter(id => id !== topicId)
    };

    await setDoc(progressRef, {
      completedTopics: newTopics,
      lastUpdated: new Date().toISOString()
    });
  }, [user, isAuthenticated]);

  // Check if a topic is completed
  const isCompleted = useCallback((topicId, type = 'python') => {
    const typeKey = type === 'python' ? 'python' : 'dsa';
    return completedTopics[typeKey]?.includes(topicId) || false;
  }, [completedTopics]);

  // Get progress percentage for a category
  const getProgress = useCallback((type = 'python', totalTopics) => {
    const typeKey = type === 'python' ? 'python' : 'dsa';
    const completed = completedTopics[typeKey]?.length || 0;
    return totalTopics > 0 ? Math.round((completed / totalTopics) * 100) : 0;
  }, [completedTopics]);

  // Get completed count for a category
  const getCount = useCallback((type = 'python') => {
    const typeKey = type === 'python' ? 'python' : 'dsa';
    return completedTopics[typeKey]?.length || 0;
  }, [completedTopics]);

  // Reset all progress
  const resetProgress = useCallback(async () => {
    if (!isAuthenticated || !user) {
      throw new Error('Must be logged in to reset progress');
    }

    const progressRef = doc(db, 'userProgress', user.uid);
    await setDoc(progressRef, {
      ...PROGRESS_DEFAULTS,
      lastUpdated: new Date().toISOString()
    });
  }, [user, isAuthenticated]);

  return {
    completedTopics,
    markCompleted,
    markIncomplete,
    isCompleted,
    getProgress,
    getCount,
    resetProgress,
    loading,
    error,
    isAuthenticated,
    pythonCount: completedTopics.python?.length || 0,
    dsaCount: completedTopics.dsa?.length || 0
  };
}

export default useProgress;
