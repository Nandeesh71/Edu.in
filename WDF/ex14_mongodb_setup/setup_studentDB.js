
# Ex 14 – MongoDB Installation and Database Creation

## AIM
To install MongoDB, start the server, and create a database named `studentDB` using the MongoDB shell.

## Procedure
1. Download and install MongoDB Community Edition.
2. Start the MongoDB server.
3. Open the MongoDB shell (`mongosh`).
4. Switch to / create `studentDB`.
5. Insert a document to persist the database.
6. Verify with `show dbs`.

## MongoDB Shell Commands

```js
// Step 1: Switch to the database (creates it on first insert)
use studentDB

// Step 2: Insert a document to persist the DB
db.students.insertOne({ name: "Ishu", age: 20, course: "Web Development" })

// Step 3: Verify
show dbs
```

## Expected Output
```
switched to db studentDB
{ acknowledged: true, insertedId: ObjectId("...") }
```




// Ex No 14 - MongoDB Installation and Database Creation
// Run these commands in MongoDB Shell (mongosh)

// Step 1: Switch to / create the database
use studentDB

// Step 2: Insert a document to trigger database creation
db.students.insertOne({ name: "Ishu", age: 20, course: "Web Development" })

// Step 3: Verify the database appears in the list
show dbs
