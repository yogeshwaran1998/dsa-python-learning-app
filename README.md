# DSA Python Learning App

> Interactive Python & Data Structures interview-prep — theory and runnable code side by side, with progress tracking.

**Live demo:** [dsa-python-learning-app.netlify.app](https://dsa-python-learning-app.netlify.app)

---

## Features

- **46 structured topics** — 26 Python fundamentals + 20 classic DSA patterns
- **Side-by-side layout** — markdown theory panel alongside a working Python code example for every topic
- **Progress tracking** — mark topics complete; progress synced to your account across devices via Firebase Firestore
- **⌘K / Ctrl+K command palette** — instant fuzzy search across all 46 topic titles
- **Google Sign-In + email/password auth** — email verification gate so only confirmed addresses can access the app
- **Dark mode** — system-aware, persisted in `localStorage`
- **Responsive** — works on mobile (tabbed theory/code view) and desktop (split panel)

## Tech Stack

| Layer | Technology |
| --- | --- |
| UI | React 19, Vite 7, Tailwind CSS v4 |
| Auth | Firebase Authentication (email/password + Google) |
| Database | Firebase Firestore (progress storage) |
| Routing | React Router v7 |
| Markdown | react-markdown + rehype-highlight + rehype-raw |
| Hosting | Netlify |

## Getting Started

### 1. Clone

```bash
git clone https://github.com/yogeshwaran1998/dsa-python-learning-app.git
cd dsa-python-learning-app/dsa-learning-app
```

### 2. Install

```bash
npm install
```

### 3. Configure Firebase

Create a `.env` file at the project root (`dsa-learning-app/.env`):

```env
VITE_FIREBASE_API_KEY=your_api_key
VITE_FIREBASE_AUTH_DOMAIN=your_project.firebaseapp.com
VITE_FIREBASE_PROJECT_ID=your_project_id
VITE_FIREBASE_STORAGE_BUCKET=your_project.appspot.com
VITE_FIREBASE_MESSAGING_SENDER_ID=your_sender_id
VITE_FIREBASE_APP_ID=your_app_id
```

Enable **Email/Password** and **Google** sign-in providers in your Firebase console, and deploy the included `firestore.rules`.

### 4. Run

```bash
npm run dev
```

App starts at `http://localhost:5173`.

## Content Pipeline

Content (`.md` theory files and `.py` code files) lives in the **`content/`** directory inside this repo — for example `content/01_arrays_strings/arrays_strings.md`. The script `scripts/sync-content.mjs` mirrors these into `public/content/` so Vite can serve them as static assets.

The sync runs automatically on `npm run dev` and `npm run build` (via `predev`/`prebuild` hooks). `public/content/` is git-ignored — never edit it by hand.

Topic metadata (id, title, file names, category) is the single source of truth in `src/data/topicsConfig.js`. To add a topic: add an entry there and drop the matching `.md` + `.py` files in the corresponding `content/` subfolder.

## Firestore Security Rules

```js
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /userProgress/{userId} {
      allow read, write: if request.auth != null && request.auth.uid == userId;
    }
    match /{document=**} {
      allow read, write: if false;
    }
  }
}
```

## Project Structure

```text
dsa-learning-app/
├── src/
│   ├── contexts/AuthContext.jsx   # Auth state + Firebase helpers
│   ├── hooks/useProgress.js       # Firestore progress read/write
│   ├── data/topicsConfig.js       # Topic metadata (single source of truth)
│   ├── components/
│   │   ├── CommandPalette.jsx     # ⌘K search palette
│   │   ├── UserMenu.jsx           # Auth header widget
│   │   ├── TheoryViewer.jsx       # Markdown renderer
│   │   └── CodeViewer.jsx         # Syntax-highlighted code panel
│   └── pages/
│       ├── Home/Home.jsx
│       ├── DSATopics.jsx
│       ├── PythonTopics.jsx
│       └── TopicDetail/TopicDetail.jsx
├── scripts/sync-content.mjs      # Copies root content into public/
├── public/content/               # Generated — git-ignored
└── firestore.rules
```

## License

MIT — see [LICENSE](LICENSE).
