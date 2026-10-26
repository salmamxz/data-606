
import requests
import pymongo
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["starwars"]
characters = db["characters"]
starships = db["starships"]

API_URL = "https://swapi.dev/api/starships/"


def create_session():
    retry = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET"]
    )

    session = requests.Session()
    session.mount("https://", HTTPAdapter(max_retries=retry))
    return session


# Get all the starships from the api
def get_starships(session):
    all_starships = []
    next_url = API_URL

    while next_url:
        response = session.get(next_url, timeout=15)
        response.raise_for_status()
        data = response.json()
        all_starships.extend(data["results"])
        next_url = data["next"]
    print(f"Found {len(all_starships)} starships.")
    return all_starships


#fixing ids for each pilot
def get_pilot_ids(pilot_urls, session):
    pilot_ids = []

    for pilot_url in pilot_urls:
        # Check if the pilot is already in our characters collection
        character = characters.find_one({"url": pilot_url})

        if character:
            pilot_ids.append(character["_id"])
        else:
            # Get the pilot's name from the API if needed
            try:
                response = session.get(pilot_url, timeout=15)
                response.raise_for_status()
                pilot_data = response.json()
                pilot_name = pilot_data.get("name")

                if pilot_name:
                    character = characters.find_one({"name": pilot_name})

                    if character:
                        pilot_ids.append(character["_id"])
                    else:
                        print(f"Could not find {pilot_name} in MongoDB.")
                else:
                    print(f"Could not get the pilot's name: {pilot_url}")

            except requests.RequestException as error:
                print(f"Could not get pilot details: {error}")

    return pilot_ids


# Replace the pilot URLs with IDs and save the starships
def replace_pilots_and_insert(starship_data, session):
    for ship in starship_data:
        ship["pilots"] = get_pilot_ids(ship.get("pilots", []), session)

        try:
            starships.replace_one(
                {"url": ship["url"]},
                ship,
                upsert=True
            )
        except pymongo.errors.PyMongoError as error:
            print(f"Could not save {ship.get('name', 'starship')}: {error}")

    print("Finished saving the starships.")


# Check that the pilot IDs link to actual characters and all is working correctly
def check_pilots():
    pipeline = [
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
                "_id": 0,
                "name": 1,
                "pilots": 1,
                "matched_pilots": "$pilot_details.name",
                "pilot_count": {"$size": "$pilots"},
                "matched_count": {"$size": "$pilot_details"}
            }
        }
    ]

    for ship in starships.aggregate(pipeline):
        print(ship)

        if ship["pilot_count"] != ship["matched_count"]:
            print(f"Some pilot references are missing for {ship['name']}.")


#main
def main():
    session = create_session()

    try:
        client.admin.command("ping")
        if characters.count_documents({}) == 0:
            print("The characters collection is empty. Check the database name.")
            return

        starship_data = get_starships(session)
        replace_pilots_and_insert(starship_data, session)
        check_pilots()

    except (requests.RequestException, pymongo.errors.PyMongoError, KeyError) as error:
        print(f"Something went wrong: {error}")

    finally:
        session.close()
        client.close()


if __name__ == "__main__":
    main()