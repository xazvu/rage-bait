// src/components/Navigation/TopNav.jsx
import React from 'react';
import { NavLink } from 'react-router-dom';
import './TopNav.css';

export default function TopNav() {
  return (
    <nav className="top-nav">
      <h1 className="logo">GwenInfo</h1>
      <div className="nav-links">
        <NavLink to="/" className={({ isActive }) => isActive ? 'nav-link active' : 'nav-link'}>
          Главная
        </NavLink>
        <NavLink to="/search" className={({ isActive }) => isActive ? 'nav-link active' : 'nav-link'}>
          Поиск
        </NavLink>
        <NavLink to="/profile" className={({ isActive }) => isActive ? 'nav-link active' : 'nav-link'}>
          Профиль
        </NavLink>
      </div>
    </nav>
  );
}
