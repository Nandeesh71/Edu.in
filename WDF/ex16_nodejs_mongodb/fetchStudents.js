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
