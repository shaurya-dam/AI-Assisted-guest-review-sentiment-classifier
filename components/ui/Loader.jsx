// /components/ui/Loader.jsx
import React from 'react';

const Loader = ({ size = "medium" }) => {
  return (
    <div className={`ui-loader loader-${size}`}>
      <span className="sr-only">Processing Vector Matrix Pipeline...</span>
    </div>
  );
};

export default Loader;