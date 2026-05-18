# Ex 12 – Node.js Callback Function for Sum of Two Numbers

## AIM
To write a Node.js function that accepts two numbers and a callback, and uses the callback to compute and display their sum.

## Procedure
1. Create `callbackSum.js`.
2. Define `calculateSum(a, b, callback)` that calls `callback(a, b)`.
3. Define `addNumbers(x, y)` that logs the sum.
4. Call `calculateSum(10, 20, addNumbers)` to demonstrate callback usage.

## Output
```
Sum of the two numbers: 30
```





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
