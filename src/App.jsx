import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { AuthProvider } from './contexts/AuthContext';
import ErrorBoundary from './components/ErrorBoundary';
import Home from './pages/Home/Home';
import PythonTopics from './pages/PythonTopics';
import DSATopics from './pages/DSATopics';
import TopicDetail from './pages/TopicDetail/TopicDetail';
import Login from './pages/Auth/Login';
import Register from './pages/Auth/Register';
import NotFound from './pages/NotFound';
import CommandPalette from './components/CommandPalette';

function App() {
  return (
    <ErrorBoundary>
      <AuthProvider>
        <Router>
          <CommandPalette />
          <Routes>
            {/* Home route */}
            <Route path="/" element={<Home />} />

            {/* Auth routes */}
            <Route path="/login" element={<Login />} />
            <Route path="/register" element={<Register />} />

            {/* Python Topics routes */}
            <Route path="/python" element={<PythonTopics />} />
            <Route path="/python/:topicId" element={<TopicDetail type="python" />} />

            {/* DSA Topics routes */}
            <Route path="/dsa" element={<DSATopics />} />
            <Route path="/dsa/:topicId" element={<TopicDetail type="dsa" />} />

            {/* 404 */}
            <Route path="*" element={<NotFound />} />
          </Routes>
        </Router>
      </AuthProvider>
    </ErrorBoundary>
  );
}

export default App;
