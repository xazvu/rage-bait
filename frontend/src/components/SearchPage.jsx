// src/components/SearchPage.jsx
import React, { useState } from 'react';
import MoodSelector from './MoodSelector';
import BudgetSelector from './BudgetSelector';
import TimeSelector from './TimeSelector';
import RecommendationList from './RecommendationList';
import mockData from '../mockData';
import './SearchPage.css';

export default function SearchPage() {
  const [mood, setMood] = useState('');
  const [budget, setBudget] = useState('');
  const [time, setTime] = useState('');

  const filteredActivities = mockData.filter((activity) =>
    (mood ? activity.mood.includes(mood) : true) &&
    (budget ? activity.budget === budget : true) &&
    (time ? activity.time === time : true)



);




  return (
    <div className="search-container">
      <h2>Подберите активность по фильтрам</h2>
      <MoodSelector selectedMood={mood} onChange={setMood} />
      <BudgetSelector selectedBudget={budget} onChange={setBudget} />
      <TimeSelector selectedTime={time} onChange={setTime} />
      <RecommendationList activities={filteredActivities} />
    </div>
  );
}