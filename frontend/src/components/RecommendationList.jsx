import React from 'react';
import mockData from '../mockData';
import ActivityCard from './ActivityCard';
import './RecommendationList.css';

export default function RecommendationList({ activities }) {
  const list = activities || mockData;

  return (
    <div className="activities-list">
      {list.map((activity) => (
        <ActivityCard key={activity.id} activity={activity} />
      ))}
    </div>
  );
}