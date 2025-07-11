// src/components/ActivityCard.jsx
import React from 'react';
import { Link } from 'react-router-dom';
import './ActivityCard.css';

export default function ActivityCard({ activity }) {
  const mainImage = activity.imgs.find((img) => img.is_main)?.url;

  return (
    <Link to={`/activity/${activity.id}`} className="activity-card">
      <div className="activity-image">
        <img src={mainImage} alt={activity.name} />
      </div>
      <div className="activity-content">
        <div className="activity-header">
          <h3 className="activity-title">{activity.name}</h3>
          <div className="rating">
            <span>★</span>
            <span>4.8</span>
          </div>
        </div>
        <p className="activity-description">Настроение: {activity.mood.join(', ')}</p>
        <div className="activity-footer">
          <div className="activity-badges">
            <span className="activity-badge">{activity.category}</span>
            <span className="activity-badge secondary">{activity.time}</span>
          </div>
        </div>
      </div>
    </Link>
  );
}