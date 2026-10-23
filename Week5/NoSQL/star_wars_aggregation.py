from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
client.admin.command("ping")

db = client["starwars"]
characters = db["characters"]
starships = db["starships"]

print("Connected successfully")
print(characters.find_one())
