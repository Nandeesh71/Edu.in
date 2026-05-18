// Ex No 20 - React ToggleText Component using State and Events
// Setup: npx create-react-app toggle-text-app
// Replace src/App.js with this file
// Run: npm start

import React, { useState } from "react";

function ToggleText() {
  const [text, setText] = useState("Hello!");

  const toggleMessage = () => {
    setText(text === "Hello!" ? "Goodbye!" : "Hello!");
  };

  return (
    <div>
      <h2>{text}</h2>
      <button onClick={toggleMessage}>
        Toggle Text
      </button>
    </div>
  );
}

export default ToggleText;
