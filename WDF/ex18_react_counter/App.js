Ex 18 – React Application with Counter Component
AIM

To create a React application with a Counter component that increments and displays the count value when a button is clicked.

Procedure

Create a React application:

npx create-react-app counter-app

Move to project folder:

cd counter-app

Start the React application:

npm start
Create a Counter component using useState.
Add a button to increase the count value.
Save the file and view the output in the browser.

Output
Counter Value: 0

[Increment Button]

After Click:
Counter Value: 1



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
