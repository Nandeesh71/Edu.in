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
