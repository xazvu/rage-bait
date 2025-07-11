import React from 'react';
import RecommendationList from './RecommendationList';
import './Home.css';

export default function Home() {
  return (
    <div className="home-container">
      <h1>Рекомендации для вас</h1>
      <RecommendationList />
    </div>
  );
}