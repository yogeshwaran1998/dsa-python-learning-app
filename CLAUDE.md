# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
npm run dev       # Start Vite dev server (usually http://localhost:5173)
npm run build     # Production build
npm run preview   # Preview production build
npm run lint      # ESLint
```

There are no tests in this project.

## Environment Setup

Firebase credentials must be set in a `.env` file at the project root:

```
VITE_FIREBASE_API_KEY=
VITE_FIREBASE_AUTH_DOMAIN=
VITE_FIREBASE_PROJECT_ID=
VITE_FIREBASE_STORAGE_BUCKET=
VITE_FIREBASE_MESSAGING_SENDER_ID=
VITE_FIREBASE_APP_ID=
```

## Architecture

### Content Model

The app has two learning tracks:
- **Python** — 26 topics, IDs like `01_syntax_datatypes`, `02_operators`, etc.
- **DSA** — 20 topics, IDs like `01_arrays_strings`, `02_two_pointers_sliding_window`, etc.

Each topic has a `.md` (theory) and `.py` (code) file, served statically from `public/content/`:
- Python: `public/content/00_python_fundamentals/{topic_id}/{topic.mdFile|pyFile}`
- DSA: `public/content/{topic_id}/{topic.mdFile|pyFile}`

The topic lists with metadata (id, title, mdFile, pyFile) live **inside `TopicDetail.jsx`** — not in `src/data/topics.js` (that file exists but is separate). When adding or renaming topics, update the arrays in `TopicDetail.jsx` and add the corresponding files in `public/content/`.

### Routing & `TopicDetail`

`TopicDetail` is the shared page for both tracks. The `type` prop (`"python"` or `"dsa"`) is passed from `App.jsx` via the route definition:

```jsx
<Route path="/python/:topicId" element={<TopicDetail type="python" />} />
<Route path="/dsa/:topicId"    element={<TopicDetail type="dsa" />} />
```

Legacy routes (`/topic/:category/:id`) also exist for backward compatibility and derive `type` from the `category` URL param. `type` controls which topic list is used, the content path, progress tracking bucket, and UI accent color (green = Python, blue = DSA).

### State & Auth

- `AuthContext` (`src/contexts/AuthContext.jsx`) — wraps the entire app, provides `user`, `isAuthenticated`, `login()`, `register()`, `logout()`.
- `useProgress` (`src/hooks/useProgress.js`) — Firestore real-time listener on `userProgress/{uid}`. Exposes `markCompleted`, `markIncomplete`, `isCompleted`, `getProgress`, `resetProgress`. All writes require the user to be authenticated.
- Zustand is installed but not used; all state is React Context + local `useState`.

### Theme

Dark mode uses Tailwind's `dark:` variant. The toggle state is persisted in `localStorage` and applied as a class on `<html>`. Colors use CSS custom properties defined in `src/index.css`.

### Color Convention

- Python UI accent: **green** (`bg-green-600 hover:bg-green-700`)
- DSA UI accent: **blue** (`bg-blue-600 hover:bg-blue-700`)

This applies to buttons, checkmarks, and progress indicators throughout the app.
