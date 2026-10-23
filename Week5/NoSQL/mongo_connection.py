from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")


client.admin.command("ping")
print("Connected to MongoDB successfully!")


db = client["book_library"]
books = db["books"]


for book in books.find():
    print(book)


books.insert_one({
    "title": "The Spanish Love Deception",
    "author": "Elena Armas",
    "genre": "Romance",
    "year": 2021,
    "rating": 4.5
})


for book in books.find():
    print(book)


books.update_one(
    {"title": "The Spanish Love Deception"},
    {"$set": {"rating": 4.7}}
)


books.delete_one({"title": "The Spanish Love Deception"})

client.close()