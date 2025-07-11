// TimeSelector.jsx
import React from 'react';
import Selector from './Selector';

export default function TimeSelector({ selectedTime, onChange }) {
  const times = ['долгое', 'среднее', 'короткое'];
  return <Selector options={times} selected={selectedTime} onChange={onChange} label="Время" />;
}