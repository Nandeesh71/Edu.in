Ex 17 – Express.js Server Creation and Routing
AIM

To install Express.js and create a basic Express server that listens on port 3000 and responds with “Hello, Express!” at the root URL.

Procedure

Initialize Node.js project:

npm init -y

Install Express.js:

npm install express
Import Express module and create an Express application.
Define a route for / using app.get().
Start the server using app.listen(3000) .

Open browser and access:

http://localhost:3000

Output

Browser Output

Hello, Express!

Console Output

Server running on port 3000



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
