Ex 15 – MongoDB Collection Creation and Document Insertion
AIM

To create a database named studentDB, create a collection called students, and insert a document containing student details using the MongoDB shell.

Procedure
Open MongoDB shell using mongosh.

Create and switch to the database using:

use studentDB

Insert a document into the students collection:

db.students.insertOne({
  name: "John Doe",
  age: 20,
  course: "Computer Science"
})

Display the inserted document using:

db.students.find()


Output
{
 "_id" : ObjectId("64f8a3c9b7c1a8d123456789"),
 "name" : "John Doe",
 "age" : 20,
 "course" : "Computer Science"
}



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
