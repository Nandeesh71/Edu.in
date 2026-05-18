// Ex No 15 - MongoDB Collection Creation and Document Insertion
// Run these commands in MongoDB Shell (mongosh)

// Step 1: Start MongoDB shell
// mongosh

// Step 2: Switch to studentDB
use studentDB

// Step 3: Insert document into students collection
db.students.insertOne({
  name: "John Doe",
  age: 20,
  course: "Computer Science"
})

// Step 4: Retrieve and display all documents
db.students.find()
