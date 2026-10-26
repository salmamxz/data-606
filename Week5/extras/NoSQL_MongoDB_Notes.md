
# MongoDB on Mac: Installation and Basic Commands

## 1. My Setup

- Operating system: macOS
- Package manager: Homebrew
- MongoDB Community Server: 8.0
- MongoDB Compass: Graphical interface
- MongoDB Shell: `mongosh`
- Connection string: `mongodb://localhost:27017`
- Installation method: Direct installation on macOS, without Docker
- PyCharm: Used to write Python code that connects to MongoDB

MongoDB Server runs in the background. Compass lets me explore the database visually, and `mongosh` lets me execute MongoDB commands.

---

## 2. How I Installed MongoDB

### Step 1: Check Homebrew

Run in macOS Terminal:

```bash
brew --version
```

### Step 2: Add the MongoDB repository

```bash
brew tap mongodb/brew
```

### Step 3: Trust the MongoDB repository

My Homebrew version required the repository to be trusted before installing.

```bash
brew trust --formula mongodb/brew/mongodb-community@8.0
brew trust mongodb/brew
```

### Step 4: Install MongoDB Community Server

```bash
brew install mongodb-community@8.0
```

### Step 5: Start MongoDB

```bash
brew services start mongodb-community@8.0
```

### Step 6: Check the service

```bash
brew services list
```

Look for `mongodb-community@8.0` with the status `started`.

### Step 7: Install MongoDB Compass

```bash
brew install --cask mongodb-compass
```

### Step 8: Open MongoDB Compass

```bash
open -a "MongoDB Compass"
```

Connect using:

```text
mongodb://localhost:27017
```

Click **Connect**.

### Step 9: Open MongoDB Shell

Run in macOS Terminal:

```bash
mongosh
```

Or connect explicitly:

```bash
mongosh "mongodb://localhost:27017"
```

To exit the shell:

```javascript
exit
```

---

## 3. Where to Run Commands

| Tool | Purpose | Example |
|---|---|---|
| macOS Terminal | Install and manage MongoDB | `brew services list` |
| MongoDB Shell | Query and manage data | `show dbs` |
| MongoDB Compass | Explore data visually | Insert a document |
| PyCharm | Write and run Python code | `from pymongo import MongoClient` |

**Important:** MongoDB commands such as `show dbs` must be run inside `mongosh`, not directly in macOS Terminal.

---

## 4. Basic MongoDB Commands

### Show databases

```javascript
show dbs
```

### Show the current database

```javascript
db
```

### Select a database

```javascript
use data_academy
```

MongoDB creates the database when data is first stored in it.

### Show collections

```javascript
show collections
```

### Create a collection

```javascript
db.createCollection("students")
```

A collection is similar to a table in a relational database.

---

## 5. Insert Documents

### Insert one document

```javascript
db.students.insertOne({
  name: "Salma",
  course: "Data Academy",
  age: 23
})
```

### Insert multiple documents

```javascript
db.students.insertMany([
  { name: "Ali", course: "Data Academy", age: 25 },
  { name: "Maya", course: "Data Academy", age: 22 },
  { name: "Adam", course: "Data Engineering", age: 27 }
])
```

MongoDB automatically creates an `_id` field when one is not provided.

---

## 6. Find Documents

### Find all documents

```javascript
db.students.find()
```

### Display documents in a readable format

```javascript
db.students.find().pretty()
```

### Find one document

```javascript
db.students.findOne({ name: "Ali" })
```

### Find a student by name

```javascript
db.students.find({ name: "Salma" })
```

### Find students older than 23

```javascript
db.students.find({ age: { $gt: 23 } })
```

### Find students aged 23 or older

```javascript
db.students.find({ age: { $gte: 23 } })
```

### Find students younger than 23

```javascript
db.students.find({ age: { $lt: 23 } })
```

### Find students aged 23 or younger

```javascript
db.students.find({ age: { $lte: 23 } })
```

### Find students whose age is not 23

```javascript
db.students.find({ age: { $ne: 23 } })
```

### Find students with either of two names

```javascript
db.students.find({
  $or: [
    { name: "Salma" },
    { name: "Maya" }
  ]
})
```

---

## 7. Projection, Sorting and Limiting

### Display only the name and course

```javascript
db.students.find(
  {},
  { name: 1, course: 1, _id: 0 }
)
```

### Sort by age ascending

```javascript
db.students.find().sort({ age: 1 })
```

### Sort by age descending

```javascript
db.students.find().sort({ age: -1 })
```

- `1` means ascending.
- `-1` means descending.

### Limit results

```javascript
db.students.find().limit(5)
```

### Skip the first two documents

```javascript
db.students.find().skip(2)
```

### Count all documents

```javascript
db.students.countDocuments({})
```

