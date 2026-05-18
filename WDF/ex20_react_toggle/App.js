Ex 20 – React ToggleText Component using State and Events
AIM

To create a React component named ToggleText that toggles between “Hello!” and “Goodbye!” when a button is clicked.

Procedure
Create a React application using create-react-app.
Import useState from React.
Create a ToggleText component.
Initialize state with the text "Hello!".
Add a button with onClick event handling.
Toggle the text between "Hello!" and "Goodbye!".


Output
Hello!

[Toggle Button]

After Click:
Goodbye!


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
