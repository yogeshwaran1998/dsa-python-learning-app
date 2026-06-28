import { createContext, useContext, useState, useEffect } from 'react';
import {
  createUserWithEmailAndPassword,
  signInWithEmailAndPassword,
  signOut,
  onAuthStateChanged,
  updateProfile,
  sendEmailVerification,
  GoogleAuthProvider,
  signInWithPopup
} from 'firebase/auth';
import { auth } from '../lib/firebase';

const AuthContext = createContext(null);

export function useAuth() {
  return useContext(AuthContext);
}

/** Derive the display label for a Firebase user (name → email prefix → uid fragment). */
function getDisplayName(firebaseUser) {
  if (!firebaseUser) return '';
  if (firebaseUser.displayName) return firebaseUser.displayName;
  if (firebaseUser.email) return firebaseUser.email.split('@')[0];
  return firebaseUser.uid.slice(0, 8);
}

/** Derive initials (up to 2 chars) from a display name string. */
function getInitials(name = '') {
  const words = name.trim().split(/\s+/);
  if (words.length >= 2) return (words[0][0] + words[1][0]).toUpperCase();
  return name.slice(0, 2).toUpperCase();
}

function buildUserObject(firebaseUser) {
  return {
    uid: firebaseUser.uid,
    email: firebaseUser.email,
    emailVerified: firebaseUser.emailVerified,
    displayName: firebaseUser.displayName,
    photoURL: firebaseUser.photoURL,
    // Derived helpers — convenient for components
    name: getDisplayName(firebaseUser),
    initials: getInitials(getDisplayName(firebaseUser))
  };
}

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Listen to auth state changes
  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, (firebaseUser) => {
      setUser(firebaseUser ? buildUserObject(firebaseUser) : null);
      setLoading(false);
    });
    return () => unsubscribe();
  }, []);

  /**
   * Register a new email/password user.
   * Sets displayName, sends a verification email, then signs out immediately.
   * The caller should show a "check your inbox" screen — do NOT navigate to '/'.
   * Returns { email } so the UI can display which address was used.
   */
  const register = async (name, email, password) => {
    setError(null);
    const userCredential = await createUserWithEmailAndPassword(auth, email, password);
    const firebaseUser = userCredential.user;

    // Set the display name right away so it appears in the verification email
    await updateProfile(firebaseUser, { displayName: name.trim() });

    // Send verification email
    await sendEmailVerification(firebaseUser);

    // Sign out so unverified users cannot access the app
    await signOut(auth);

    return { email };
  };

  /**
   * Sign in with email/password.
   * Throws auth/email-not-verified if the account hasn't been verified yet,
   * so the caller can show a Resend option.
   */
  const login = async (email, password) => {
    setError(null);
    const userCredential = await signInWithEmailAndPassword(auth, email, password);
    if (!userCredential.user.emailVerified) {
      await signOut(auth);
      const err = new Error('Please verify your email before signing in.');
      err.code = 'auth/email-not-verified';
      throw err;
    }
    return buildUserObject(userCredential.user);
  };

  /**
   * Sign in (or register) with Google via popup.
   * Google accounts are pre-verified — no gate needed.
   */
  const loginWithGoogle = async () => {
    setError(null);
    const provider = new GoogleAuthProvider();
    const userCredential = await signInWithPopup(auth, provider);
    return buildUserObject(userCredential.user);
  };

  /**
   * Resend a verification email.
   * Signs in silently, sends the email, then signs out again.
   */
  const resendVerification = async (email, password) => {
    setError(null);
    const userCredential = await signInWithEmailAndPassword(auth, email, password);
    await sendEmailVerification(userCredential.user);
    await signOut(auth);
  };

  // Logout
  const logout = async () => {
    setError(null);
    await signOut(auth);
  };

  const value = {
    user,
    loading,
    error,
    register,
    login,
    loginWithGoogle,
    resendVerification,
    logout,
    isAuthenticated: !!user
  };

  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  );
}

export default AuthContext;
