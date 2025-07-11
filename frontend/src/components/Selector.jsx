// src/components/Selector.jsx
import React from 'react';

export default function Selector({ options, selected, onChange, label }) {
  return (
    <div className="selector">
      <h4>{label}</h4>
      <div className="selector-buttons">
        {options.map((option) => (
          <button
            key={option}
            onClick={() => onChange(option)}
            className={selected === option ? 'active' : ''}
          >
            {option.charAt(0).toUpperCase() + option.slice(1)}
          </button>
        ))}
      </div>
    </div>
  );
}