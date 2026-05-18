# Ex 11 – Node.js EventEmitter with setTimeout

## AIM
To create a Node.js program that uses the EventEmitter class to define a custom event and trigger it after 3 seconds.

## Procedure
1. Create `eventEmitter.js`.
2. Import the built-in `events` module.
3. Create an `EventEmitter` instance.
4. Register a listener for the `"welcome"` event using `.on()`.
5. Use `setTimeout()` to emit the event after 3000ms.
6. Run with Node.js.

## Output
```
Waiting 3 seconds...
Welcome to Node.js!    ← appears after 3 seconds
```



// Ex No 11 - Node.js EventEmitter and setTimeout
// Run: node eventEmitter.js

const EventEmitter = require('events');

// Create an EventEmitter object
const emitter = new EventEmitter();

// Define the custom event "welcome"
emitter.on('welcome', () => {
  console.log("Welcome to Node.js!");
});

// Trigger the event after 3 seconds
setTimeout(() => {
  emitter.emit('welcome');
}, 3000);
