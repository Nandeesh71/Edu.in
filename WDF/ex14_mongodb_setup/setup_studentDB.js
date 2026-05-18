// Ex No 14 - MongoDB Installation and Database Creation
// Run these commands in MongoDB Shell (mongosh)

// Step 1: Switch to / create the database
use studentDB

// Step 2: Insert a document to trigger database creation
db.students.insertOne({ name: "Ishu", age: 20, course: "Web Development" })

// Step 3: Verify the database appears in the list
show dbs
