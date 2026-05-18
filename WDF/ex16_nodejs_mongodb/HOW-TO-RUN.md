# Ex 16 — Node.js: Connect to MongoDB and Retrieve Data

Requirements: Node.js, MongoDB server running.

Steps:

1. Ensure MongoDB server is running (e.g., `mongod`).
2. Open a terminal and change to the exercise folder:

```
cd ex16_nodejs_mongodb
```

3. Install the MongoDB driver and run the script:

```
npm install mongodb
node fetchStudents.js
```

The script connects to `mongodb://localhost:27017`, reads the `studentDB.students` collection and prints the results.
