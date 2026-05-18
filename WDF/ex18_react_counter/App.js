// Ex No 18 - React Application with Counter Component
// Setup: npx create-react-app counter-app
// Replace src/App.js with this file
// Run: npm start

import React, { useState } from "react";

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <h2>Counter Value: {count}</h2>
      <button onClick={() => setCount(count + 1)}>
        Increment
      </button>
    </div>
  );
}

export default Counter;
