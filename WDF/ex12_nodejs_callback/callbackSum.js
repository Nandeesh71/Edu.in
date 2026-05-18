// Ex No 12 - Node.js Callback Function for Sum of Two Numbers
// Run: node callbackSum.js

// Function that accepts two numbers and a callback
function calculateSum(a, b, callback) {
  callback(a, b);
}

// Callback function to return the sum
function addNumbers(x, y) {
  console.log("Sum of the two numbers:", x + y);
}

// Function call
calculateSum(10, 20, addNumbers);
