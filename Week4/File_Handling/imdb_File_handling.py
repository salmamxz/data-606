import csv
class IMDBData:

    # Constructor
    def __init__(self, input_file, output_file):

        #store the filenames as attributes of the object
        self.input_file = input_file
        self.output_file = output_file
    def transform_data(self):
        try:
            #e
            with open(self.input_file, "r", newline="", encoding="utf-8") as csv_file:
                csv_reader = csv.DictReader(csv_file)
                #t
                csv_reader.fieldnames = [
                    name.strip() for name in csv_reader.fieldnames
                ]
                fieldnames = ["primaryTitle","startYear","runtimeMinutes","genres"]
                #l
                with open(
                    self.output_file, "w", newline="", encoding="utf-8"
                ) as new_file:
                    csv_writer = csv.DictWriter(new_file,fieldnames=fieldnames)

                    #write the column headings into the outputt
                    csv_writer.writeheader()
                    #iterate loop for each row in the input filee
                    for row in csv_reader:
                        if (
                            row.get("titleType") == "movie"
                            and row.get("startYear", "").isdigit()
                            and int(row["startYear"]) >= 2010
                        ):
                            new_row = {"primaryTitle": row["primaryTitle"],"startYear": row["startYear"],"runtimeMinutes": row["runtimeMinutes"],"genres": row["genres"]}
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
