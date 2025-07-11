import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from './AuthContext';

export default function Login() {
  const { login } = useAuth();
  const [username, setUsername] = useState('');
  const navigate = useNavigate();

  const handleLogin = () => {
    const role = username === 'admin' ? 'admin' : 'user';
    login(username, role);
    navigate('/profile');
  };

  return (
    <div className="auth-form">
      <h2>Вход</h2>
      <input placeholder="Имя пользователя" value={username} onChange={(e) => setUsername(e.target.value)} />
      <button onClick={handleLogin}>Войти</button>
    </div>
  );
}
