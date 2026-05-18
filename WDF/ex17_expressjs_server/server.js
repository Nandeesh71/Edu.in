// Ex No 17 - Express.js Server Creation and Routing
// Setup: npm install express
// Run:   node server.js
// Open browser: http://localhost:3000/

const express = require("express");
const app = express();

// Root route
app.get("/", (req, res) => {
  res.send("Hello, Express!");
});

// Start server on port 3000
app.listen(3000, () => {
  console.log("Server running on port 3000");
});
