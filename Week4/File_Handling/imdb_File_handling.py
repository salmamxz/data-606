import csv


# OOP: A class is a blueprint for organising code and data
class IMDBData:

    # Constructor: runs when an object is created
    # self refers to the current object
    def __init__(self, input_file, output_file):

        # Encapsulation: store the filenames as attributes of the object
        self.input_file = input_file
        self.output_file = output_file

    # Method: contains the steps for transforming the IMDb data
    def transform_data(self):

        # Error handling: try the code in case an error occurs
        try:

            # File handling: open the input CSV in read mode
            # with automatically closes the file when finished
            with open(self.input_file, "r", newline="", encoding="utf-8") as csv_file:

                # DictReader reads each row as a dictionary
                # using the column names as keys
                csv_reader = csv.DictReader(csv_file)

                # Data cleaning: remove extra spaces from column names
                csv_reader.fieldnames = [
                    name.strip() for name in csv_reader.fieldnames
                ]

                # Select the columns I want to keep in the output
                # This excludes columns such as endYear and isAdult
                fieldnames = [
                    "primaryTitle",
                    "startYear",
                    "runtimeMinutes",
                    "genres"
                ]

                # File handling: open the output CSV in write mode
                # This creates the file or replaces it if it already exists
                with open(
                    self.output_file, "w", newline="", encoding="utf-8"
                ) as new_file:

                    # DictWriter writes dictionary data into the CSV
                    # fieldnames defines the columns in the output file
                    csv_writer = csv.DictWriter(new_file,fieldnames=fieldnames)

                    # Write the column headings into the new CSV file
                    csv_writer.writeheader()

                    # Iteration: loop through each row in the input CSV
                    for row in csv_reader:

                        # Control flow: use if and and to check all conditions
                        # Keep only movies with a valid year from 2010 onwards
                        if (
                            row.get("titleType") == "movie"
                            and row.get("startYear", "").isdigit()
                            and int(row["startYear"]) >= 2010
                        ):

                            # Data transformation: create a new dictionary
                            # containing only the columns I need
                            new_row = {
                                "primaryTitle": row["primaryTitle"],
                                "startYear": row["startYear"],
                                "runtimeMinutes": row["runtimeMinutes"],
                                "genres": row["genres"]
                            }

                            # Write the filtered row into the output CSV
                            csv_writer.writerow(new_row)

            # Display a message when the transformation is completed
            print("IMDb data transformation completed successfully!")

        # Handle the error if the input file cannot be found
        except FileNotFoundError:
            print("File not found. Check the input file path.")

        # Handle a missing column or dictionary key
        except KeyError as error:
            print(f"Column not found: {error}. Check your CSV headers.")


# Create an object of the IMDBData class
# Pass the input and output filenames to the constructor
imdb = IMDBData(
    "imdbtitles.csv",
    "imdbtitles_transformed.csv"
)

# Call the method to run the data transformation
imdb.transform_data()
