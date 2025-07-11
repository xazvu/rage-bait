import React from 'react';
import { NavLink } from 'react-router-dom';
import './BottomNav.css';

export default function BottomNav() {
  return (
    <nav className="bottom-nav">
      <NavLink to="/" className={({ isActive }) => isActive ? 'nav-item active' : 'nav-item'}>
        <span>🏠</span>
        <span>Главная</span>
      </NavLink>
      <NavLink to="/search" className={({ isActive }) => isActive ? 'nav-item active' : 'nav-item'}>
        <span>🔍</span>
        <span>Поиск</span>
      </NavLink>
      <NavLink to="/profile" className={({ isActive }) => isActive ? 'nav-item active' : 'nav-item'}>
        <span>👤</span>
        <span>Профиль</span>
      </NavLink>
    </nav>
  );
}