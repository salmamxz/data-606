
import unittest
from unittest.mock import patch
from bson import ObjectId
import mongomock
import pymongo_referencing as project


class TestStarshipPilots(unittest.TestCase):

    def setUp(self):
        self.client = mongomock.MongoClient()
        self.db = self.client["starwars"]
        self.characters = self.db["characters"]
        self.starships = self.db["starships"]

        self.pilot_id = ObjectId()
        self.characters.insert_one({
            "_id": self.pilot_id,
            "name": "Luke Skywalker",
            "url": "https://swapi.dev/api/people/1/"
        })

        self.p1 = patch.object(project, "characters", self.characters)
        self.p2 = patch.object(project, "starships", self.starships)
        self.p1.start()
        self.p2.start()

    def tearDown(self):
        self.p1.stop()
        self.p2.stop()
        self.client.close()

    def test_get_pilot_ids(self):
        result = project.get_pilot_ids([
            "https://swapi.dev/api/people/1/"
        ])
        self.assertEqual(result, [self.pilot_id])

    def test_starship_saved_with_correct_pilot(self):
        test_data = [{
            "name": "X-wing",
            "url": "https://swapi.dev/api/starships/12/",
            "pilots": ["https://swapi.dev/api/people/1/"]
        }]

        with patch.object(project, "get_starships", return_value=test_data):
            project.replace_pilots_and_insert()

        ship = self.starships.find_one({"name": "X-wing"})
        self.assertEqual(ship["pilots"], [self.pilot_id])


if __name__ == "__main__":
    unittest.main()
