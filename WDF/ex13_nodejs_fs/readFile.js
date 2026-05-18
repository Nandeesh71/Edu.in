# Ex 13 – Node.js Program to Read a File using fs Module

## AIM
To write a Node.js script that reads a text file asynchronously using the `fs` module and displays its content in the console.

## Procedure
1. Create `sample.txt` with some text content.
2. Create `readFile.js` and import the `fs` module.
3. Call `fs.readFile('sample.txt', 'utf8', callback)`.
4. In the callback, check for errors; if none, log the file content.
5. Run with Node.js – the file is read without blocking the main thread.

## Output
```
File Content:
Welcome to Node.js File System Module.
This is a sample text file.
Node.js makes file reading simple using the fs module.
```



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
