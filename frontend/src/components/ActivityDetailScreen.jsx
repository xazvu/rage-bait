// src/components/ActivityDetailScreen.jsx
import React from 'react';
import { useParams } from 'react-router-dom';
import mockData from '../mockData';
import ImageCarousel from './ImageCarousel';
import './ActivityDetailScreen.css'

export default function ActivityDetailScreen() {
  const { id } = useParams();
  const activity = mockData.find((a) => a.id === Number(id));

  if (!activity) {
    return <div className="not-found">Активность не найдена</div>;
  }

  return (
    <div className="activity-detail">
      <div className="activity-carousel">
        <ImageCarousel images={activity.imgs} />
      </div>

      <div className="activity-info">
        <h1>{activity.name}</h1>
        <p><strong>Категория:</strong> {activity.category}</p>
        <p><strong>Настроение:</strong> {activity.mood.join(', ')}</p>
        <p><strong>Время:</strong> {activity.time}</p>
        <p><strong>Бюджет:</strong> {activity.budget}</p>
        <button onClick={() => window.history.back()} className="back-button">← Назад</button>
      </div>
    </div>
  );
}