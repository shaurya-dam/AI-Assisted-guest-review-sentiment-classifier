// /components/ui/Button.jsx
import React from 'react';

const Button = ({ children, onClick, type = "button", variant = "primary", className = "" }) => {
  return (
    <button 
      type={type} 
      onClick={onClick}
      className={`ui-btn variant-${variant} ${className}`}
    >
      {children}
    </button>
  );
};

export default Button;