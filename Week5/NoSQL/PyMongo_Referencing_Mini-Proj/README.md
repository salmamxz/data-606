# PyMongo Referencing Mini-Project

## Overview
This project uses Python, the Star Wars API and MongoDB to retrieve starship data and link starships to their pilots.

## Technologies
- Python
- Requests
- PyMongo
- MongoDB
- Star Wars API (SWAPI)

## What the project does
1. Retrieves all starships from the Star Wars API, including multiple pages.
2. Searches the MongoDB characters collection to find each pilot.
3. Replaces pilot URLs with MongoDB ObjectIds.
4. Saves the starship documents in the starships collection.
5. Includes basic error handling for API requests and MongoDB operations.

## Database Structure
The project uses the `starwars` database with two collections:
- `characters`: stores character documents.
- `starships`: stores starship documents with references to their pilots.

## How to Run
1. Make sure MongoDB is running locally.
2. Make sure the `characters` collection contains the character documents.
3. Install the required libraries:

   ```bash
   pip install requests pymongo
   ```

4. Run `PyMongo_Referencing_Mini-Proj.py` from PyCharm.

## Learning Outcomes
This project helped me practise API requests, working with MongoDB through PyMongo, referencing documents using ObjectIds, and handling errors.