### Count students older than 23

```javascript
db.students.countDocuments({ age: { $gt: 23 } })
```

---

## 8. Update Documents

### Update one document

```javascript
db.students.updateOne(
  { name: "Salma" },
  { $set: { course: "Data Engineering" } }
)
```

### Update multiple documents

```javascript
db.students.updateMany(
  { course: "Data Academy" },
  { $set: { active: true } }
)
```

### Increase a student's age

```javascript
db.students.updateOne(
  { name: "Ali" },
  { $inc: { age: 1 } }
)
```

### Remove a field

```javascript
db.students.updateOne(
  { name: "Salma" },
  { $unset: { active: "" } }
)
```

- `$set` changes or adds a field.
- `$inc` increases or decreases a numeric field.
- `$unset` removes a field.

---

## 9. Delete Documents

### Delete one document

```javascript
db.students.deleteOne({ name: "Ali" })
```

### Delete multiple documents

```javascript
db.students.deleteMany({ course: "Data Academy" })
```

### Delete all documents in a collection

```javascript
db.students.deleteMany({})
```

**Warning:** `deleteMany({})` deletes every document in that collection. Always check your filter before deleting data.

### Drop a collection

```javascript
db.students.drop()
```

### Drop the current database

```javascript
db.dropDatabase()
```

These commands permanently remove data unless backups are available. Use them carefully.

---

## 10. Important Query Operators

| Operator | Meaning | Example |
|---|---|---|
| `$eq` | Equal to | `{ age: { $eq: 23 } }` |
| `$ne` | Not equal to | `{ age: { $ne: 23 } }` |
| `$gt` | Greater than | `{ age: { $gt: 23 } }` |
| `$gte` | Greater than or equal to | `{ age: { $gte: 23 } }` |
| `$lt` | Less than | `{ age: { $lt: 23 } }` |
| `$lte` | Less than or equal to | `{ age: { $lte: 23 } }` |
| `$in` | Matches any value in a list | `{ age: { $in: [22, 23, 25] } }` |
| `$and` | All conditions must match | `{ $and: [{ age: { $gte: 20 } }, { age: { $lt: 30 } }] }` |
| `$or` | At least one condition matches | `{ $or: [{ age: 22 }, { age: 25 }] }` |
| `$set` | Sets a field value | `{ $set: { age: 24 } }` |
| `$inc` | Increments a number | `{ $inc: { age: 1 } }` |
| `$unset` | Removes a field | `{ $unset: { course: "" } }` |

### Example using `$in`

```javascript
db.students.find({
  age: { $in: [22, 23, 25] }
})
```

### Example using `$and`

```javascript
db.students.find({
  $and: [
    { age: { $gte: 20 } },
    { age: { $lt: 30 } }
  ]
})
```

---

## 11. Arrays and Nested Documents

MongoDB documents can contain arrays and nested objects.

### Insert a document with an array

```javascript
db.students.insertOne({
  name: "Sara",
  skills: ["Python", "SQL", "MongoDB"],
  address: {
    city: "Sheffield",
    country: "UK"
  }
})
```

### Find documents containing Python in the skills array

```javascript
db.students.find({ skills: "Python" })
```

### Find a nested field

```javascript
db.students.find({ "address.city": "Sheffield" })
```

### Add a value to an array

```javascript
db.students.updateOne(
  { name: "Sara" },
  { $push: { skills: "Pandas" } }
)
```

---

## 12. Aggregation

Aggregation processes documents through a series of pipeline stages.

### Count students by course

```javascript
db.students.aggregate([
  {
    $group: {
      _id: "$course",
      totalStudents: { $sum: 1 }
    }
  }
])
```

### Filter and sort students

```javascript
db.students.aggregate([
  { $match: { age: { $gte: 23 } } },
  { $sort: { age: -1 } }
])
```

| Stage | Purpose |
|---|---|
| `$match` | Filters documents |
| `$group` | Groups documents and calculates summaries |
| `$sort` | Sorts documents |
| `$project` | Selects or calculates fields |
| `$limit` | Limits results |
| `$unwind` | Separates array elements into pipeline documents |

---

## 13. Indexes

Indexes help MongoDB find documents more efficiently.

### Create an index

```javascript
db.students.createIndex({ name: 1 })
```

### View indexes

```javascript
db.students.getIndexes()
```

### Remove an index

```javascript
db.students.dropIndex("name_1")
```

Indexes can improve query performance but require storage and can add overhead to writes.

---

## 14. MongoDB Compared with SQL

