import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { AuthProvider } from './components/AuthContext';
import Home from './components/Home';
import SearchPage from './components/SearchPage';
import ProfileScreen from './components/ProfileScreen';
import ActivityDetailScreen from './components/ActivityDetailScreen';
import BottomNav from './components/Navigation/BottomNav';
import TopNav from './components/TopNav';
import './styles/App.css';

export default function App() {
  return (
    <AuthProvider>
      <Router>
        <div className="app">
          <TopNav /> {/* верхняя навигация для десктопа */}
          <main className="content">
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/search" element={<SearchPage />} />
              <Route path="/profile" element={<ProfileScreen />} />
              <Route path="/activity/:id" element={<ActivityDetailScreen />} />
            </Routes>
          </main>
          <BottomNav /> {/* нижняя навигация для мобильных */}
        </div>
      </Router>
    </AuthProvider>
  );
}
