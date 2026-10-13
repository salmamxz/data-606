import csv



class IMDBData:

    # Constructor
    def __init__(self, input_file, output_file):

        # Encapsulation: store the filenames as attributes of the object
        self.input_file = input_file
        self.output_file = output_file


    def transform_data(self):
        try:
            with open(self.input_file, "r", newline="", encoding="utf-8") as csv_file:
                csv_reader = csv.DictReader(csv_file)
                csv_reader.fieldnames = [
                    name.strip() for name in csv_reader.fieldnames
                ]
                fieldnames = [
                    "primaryTitle",
                    "startYear",
                    "runtimeMinutes",
                    "genres"
                ]
                with open(
                    self.output_file, "w", newline="", encoding="utf-8"
                ) as new_file:
                    csv_writer = csv.DictWriter(new_file,fieldnames=fieldnames)

                    #write the column headings into the new CSV file
                    csv_writer.writeheader()
                    #iterate loop through each row in the input CSV
                    for row in csv_reader:
                        if (
                            row.get("titleType") == "movie"
                            and row.get("startYear", "").isdigit()
                            and int(row["startYear"]) >= 2010
                        ):
                            new_row = {
                                "primaryTitle": row["primaryTitle"],
                                "startYear": row["startYear"],
                                "runtimeMinutes": row["runtimeMinutes"],
                                "genres": row["genres"]
                            }

                            csv_writer.writerow(new_row)
            print("IMDb data transformation completed successfully!")

        except FileNotFoundError:
            print("File not found. Check the input file path.")
        except KeyError as error:
            print(f"Column not found: {error}. Check your CSV headers.")


imdb = IMDBData(
    "imdbtitles.csv",
    "imdbtitles_transformed.csv"
)

imdb.transform_data()
