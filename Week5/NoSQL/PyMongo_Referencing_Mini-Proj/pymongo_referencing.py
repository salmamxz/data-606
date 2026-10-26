import requests
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["starwars"]
characters = db["characters"]
starships = db["starships"]

API_URL = "https://swapi.dev/api/starships/"


# Get starships function
def get_starships():
    all_starships = []
    next_url = API_URL

    # Handle errors when requesting data from the API.
    try:
        while next_url:
            # Set a timeout so the request does not wait too long.
            response = requests.get(next_url, timeout=15)
            response.raise_for_status()

            # Convert the API response into Python data.
            data = response.json()

            # Add starships from each page to the list.
            all_starships.extend(data["results"])
            next_url = data["next"]

    except requests.RequestException as error:
        print(f"Error retrieving starships: {error}")
        return []

    print(f"Found {len(all_starships)} starships.")
    return all_starships


# Get pilot IDs function
def get_pilot_ids(pilot_urls):
    pilot_ids = []

    for pilot_url in pilot_urls:
        try:
            # First, search for the character using their API URL.
            character = characters.find_one({"url": pilot_url})

            if character:
                # Add the character's MongoDB ObjectId.
                pilot_ids.append(character["_id"])

            else:
                # If not found, retrieve the pilot's details from the API.
                response = requests.get(pilot_url, timeout=15)
                response.raise_for_status()
                pilot_data = response.json()

                # Search for the pilot using their name.
                pilot_name = pilot_data.get("name")

                if pilot_name:
                    character = characters.find_one({"name": pilot_name})

                    if character:
                        pilot_ids.append(character["_id"])
                    else:
                        print(f"Could not find {pilot_name} in MongoDB.")

        except requests.RequestException as error:
            print(f"Error retrieving pilot details: {error}")

        except pymongo.errors.PyMongoError as error:
            print(f"Error accessing character in MongoDB: {error}")

    return pilot_ids


# Replace pilot links with IDs and save starships
def replace_pilots_and_insert():
    try:
        # Retrieve the starships from the API.
        starship_data = get_starships()

        # Stop if the API request failed.
        if not starship_data:
            print("No starships were retrieved.")
            return

        for ship in starship_data:
            # Replace pilot URLs with MongoDB ObjectIds.
            ship["pilots"] = get_pilot_ids(ship.get("pilots", []))

            # Update the starship if it exists, or insert it if it doesn't.
            starships.replace_one(
                {"url": ship["url"]},
                ship,
                upsert=True
            )

        print("Finished saving the starships.")

    except pymongo.errors.PyMongoError as error:
        print(f"Error saving starships to MongoDB: {error}")


# Show starships and their linked pilots
def show_starships_with_pilots():
    try:
        results = starships.aggregate([
            {
                "$lookup": {
                    "from": "characters",
                    "localField": "pilots",
                    "foreignField": "_id",
                    "as": "pilot_details"
                }
            },
            {
                "$project": {
                    "name": 1,
                    "pilot_details.name": 1
                }
            }
        ])

        for ship in results:
            pilot_names = [
                pilot["name"] for pilot in ship["pilot_details"]
            ]

            print(f"Starship: {ship.get('name', 'Unknown')}")
            print(f"Pilots: {pilot_names}")
            print()

    except pymongo.errors.PyMongoError as error:
        print(f"Error displaying starship pilots: {error}")


# Run the process and close the MongoDB connection afterwards
if __name__ == "__main__":
    try:
        replace_pilots_and_insert()
        show_starships_with_pilots()
    finally:
        client.close()
