// BudgetSelector.jsx
import React from 'react';
import Selector from './Selector';

export default function BudgetSelector({ selectedBudget, onChange }) {
  const budgets = ['бесплатно', 'дешево', 'дорого'];
  return <Selector options={budgets} selected={selectedBudget} onChange={onChange} label="Бюджет" />;
}