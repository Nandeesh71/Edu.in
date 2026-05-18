// Ex No 13 - Node.js Read File using fs Module
// Run: node readFile.js

const fs = require('fs');

// Read the file asynchronously
fs.readFile('sample.txt', 'utf8', (error, data) => {
  if (error) {
    console.log("Error reading file:", error);
    return;
  }
  console.log("File Content:\n" + data);
});
