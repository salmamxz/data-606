# Star Wars Starship Data Pipeline

## Project Overview

This project retrieves starship data from the [Star Wars API (SWAPI)](https://swapi.dev/) using Python and stores it in MongoDB.

The main objective is to retrieve all available starships, replace the pilot URLs with MongoDB ObjectIDs from the existing `characters` collection, and save the starships in a separate `starships` collection.

The project also includes error handling, unit testing, mocking and a MongoDB aggregation query to verify that starships are correctly linked to their pilots.

## Technologies Used

- **Python**: Extracts, transforms and processes the data.
- **Requests**: Sends HTTP requests to the Star Wars API.
- **MongoDB**: Stores the characters and starship data.
- **PyMongo**: Connects Python to MongoDB and performs database operations.
- **MongoMock**: Provides a simulated MongoDB database for unit testing.
- **Unittest**: Tests individual functions and expected behaviour.
- **Mock and Patch**: Replace external dependencies during testing.

## Project Requirements

The project meets the following requirements:

- Retrieve all available starships from SWAPI, including paginated results.
- Collect pilot information from the API.
- Replace pilot URLs with MongoDB ObjectIDs.
- Insert new starships and update existing records without creating duplicates.
- Handle API and MongoDB errors.
- Use comments to explain the code.
- Write unit tests using `unittest`, `mongomock` and `unittest.mock`.
- Use MongoDB `$lookup` to display starships alongside their pilots.

## How It Works

The project follows an Extract, Transform and Load (ETL) process.

### 1. Extract

The `get_starships()` function retrieves starships from the SWAPI starships endpoint.

It follows the API's pagination links until all pages have been retrieved. The results are combined into a single Python list.

Error handling and a 15-second timeout help manage failed or unresponsive requests.

### 2. Transform

The `get_pilot_ids()` function processes the pilot URLs associated with each starship.

It searches for each pilot in the existing `characters` collection, first using the API URL and then using the character's name if necessary.

When a matching character is found, its MongoDB ObjectID is added to the pilot list.

This replaces the original pilot URLs with references to documents in MongoDB.

### 3. Load

The `replace_pilots_and_insert()` function processes the starships and saves them to the `starships` collection.

The `replace_one()` operation uses the starship's API URL to identify an existing record. Setting `upsert=True` updates an existing record or inserts it if it does not exist.

This makes the process repeatable without creating duplicate records for the same starship URL.

### 4. Verify Relationships

The `show_starships_with_pilots()` function uses MongoDB's `$lookup` aggregation stage to join the `starships` and `characters` collections.

It matches the pilot ObjectIDs in the starship documents against the `_id` values in the characters collection, allowing the pilot names to be displayed alongside their starships.

## Database Structure

The project uses a MongoDB database named `starwars`.

| Collection | Purpose |
|---|---|
| `characters` | Stores character information, including names and API URLs. |
| `starships` | Stores starship information and references to their pilots. |

The `pilots` field in each starship document contains a list of MongoDB ObjectIDs rather than API URLs.

This allows relationships between starships and characters to be verified using MongoDB aggregation.

## Error Handling

The project includes error handling for common failures:

- **API request errors:** Handles connection problems, timeouts and unsuccessful HTTP responses.
- **MongoDB errors:** Handles database access and data-saving errors.
- **Missing pilot records:** Reports when a pilot cannot be matched to a character in the database.
- **Empty API results:** Stops the loading process if no starships are retrieved.
- **Connection management:** Closes the MongoDB connection when the main process finishes.

## Unit Testing and Mocking

The project includes unit tests in `test_pymongo_referencing.py`.

The tests use `unittest` to check that the functions behave as expected and `mongomock` to simulate MongoDB without requiring a real database for the tests.

### Tests Included

**1. Test pilot ObjectID retrieval**

Checks that `get_pilot_ids()` returns the correct MongoDB ObjectID when a pilot already exists in the characters collection.

**2. Test starship insertion**

Checks that `replace_pilots_and_insert()` saves a starship and replaces its pilot URL with the correct MongoDB ObjectID.

**3. Mock external dependencies**

The tests mock the starship retrieval function so the insertion test uses controlled test data rather than relying on a live API response.

The character and starship collections are also replaced with mock collections to isolate the tests from the real database.

### Run the Tests

From the project directory, run:

```bash
python -m unittest -v test_pymongo_referencing.py
```

The tests should run without making changes to the real MongoDB database.

## Installation and Setup

### Prerequisites

- Python 3.10 or later.
- MongoDB running locally or an accessible MongoDB instance.
- Git.

### 1. Clone the Repository

```bash
git clone https://github.com/salmamxz/data-606.git
cd data-606
```

Navigate to the folder containing the project files if the script is stored in a subdirectory.

### 2. Install Dependencies

```bash
python -m pip install requests pymongo mongomock
```

### 3. Prepare MongoDB

Ensure MongoDB is running at:

```text
mongodb://localhost:27017/
```

The project expects an existing `starwars` database with a populated `characters` collection.

The characters must include their names and SWAPI URLs so that the pilot references can be resolved.

### 4. Run the Project

Run the main Python script:

```bash
python pymongo_referencing.py
```

The script retrieves the starships, replaces pilot URLs with ObjectIDs, saves the data to MongoDB and displays the starships with their linked pilots.

### 5. Run the Unit Tests

```bash
python -m unittest -v test_pymongo_referencing.py
```

## Expected Results

The project requirements specify **36 starships**.

After running the script successfully, the `starships` collection should contain 36 distinct starships, assuming the API returns the expected data and all records are processed successfully.

The terminal should display the number of starships retrieved and a list of starships with their associated pilot names.

Some starships may have no pilots, and some pilot references may not resolve if their character records are missing from the database.

## Future Improvements

Possible improvements include:

- Adding retry logic for temporary API failures.
- Using bulk database operations to improve performance.
- Adding more unit tests for API failures, missing pilots and MongoDB errors.
- Validating that all 36 starships have been saved successfully.
- Improving pilot matching and reporting unresolved references.
- Refactoring the functions into classes to follow an object-oriented design.

## Learning Outcomes

This project demonstrates practical experience with REST APIs, Python functions, NoSQL databases, MongoDB document relationships, data transformation, error handling, unit testing and mocking.

It also demonstrates how an ETL-style process can extract data from an external API, transform relationships between documents and load the resulting data into MongoDB.

## Data Source

All starship data originates from the [Star Wars API (SWAPI)](https://swapi.dev/).
