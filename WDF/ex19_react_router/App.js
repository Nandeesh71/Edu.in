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
