# Ex No 14 - MongoDB Installation and Database Creation

## Steps

### 1. Install MongoDB
- Download MongoDB Community Server from https://www.mongodb.com/try/download/community
- Run the installer → Choose Complete Installation → Install as a Service

### 2. Start MongoDB Server
```bash
# Option 1: Direct command
mongod

# Option 2: If installed as a Windows Service
net start MongoDB
```
MongoDB listens on port **27017** by default.

### 3. Open MongoDB Shell
```bash
mongosh
```

### 4. Create Database
```js
use studentDB
```

### 5. Insert a Sample Document (triggers DB creation)
```js
db.students.insertOne({ name: "Ishu", age: 20, course: "Web Development" })
```

### 6. Verify Database
```js
show dbs
```

## Expected Output
```
switched to db studentDB
{ acknowledged: true, insertedId: ObjectId("...") }
```
