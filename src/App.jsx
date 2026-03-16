import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { AuthProvider } from './contexts/AuthContext';
import Home from './pages/Home/Home';
import PythonTopics from './pages/PythonTopics';
import DSATopics from './pages/DSATopics';
import TopicDetail from './pages/TopicDetail/TopicDetail';
import Login from './pages/Auth/Login';
import Register from './pages/Auth/Register';

function App() {
  return (
    <AuthProvider>
      <Router>
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

          {/* Legacy routes for backward compatibility */}
          <Route path="/topic/python/:id" element={<TopicDetail />} />
          <Route path="/topic/dsa/:id" element={<TopicDetail />} />
          <Route path="/topic/:category/:id" element={<TopicDetail />} />
        </Routes>
      </Router>
    </AuthProvider>
  );
}

export default App;
