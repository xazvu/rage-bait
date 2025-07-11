import React, { useState } from 'react';
import { useAuth } from './AuthContext';

export default function ProfileScreen() {
  const { user, login, logout } = useAuth();
  const [username, setUsername] = useState('');
  const [isRegistering, setIsRegistering] = useState(false);

  if (!user) {
    const handleSubmit = () => {
      const role = username === 'admin' ? 'admin' : 'user';
      login(username, role);
    };

    return (
      <div className="auth-form">
        <h2>{isRegistering ? 'Регистрация' : 'Авторизация'}</h2>
        <input
          type="text"
          placeholder="Имя пользователя"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <button onClick={handleSubmit}>
          {isRegistering ? 'Зарегистрироваться' : 'Войти'}
        </button>
        <p style={{ textAlign: 'center', marginTop: '1rem' }}>
          {isRegistering ? (
            <>
              Уже есть аккаунт?{' '}
              <button onClick={() => setIsRegistering(false)}>Войти</button>
            </>
          ) : (
            <>
              Нет аккаунта?{' '}
              <button onClick={() => setIsRegistering(true)}>Регистрация</button>
            </>
          )}
        </p>
      </div>
    );
  }

  if (user.role === 'admin') {
    return (
      <div>
        <h2>Админ-панель</h2>
        <button onClick={logout}>Выйти</button>
        <div className="admin-form">
          <h3>Добавить пост</h3>
          <input placeholder="Название" />
          <textarea placeholder="Описание"></textarea>
          <button>Добавить</button>
        </div>
      </div>
    );
  }

  return (
    <div>
      <h2>Профиль пользователя: {user.username}</h2>
      <button onClick={logout}>Выйти</button>
    </div>
  );
}
