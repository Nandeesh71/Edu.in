Ex 19 – React Router Implementation with Home and About Pages
AIM

To implement React Router in a React application and navigate between Home and About pages without refreshing the browser.

Procedure
Create a React application.

Install React Router:

npm install react-router-dom
Create Home and About components.
Configure routes using BrowserRouter, Routes, and Route.
Add navigation links using Link.

Run the application using:

npm start


Output
Home Page

About Page

Navigation works without page refresh.


// Ex No 19 - React Router Implementation with Home and About Pages
// Setup: npx create-react-app router-app
//        npm install react-router-dom
// Replace src/App.js with this file, add Home.js and About.js in src/
// Run: npm start

import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import Home from "./Home";
import About from "./About";

function App() {
  return (
    <BrowserRouter>
      <nav>
        <Link to="/">Home</Link> |{" "}
        <Link to="/about">About</Link>
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
