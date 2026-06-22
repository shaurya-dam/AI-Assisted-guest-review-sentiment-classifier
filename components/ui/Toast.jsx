// /components/ui/Toast.jsx
import React from 'react';

const Toast = ({ message, type = "info", onClose }) => {
  return (
    <div className={`ui-toast toast-${type}`}>
      <span className="toast-text">{message}</span>
      <button onClick={onClose} className="toast-close">&times;</button>
    </div>
  );
};

export default Toast;