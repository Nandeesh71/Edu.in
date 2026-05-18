Ex 16 – Node.js Program to Connect MongoDB and Retrieve Data
AIM

To write a Node.js script to connect to MongoDB and retrieve all documents from the students collection.

Procedure

Install MongoDB driver:

npm install mongodb
Import MongoClient from MongoDB package.
Define MongoDB URL and database name.
Connect to MongoDB using MongoClient.
Access students collection and retrieve documents using find().toArray().
Display the retrieved data in the console.


Output
Connected to MongoDB

[
 {
   "_id": "64f8a3c9b7c1a8d123456789",
   "name": "John Doe",
   "age": 20,
   "course": "Computer Science"
 }
]

// Ex No 16 - Node.js Program to Connect MongoDB and Retrieve Data
// Setup: npm install mongodb
// Run:   node fetchStudents.js

const { MongoClient } = require("mongodb");

const url    = "mongodb://localhost:27017";
const dbName = "studentDB";

async function fetchStudents() {
  const client = new MongoClient(url);
  try {
    await client.connect();
    console.log("Connected to MongoDB");

    const db         = client.db(dbName);
    const collection = db.collection("students");
    const students   = await collection.find({}).toArray();

    console.log("Students Collection Data:");
    console.log(students);
  } catch (error) {
    console.error("Error:", error);
  } finally {
    await client.close();
  }
}

fetchStudents();
