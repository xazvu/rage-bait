import React, { useState } from 'react';

export default function Register() {
  const [username, setUsername] = useState('');
  const handleRegister = () => {
    alert(`Пользователь ${username} зарегистрирован!`);
  };

  return (
    <div className="auth-form">
      <h2>Регистрация</h2>
      <input placeholder="Имя пользователя" value={username} onChange={(e) => setUsername(e.target.value)} />
      <button onClick={handleRegister}>Зарегистрироваться</button>
    </div>
  );
}
