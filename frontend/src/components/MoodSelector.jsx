// MoodSelector.jsx
import React from 'react';
import Selector from './Selector';

export default function MoodSelector({ selectedMood, onChange }) {
  const moods = ['спокойное', 'нейтральное', 'серьезное'];
  return <Selector options={moods} selected={selectedMood} onChange={onChange} label="Настроение" />;
}