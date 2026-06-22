// /components/ui/Input.jsx
import React from 'react';

const Input = ({ type = "text", placeholder, value, onChange, className = "" }) => {
  return (
    <input 
      type={type}
      placeholder={placeholder}
      value={value}
      onChange={onChange}
      className={`ui-input-field ${className}`}
    />
  );
};

export default Input;