| SQL | MongoDB |
|---|---|
| Database | Database |
| Table | Collection |
| Row | Document |
| Column | Field |
| Primary key | Usually the `_id` field |
| `SELECT` | `find()` |
| `INSERT` | `insertOne()` or `insertMany()` |
| `UPDATE` | `updateOne()` or `updateMany()` |
| `DELETE` | `deleteOne()` or `deleteMany()` |
| `WHERE` | Query filter |
| `ORDER BY` | `.sort()` |
| `GROUP BY` | `$group` in aggregation |

MongoDB is a NoSQL document database. It stores documents in BSON, a binary representation of JSON-like data.

---

## 15. Connect MongoDB to PyCharm with Python

### Step 1: Install PyMongo

Run in the PyCharm Terminal using your project's Python environment:

```bash
python3 -m pip install pymongo
```

### Step 2: Create `mongodb_test.py`

```python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

# Test the connection
client.admin.command("ping")
print("Connected to MongoDB successfully!")

# Select a database and collection
db = client["data_academy"]
students = db["students"]

# Insert a document
result = students.insert_one({
    "name": "Salma",
    "course": "Data Academy",
    "skills": ["Python", "SQL", "MongoDB"]
})

print("Inserted ID:", result.inserted_id)

# Read documents
for student in students.find():
    print(student)

client.close()
```

Run the Python file. You should see a connection confirmation, the inserted ID and the documents.

**Note:** Running this script multiple times inserts another document each time.

---

## 16. Manage MongoDB on macOS

Run these commands in macOS Terminal.

### Check service status

```bash
brew services list
```

### Start MongoDB

```bash
brew services start mongodb-community@8.0
```

### Stop MongoDB

```bash
brew services stop mongodb-community@8.0
```

### Restart MongoDB

```bash
brew services restart mongodb-community@8.0
```

### Check MongoDB Shell version

```bash
mongosh --version
```

### Connect to MongoDB

```bash
mongosh "mongodb://localhost:27017"
```

### Open Compass

```bash
open -a "MongoDB Compass"
```

### Test the server from `mongosh`

```javascript
db.runCommand({ ping: 1 })
```

A successful response includes `ok: 1`.

---

## 17. Troubleshooting Common Errors

| Error | Solution |
|---|---|
| `mongosh: command not found` | Check that MongoDB Shell is installed and available on your PATH. |
| `ECONNREFUSED` | Check whether MongoDB is running and whether the port is correct. |
| `show: command not found` | Open `mongosh` first. `show dbs` is not a macOS Terminal command. |
| `ModuleNotFoundError: No module named 'pymongo'` | Install PyMongo in the Python environment selected by PyCharm. |
| Compass cannot connect | Check `brew services list` and use `mongodb://localhost:27017`. |
| `E11000 duplicate key error` | A unique key value, often `_id`, already exists. |
| Port 27017 is already in use | Identify the process using the port before changing or stopping anything. |

### Check which process uses port 27017

```bash
lsof -nP -iTCP:27017 -sTCP:LISTEN
```

Do not terminate a process until you have identified it.

---

## 18. Quick Reference for Training

| Task | Command |
|---|---|
| Show databases | `show dbs` |
| Switch database | `use data_academy` |
| Show current database | `db` |
| Show collections | `show collections` |
| Create collection | `db.createCollection("students")` |
| Insert one document | `db.students.insertOne({name: "Salma", age: 23})` |
| Insert many documents | `db.students.insertMany([{name: "Ali"}, {name: "Maya"}])` |
| Find all documents | `db.students.find()` |
| Find one document | `db.students.findOne({name: "Salma"})` |
| Filter documents | `db.students.find({age: {$gt: 23}})` |
| Sort ascending | `db.students.find().sort({age: 1})` |
| Sort descending | `db.students.find().sort({age: -1})` |
| Limit results | `db.students.find().limit(5)` |
| Count documents | `db.students.countDocuments({})` |
| Update a document | `db.students.updateOne({name: "Salma"}, {$set: {age: 24}})` |
| Delete a document | `db.students.deleteOne({name: "Salma"})` |
| Exit the shell | `exit` |

---

## 19. Important Reminders

- MongoDB Server runs in the background.
- Compass is the graphical application.
- `mongosh` is the MongoDB command-line shell.
- MongoDB is installed directly on macOS, not in Docker.
- The local connection string is `mongodb://localhost:27017`.
- MongoDB Shell commands and macOS Terminal commands are different.
- Be careful with deletion and database-drop commands.
- Use `data_academy` and `students` for practice.
- If a trainer's command fails, check whether it is intended for MongoDB Shell, macOS Terminal, or another operating system.

## Official Documentation

- MongoDB installation: https://www.mongodb.com/docs/manual/installation/
- MongoDB Shell: https://www.mongodb.com/docs/mongodb-shell/
- Query operators: https://www.mongodb.com/docs/manual/reference/operator/query/
- PyMongo documentation: https://www.mongodb.com/docs/languages/python/pymongo-driver/current/
